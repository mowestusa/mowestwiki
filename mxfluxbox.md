<!--
category: Linux Tips
-->

# MX Linux Fluxbox

## Bugs Found

### keys file issues

1. The key combo to take a screen capture fails to work on some computers.

`none Print :Exec /usr/bin/xfce4-screenshooter`

The above command in the `keys` file fails to execute screenshooter. It works on HPEnvy with MX-Fluxbox in Gnomeboxes, but not on the laptop where the "Fn" key needs to be engaged in order to get the "Prt Sc" key. The following provides a fix on the laptop that needs "Fn" command key to access "Prt Sc":

`none Insert :Exec /usr/bin/xfce4-screenshooter`

2. Shortcut for opening a terminal is not working because in a default install of MX Linux calling `xterm` fails because it is not installed. So change the following line from 'xterm' to following so that the default terminal will open using the keycombination:

`Mod1 F2 :Exec x-terminal-emulator`
    
## Check Out

*FBmenugen*
    
A "right click" menu generator for Fluxbox.

