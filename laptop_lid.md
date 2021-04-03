<!--
category: Homelab
-->

# Laptop Lids

## Problem 

Using a laptop as a server creates an issue if you want to close the lid but keep the computer running and "serving." There is a way to fix this with systemd setting in Debian 10.

## Solution

1. Open the file `/etc/systemd/logind.conf` as root

2. Find the following settings and switch to what is below and then uncomment by removing the `#`

```
HandleLidSwitch=ignore
HandleLidSwitchExternalPower=ignore
HandleLidSwitchDocked=ignore
LidSwitchIgnoreInhibited=no
```

3. Finally, restart the service with the command below:

`sudo service systemd-logind restart`

