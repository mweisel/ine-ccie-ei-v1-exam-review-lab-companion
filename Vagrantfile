# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box_check_update = false
  config.vm.provider :libvirt do |lv|
    lv.suspend_mode = "managedsave"
    lv.management_network_keep = true
  end

  config.vm.define "r1" do |node|
    node.vm.box = "cisco-iosv"
    node.vm.provider :libvirt do |domain|
      domain.management_network_mac = "52:54:00:f4:e1:51"
    end
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/1",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.1.1",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.2.1",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/2",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.1.2",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.3.1",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/3",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.1.3",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.4.1",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/4",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.1.4",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.5.1",
      :libvirt__tunnel_port => "10001",
      auto_config: false
  end

  config.vm.define "r2" do |node|
    node.vm.box = "cisco-iosv"
    node.vm.provider :libvirt do |domain|
      domain.management_network_mac = "52:54:00:42:f3:17"
    end
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/1",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.2.1",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.1.1",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/2",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.2.2",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.6.1",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/3",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.2.3",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.10.2",
      :libvirt__tunnel_port => "10001",
      auto_config: false
  end

  config.vm.define "r3" do |node|
    node.vm.box = "cisco-iosv"
    node.vm.provider :libvirt do |domain|
      domain.management_network_mac = "52:54:00:ac:6e:fe"
    end
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/1",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.3.1",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.1.2",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/2",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.3.2",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.7.2",
      :libvirt__tunnel_port => "10001",
      auto_config: false
  end

  config.vm.define "r4" do |node|
    node.vm.box = "cisco-iosv"
    node.vm.provider :libvirt do |domain|
      domain.management_network_mac = "52:54:00:cd:73:ad"
    end
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/1",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.4.1",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.1.3",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/2",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.4.2",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.13.1",
      :libvirt__tunnel_port => "10001",
      auto_config: false
  end

  config.vm.define "r5" do |node|
    node.vm.box = "cisco-iosv"
    node.vm.provider :libvirt do |domain|
      domain.management_network_mac = "52:54:00:b1:57:a1"
    end
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/1",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.5.1",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.1.4",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/2",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.5.2",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.8.2",
      :libvirt__tunnel_port => "10001",
      auto_config: false
  end

  config.vm.define "r6" do |node|
    node.vm.box = "cisco-iosv"
    node.vm.provider :libvirt do |domain|
      domain.management_network_mac = "52:54:00:5c:ea:72"
    end
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/1",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.6.1",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.2.2",
      :libvirt__tunnel_port => "10001",
      auto_config: false
  end

  config.vm.define "r7" do |node|
    node.vm.box = "cisco-iosv"
    node.vm.provider :libvirt do |domain|
      domain.management_network_mac = "52:54:00:c6:3b:65"
    end
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/1",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.7.1",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.20.1",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/2",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.7.2",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.3.2",
      :libvirt__tunnel_port => "10001",
      auto_config: false
  end

  config.vm.define "r8" do |node|
    node.vm.box = "cisco-iosv"
    node.vm.provider :libvirt do |domain|
      domain.management_network_mac = "52:54:00:a5:59:b5"
    end
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/1",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.8.1",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.20.2",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/2",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.8.2",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.5.2",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/3",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.8.3",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.14.2",
      :libvirt__tunnel_port => "10001",
      auto_config: false
  end

  config.vm.define "r9" do |node|
    node.vm.box = "cisco-iosv"
    node.vm.provider :libvirt do |domain|
      domain.management_network_mac = "52:54:00:94:59:ef"
    end
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/1",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.9.1",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.20.3",
      :libvirt__tunnel_port => "10001",
      auto_config: false
  end

  config.vm.define "r10" do |node|
    node.vm.box = "cisco-iosv"
    node.vm.provider :libvirt do |domain|
      domain.management_network_mac = "52:54:00:8e:88:fc"
    end
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/1",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.10.1",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.15.1",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/2",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.10.2",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.2.3",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/3",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.10.3",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.13.3",
      :libvirt__tunnel_port => "10001",
      auto_config: false
  end

  config.vm.define "r11" do |node|
    node.vm.box = "cisco-iosv"
    node.vm.provider :libvirt do |domain|
      domain.management_network_mac = "52:54:00:90:e4:c0"
    end
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/1",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.11.1",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.15.2",
      :libvirt__tunnel_port => "10001",
      auto_config: false
  end

  config.vm.define "r12" do |node|
    node.vm.box = "cisco-iosv"
    node.vm.provider :libvirt do |domain|
      domain.management_network_mac = "52:54:00:b1:e3:1d"
    end
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/1",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.12.1",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.15.3",
      :libvirt__tunnel_port => "10001",
      auto_config: false
  end

  config.vm.define "r13" do |node|
    node.vm.box = "cisco-iosv"
    node.vm.provider :libvirt do |domain|
      domain.management_network_mac = "52:54:00:d9:eb:fd"
    end
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/1",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.13.1",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.4.2",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/2",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.13.2",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.14.1",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/3",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.13.3",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.10.3",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/4",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.13.4",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.16.1",
      :libvirt__tunnel_port => "10001",
      auto_config: false
  end

  config.vm.define "r14" do |node|
    node.vm.box = "cisco-iosv"
    node.vm.provider :libvirt do |domain|
      domain.management_network_mac = "52:54:00:26:c4:c0"
    end
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/1",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.14.1",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.13.2",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/2",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.14.2",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.8.3",
      :libvirt__tunnel_port => "10001",
      auto_config: false
  end

  config.vm.define "sw1" do |node|
    node.vm.box = "cisco-iosvl2"
    node.vm.provider :libvirt do |domain|
      domain.management_network_mac = "52:54:00:4f:ae:45"
    end
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/1",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.15.1",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.10.1",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/2",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.15.2",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.11.1",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/3",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.15.3",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.12.1",
      :libvirt__tunnel_port => "10001",
      auto_config: false
  end
  
  config.vm.define "sw2" do |node|
    node.vm.box = "cisco-iosvl2"
    node.vm.provider :libvirt do |domain|
      domain.management_network_mac = "52:54:00:4a:f1:ca"
    end
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/1",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.16.1",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.13.4",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/2",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.16.2",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.17.1",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/3",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.16.3",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.17.2",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g1/0",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.16.4",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.18.1",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g1/1",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.16.5",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.18.2",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g1/2",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.16.6",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.19.1",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g1/3",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.16.7",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.19.2",
      :libvirt__tunnel_port => "10001",
      auto_config: false
  end

  config.vm.define "sw3" do |node|
    node.vm.box = "cisco-iosvl2"
    node.vm.provider :libvirt do |domain|
      domain.management_network_mac = "52:54:00:38:33:22"
    end
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/1",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.17.1",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.16.2",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/2",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.17.2",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.16.3",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/3",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.17.3",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.18.3",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g1/0",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.17.4",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.18.4",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g1/1",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.17.5",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.19.5",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g1/2",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.17.6",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.19.6",
      :libvirt__tunnel_port => "10001",
      auto_config: false
  end

  config.vm.define "sw4" do |node|
    node.vm.box = "cisco-iosvl2"
    node.vm.provider :libvirt do |domain|
      domain.management_network_mac = "52:54:00:fa:15:25"
    end
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/1",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.18.1",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.16.4",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/2",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.18.2",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.16.5",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/3",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.18.3",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.17.3",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g1/0",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.18.4",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.17.4",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g1/1",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.18.5",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.19.3",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g1/2",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.18.6",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.19.4",
      :libvirt__tunnel_port => "10001",
      auto_config: false
  end

  config.vm.define "sw5" do |node|
    node.vm.box = "cisco-iosvl2"
    node.vm.provider :libvirt do |domain|
      domain.management_network_mac = "52:54:00:b8:bb:f1"
    end
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/1",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.19.1",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.16.6",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/2",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.19.2",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.16.7",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/3",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.19.3",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.18.5",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g1/0",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.19.4",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.18.6",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g1/1",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.19.5",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.17.5",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g1/2",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.19.6",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.17.6",
      :libvirt__tunnel_port => "10001",
      auto_config: false
  end

  config.vm.define "sw6" do |node|
    node.vm.box = "cisco-iosvl2"
    node.vm.provider :libvirt do |domain|
      domain.management_network_mac = "52:54:00:04:a4:eb"
    end
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/1",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.20.1",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.7.1",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/2",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.20.2",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.8.1",
      :libvirt__tunnel_port => "10001",
      auto_config: false
    node.vm.network :private_network,
      :libvirt__iface_name => "g0/3",
      :libvirt__tunnel_type => "udp",
      :libvirt__tunnel_local_ip => "127.1.20.3",
      :libvirt__tunnel_local_port => "10001",
      :libvirt__tunnel_ip => "127.1.9.1",
      :libvirt__tunnel_port => "10001",
      auto_config: false
  end
end
