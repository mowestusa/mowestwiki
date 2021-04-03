<!--
category: Linux Tips
-->

# Fedora

It would be a good idea to turn these into a bash script one day.

## Add System Clipboard to VIM on Fedora

1. `sudo dnf install vim-X11`
2. Add the line below to .vimrc
`set clipboard=unnamedplus`
3. Add `alias vim="vimx"` to `.bashrc`
4. Now y and p work with the system clipboard.

## Add RPMFusion Repos for Non-Free Software

1. Add repos

```
sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm

sudo dnf install https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

2. Add RPMFusion AppStream Data

```bash
sudo dnf groupupdate core
```

3. Add the following non-free software for multimedia

```bash
sudo dnf install gstreamer1-plugins-{bad-\*,good-\*,base} gstreamer1-plugin-openh264 gstreamer1-libav --exclude=gstreamer1-plugins-bad-free-devel
sudo dnf install lame\* --exclude=lame-devel
sudo dnf group upgrade --with-optional Multimedia
sudo dnf install mpv
```

## Install Regularly Used Packages

```bash
sudo dnf install gnome-extensions-app
```

## Gnome Terminal Tweaks

```bash
bash -c  "$(wget -qO- https://git.io/vQgMr)"
```

The above command launches a Profile installer to set terminal color schemes. My current preferred is "Night Owl". With "Night Owl" for the Gnome terminal color scheme, I like using VIM's colorscheme "night".

## Additional Packages I Need

* Kmymoney
* AisleRiot Solitare
* JetBrains Mono Font
* Gnome Tweaks
* KeepassXC

