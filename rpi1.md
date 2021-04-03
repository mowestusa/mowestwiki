<!--
category: Homelab
-->

# Secure RPi 1 Model B+

## Install RaspberryOS Lite

`lsblk -p`

The above command will give you a list of your disks and allow you to figure out how your Linux Computer is seeing the SD card.

I like to erase all partitions on the SD card, then create one FAT Partition using all of the free space. I find that this seems to reset a corrupted SD card that is not having secter failings.

`dd if=2021-01-11-raspios-buster-armhf.img of=/dev/sdX bs=4M conv=fsync`

The above command will copy the image onto the SD card as long as `/dev/???` matches the device name that was found with the command above.

## Enable SSH

Before removing the card mount the `boot` partition. This is probably most easily done by ejecting and reinserting the card into the SD slot.

Next `sudo touch ssh` to create a file called `ssh` in the boot partition.

## Logging into the RPi for the First Time

`ssh pi@raspberrypi.local`

On Linux the above should work.

Defaults

* user = pi
* password = raspberry

## Things to do when you first log into RPi

1. Change the pi user default password
2. Change the hostname to desired
3. Change the local to en_US UT8 and leave the default also selected en_GB UT8
4. Update RaspberryOS Lite
5. Turn on ssh interface

All of the above can be done through `sudo raspi-config`.

6. Update again with `sudo apt update && sudo apt upgrade`

It seems as if there are additional packages that get upgraded this way that were not upgraded through `raspi-config` tool.

7. `sudo reboot` to reboot the RPi so that it now responds to the new hostname

## Avoid Issues of boot hanging as it waits for External Drive

A second thing I found is the raspberry pi will boot much faster than an external hard drive can spin up. So the pi will hang at boot until the hard drive is ready or sometimes will not boot at all. This can be a big problem with the remote situation. So I found a set of options to use in the fs tab file that will tell the operating system to boot then Mount the drive when it's ready.

This is what I used:
Get the UUID of the partiton using the blkid command.

PARTUUID=<long uuid string>    /media/backup   ext4    auto,nofail,noatime,rw,user 0 0

## Advice on Connecting Remotely to a RPi on a different network

* RPi will need a static ip (best to set static ip on RPi and "reserved" ip on DHCP in router)
* Do not allow root to SSH
* No password authentication for SSH, force SSH key login only (you must exchange SSH keys before turning this option on or else I won't be able to log into the RPi)

## Great Documentation for Securing the RPi

* Remove default pi account and create a new account with a secure password
* Install fail2ban to ban remote attacks
* Enable the firewall on the pi, ufw, and only allow SSH connections on the RPi

This tutorial works well to address the above security practices.

`https://www.raspberrypi.org/documentation/configuration/security.md`


* Stay up on security patches by using "UnattendedUpgrades" for apt
* Use Dynamic DNS service that checks Public IP every 5 minutes
* Change the Port number for the SSH server (could be done in most routers by forwarding a certain port to the port 22 on the RPi)


