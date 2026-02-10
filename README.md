![Vagrant](https://img.shields.io/badge/vagrant%20-%231563FF.svg?&style=for-the-badge&logo=vagrant&logoColor=white)

This project constructs a lab environment for INE's [CCIE Enterprise Infrastructure v1 Exam Review](https://my.ine.com/Networking/courses/02d0607e/ccie-enterprise-infrastructure-v1-exam-review) course.

![CCIE Enterprise Infrastructure v1 topology](network-diagram.svg)

## Prerequisites

- [Install and configure a lab server with Arch Linux](https://marcstech.blog/archives/install-configure-lab-server-arch-linux/)
- [Cisco IOSv Vagrant box](https://github.com/mweisel/cisco-iosv-vagrant-libvirt)
- [Cisco IOSvL2 Vagrant box](https://github.com/mweisel/cisco-iosvl2-vagrant-libvirt)

## Steps

1\. Clone this GitHub repo and _cd_ into the directory.

```
git clone https://github.com/mweisel/ine-ccie-ei-v1-exam-review-lab-companion.git && cd ine-ccie-ei-v1-exam-review-lab-companion
```

2\. Instantiate the Cisco devices.

```
vagrant up
```

3\. Verify the devices are in the `running` state.

```
vagrant status
```

output:

```
Current machine states:

r1                        running (libvirt)
r2                        running (libvirt)
r3                        running (libvirt)
r4                        running (libvirt)
r5                        running (libvirt)
r6                        running (libvirt)
r7                        running (libvirt)
r8                        running (libvirt)
r9                        running (libvirt)
r10                       running (libvirt)
r11                       running (libvirt)
r12                       running (libvirt)
r13                       running (libvirt)
r14                       running (libvirt)
sw1                       running (libvirt)
sw2                       running (libvirt)
sw3                       running (libvirt)
sw4                       running (libvirt)
sw5                       running (libvirt)
sw6                       running (libvirt)

This environment represents multiple VMs. The VMs are all listed
above with their current state. For more information about a specific
VM, run `vagrant status NAME`.
```

4\. Create a Python virtual environment for the project.

```
uv sync
```

5\. Run the Python script to set a baseline configuration for the INE labs.

```
uv run set_lab_config.py
```

6\. Connect to the `r1` device.

```
vagrant ssh r1
```

7\. Verify Link Layer Discovery Protocol (LLDP) neighborship.

```
show lldp neighbors
```

output:

```
Capability codes:
    (R) Router, (B) Bridge, (T) Telephone, (C) DOCSIS Cable Device
    (W) WLAN Access Point, (P) Repeater, (S) Station, (O) Other

Device ID           Local Intf     Hold-time  Capability      Port ID
r4.example.com      Gi0/3          120        R               Gi0/1
r5.example.com      Gi0/4          120        R               Gi0/1
r2.example.com      Gi0/1          120        R               Gi0/1
r3.example.com      Gi0/2          120        R               Gi0/1

Total entries displayed: 4
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
