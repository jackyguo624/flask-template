# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

disk1 = './tmp/large_disk1.vdi'
disk2 = './tmp/large_disk2.vdi'
disk3 = './tmp/large_disk3.vdi'

disk11 = './tmp/large_disk11.vdi'
disk22 = './tmp/large_disk22.vdi'
disk33 = './tmp/large_disk33.vdi'

Vagrant.configure(2) do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
config.ssh.insert_key = false
#config.ssh.password ="1"	
  config.vm.define "cephmaster" do |cephmaster|
    cephmaster.vm.box = "ubuntu/xenial64"
    cephmaster.vm.hostname = "cephmaster"
    cephmaster.vm.network "private_network", ip: "192.168.50.10"
    cephmaster.ssh.shell="bash"
  end

  config.vm.define "ceph1" do |ceph1|
    ceph1.vm.box =  "ubuntu/xenial64" # "ubuntu/trusty64"
    ceph1.vm.hostname = "ceph1"
    ceph1.vm.network "private_network", ip: "192.168.50.11"
    config.vm.network "forwarded_port", guest: 7480, host: 37480
    ceph1.ssh.shell="bash"

    #ceph1.vm.provider "virtualbox" do |vb|
    #  unless File.exist?(disk1)
    #    vb.customize ['createhd', '--filename', disk1, '--variant', 'Fixed', '--size', 20 * 1024]
    #  end
    #  unless File.exist?(disk11)
    #    vb.customize ['createhd', '--filename', disk11, '--variant', 'Fixed', '--size', 20 * 1024]
    #  end
    #  vb.memory = "2048"
    #  vb.customize ['storageattach', :id,  '--storagectl', 'SCSI', '--port', 2, '--device', 0, '--type', 'hdd', '--medium', disk1]
    #  vb.customize ['storageattach', :id,  '--storagectl', 'SCSI', '--port', 3, '--device', 0, '--type', 'hdd', '--medium', disk11]
    #end
  end

  config.vm.define "ceph2" do |ceph2|
    ceph2.vm.box = "ubuntu/xenial64" #"ubuntu/trusty64"
    ceph2.vm.hostname = "ceph2"
    ceph2.vm.network "private_network", ip: "192.168.50.12"
    ceph2.vm.network "forwarded_port", guest: 80, host: 3080
    #ceph2.vm.provider "virtualbox" do |vb|
    #  unless File.exist?(disk2)
    #    vb.customize ['createhd', '--filename', disk2, '--variant', 'Fixed', '--size', 20 * 1024]
    #  end
    #  unless File.exist?(disk22)
    #    vb.customize ['createhd', '--filename', disk22, '--variant', 'Fixed', '--size', 20 * 1024]
    #  end
    #  vb.memory = "1024"
    #  vb.customize ['storageattach', :id,  '--storagectl', 'SCSI', '--port', 2, '--device', 0, '--type', 'hdd', '--medium', disk2]
    #  vb.customize ['storageattach', :id,  '--storagectl', 'SCSI', '--port', 3, '--device', 0, '--type', 'hdd', '--medium', disk22]
    #end
  end

  config.vm.define "ceph3" do |ceph3|
    ceph3.vm.box = "ubuntu/xenial64"
    ceph3.vm.hostname = "ceph3"
    ceph3.vm.network "private_network", ip: "192.168.50.13"
    ceph3.ssh.shell="bash"
    #ceph3.vm.provider "virtualbox" do |vb|
    #  unless File.exist?(disk3)
    #    vb.customize ['createhd', '--filename', disk3, '--variant', 'Fixed', '--size', 20 * 1024]
    #  end
    #  unless File.exist?(disk33)
    #    vb.customize ['createhd', '--filename', disk33, '--variant', 'Fixed', '--size', 20 * 1024]
    #  end
    #  vb.memory = "1024"
    #  vb.customize ['storageattach', :id,  '--storagectl', 'SCSI', '--port', 2, '--device', 0, '--type', 'hdd', '--medium', disk3]
    #  vb.customize ['storageattach', :id,  '--storagectl', 'SCSI', '--port', 3, '--device', 0, '--type', 'hdd', '--medium', disk33]
    #end
  end

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # config.vm.network "forwarded_port", guest: 80, host: 8080

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  # config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
  #   vb.memory = "1024"
  # end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # config.vm.provision "shell", inline: <<-SHELL
  #   sudo apt-get update
  #   sudo apt-get install -y apache2
  # SHELL
end
