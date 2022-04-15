![CCIE Enterprise Infrastructure v1 topology](network-diagram.svg)

This project constructs a lab environment for INE's [CCIE Enterprise Infrastructure v1 Exam Review](https://my.ine.com/Networking/courses/02d0607e/ccie-enterprise-infrastructure-v1-exam-review) course.

## Ingredients

  * [Vagrant](https://www.vagrantup.com)
  * [QEMU](https://www.qemu.org)/[KVM](https://www.linux-kvm.org)
  * [libvirt](https://libvirt.org)
  * [vagrant-libvirt](https://github.com/vagrant-libvirt/vagrant-libvirt) >= 0.8.0
  * [Cisco IOSv Vagrant box](https://github.com/mweisel/cisco-iosv-vagrant-libvirt)
  * [Cisco IOSvL2 Vagrant box](https://github.com/mweisel/cisco-iosvl2-vagrant-libvirt)
  * [Python](https://www.python.org) >= 3.7
  * [Nornir](https://github.com/nornir-automation/nornir)
  * [Scrapli](https://github.com/carlmontanari/scrapli)

## Prerequisites

A\. Add the Cisco IOSv and IOSvL2 Vagrant boxes.

<pre>
$ <b>vagrant box list | grep iosv</b>
cisco-iosv        (libvirt, 15.9)
cisco-iosvl2      (libvirt, 2020)
</pre>

B\. Create a DHCP reservation entry for the management interface of each Cisco device.

Refer to [Controlling Vagrant Box Management IP](https://codingpackets.com/blog/controlling-vagrant-box-management-ip) for more information. Use [vagrant-libvirt-vnet.xml](files/vagrant-libvirt-vnet.xml) as a reference.

C\. Create/Update the SSH client configuration file for the Cisco devices.

Use [sshconfig](files/sshconfig) as a reference.

## Steps

1\. Clone this GitHub repo and _cd_ into the directory.

<pre>
$ <b>git clone https://github.com/mweisel/ine-ccie-ei-v1-exam-review-lab-companion.git</b>
$ <b>cd ine-ccie-ei-v1-exam-review-lab-companion</b>
</pre>

2\. Create a Python virtual environment.

<pre>
$ <b>python3 -m venv .venv</b>
</pre>

3\. _Activate_ the Python virtual environment.

<pre>
$ <b>source .venv/bin/activate</b>
</pre>

4\. Update the `pip` and `setuptools` Python packages.

<pre>
$ <b>pip install -U pip setuptools</b>
</pre>

5\. _Reactivate_ the Python virtual environment.

<pre>
$ <b>deactivate && source .venv/bin/activate</b>
</pre>

6\. Install the Nornir and Scrapli Python packages.

<pre>
$ <b>pip install -r requirements.txt</b>
</pre>

7\. _Reactivate_ the Python virtual environment.

<pre>
$ <b>deactivate && source .venv/bin/activate</b>
</pre>

8\. Instantiate the Cisco devices.

<pre>
$ <b>vagrant up</b>
</pre>

9\. Run the Python script to configure the Cisco devices for the INE labs.

<pre>
$ <b>python init.py</b>
</pre>

10\. Connect to the Cisco devices via SSH.

<pre>
$ <b>ssh r7</b>
$ <b>ssh sw2</b>
</pre>

<a href="https://asciinema.org/a/440193?speed=2" target="_blank"><img src="https://asciinema.org/a/440193.svg" /></a>

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
