# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.box = "debian/jessie64"

  #config.vm.define "alfred_home" do |alfred_home|
  #end

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
    vb.name = "alfred_home"
  end

  config.vm.provision "ansible" do |ansible|
    #ansible.groups = {
    #  "batcave" => ["alfred_home"],
    #  "all_groups:children" => ["batcave"]
    #}

    ansible.playbook = "alfred-install.yml"
  end

end
