# -*- mode: ruby -*-
# vi: set ft=ruby :
VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(2) do |config|
  config.vm.define :ansible do | ansible |
    ansible.vm.hostname = "ansible"
    ansible.vm.box      = "CentOS65"
    ansible.vm.box_url  = "https://github.com/2creatives/vagrant-centos/releases/download/v6.5.3/centos65-x86_64-20140116.box"
    ansible.vm.network :private_network, ip: "192.168.33.200"
    ansible.vm.provider "virtualbox" do | v |
      v.customize ["modifyvm", :id, "--memory", "2048"]
      v.customize ["modifyvm", :id, "--natdnsproxy1", "off"]
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "off"]
    end
  end
end
