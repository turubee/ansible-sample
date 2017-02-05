#####
# Output statics json file callback
# How to use:
#  1. set environment variable.
#    $ export ANSIBLE_CALLBACK_PLUGINS=etc/callback_plugins/
#  2. execute ansible-playbook command usually.
#
# output files:
#  results.json - all results. to append the element in file.
#    *** must delete operation manually  ***
#  result-[playbookname].json - each playbook result.
#####
import os
import json
import pprint
from datetime import datetime

class CallbackModule(object):
    def __init__(self):
        self.link = None
        self.hosts_name = None
        self.results_dir = 'results'
        if not os.path.exists(self.results_dir):
            os.makedirs(self.results_dir)

    def playbook_on_play_start(self, name):
        self.hosts_name = self.play.hosts
        jenkins_build_url = self.playbook.extra_vars.get("jenkins_build_url")
        if jenkins_build_url:
            self.link = jenkins_build_url + 'artifact/logs/' + self.hosts_name + '.log'

    def playbook_on_stats(self, stats):
        hosts = sorted(stats.processed.keys())
        result_hosts = []
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(stats)
        (r_ok, r_changed, r_unreachable, r_failures, t_ok, t_changed, t_unreachable, t_failures) = (0, 0, 0, 0, 0, 0, 0, 0)
        now = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        for host in hosts:
            s = stats.summarize(host)
            dict = {
                "host": host,
                "result": {
                    "ok": s['ok'],
                    "changed": s['changed'],
                    "unreachable": s['unreachable'],
                    "failures": s['failures']
                }
            }
            result_hosts.append(dict)
            # total counts
            r_ok += s['ok']
            r_changed += s['changed']
            r_unreachable += s['unreachable']
            r_failures += s['failures']
            # total hosts
            t_ok = t_ok+1 if (s['changed']+s['unreachable']+s['failures']) ==0 else t_ok
            t_changed = t_changed+1 if s['changed'] > 0 else t_changed
            t_unreachable = t_unreachable+1 if s['unreachable'] > 0 else t_unreachable
            t_failures = t_failures+1 if s['failures'] > 0 else t_failures

        result = {
            "playbook": self.hosts_name,
            "checkdate": now,
            "hosts": result_hosts,
            "link": self.link,
            "task_summary": {
                "ok": r_ok,
                "changed": r_changed,
                "unreachable": r_unreachable,
                "failures": r_failures
            },
            "host_summary": {
                "ok": t_ok,
                "changed": t_changed,
                "unreachable": t_unreachable,
                "failures": t_failures
            }
        }

        # Write current playbook result file
        playbook_results_path = os.path.join(
                self.results_dir, 'result-' + self.hosts_name + '.json' )
        playbook_result_json = json.dumps(result)
        with open(playbook_results_path, 'w') as f:
            f.write(playbook_result_json)

        # Write (append) all result file
        results_path = os.path.join(self.results_dir, 'results.json')
        all_result_json=json.loads('[]')
        if os.path.exists(results_path):
            with open(results_path, 'r') as f:
                all_result_json = json.load(f)
        all_result_json.append(result)
        with open(results_path, 'w') as f:
            f.write(json.dumps(all_result_json))
