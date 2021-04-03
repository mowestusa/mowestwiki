<!--
category: Linux Tips
-->

# General Tips

## Remote Desktop Options

* XtoGo - opensource, need to forward ports, static ip...
* Simple Help - not opensource, pay one time and own it forever, host self
* Teamviewer - not opensource, not feature full, and client is always running

## Git Training

* Start here 12 days of Git: https://dev.to/sushicodes
* Ben Cotton: https://fedoraproject.org/wiki/User:Bcotton/git-for-docs-writers


## Open File in Default GUI from CLI

`xdg-open {file}`


## Quick Conversion of Markdown into PDF

```bash
pandoc example.md -o example.pdf --from=markdown -V geometry:margin=.5in -V fontsize=12pt
```

## What to install for Pandoc to convert into PDF - Debian

```bash
sudo apt install pandoc texlive-latex-recommended lmodern texlive-latex-extra texlive-fonts-recommended
```

## Weather in the Terminal

```bash
inxi -w
```

OR

```bash
curl http://wttr.in/South_Haven
```

## How to eliminate showing "snap" packages in your df

```bash
alias df='df -x squashfs'
```

## Linux Tweaks mentioned on Linux Unplugged

* profile-sync-daemon — Symlinks and syncs browser profile dirs to RAM thus reducing HDD/SDD calls and speeding-up browsers.

https://github.com/graysky2/profile-sync-daemon

* junegunn/fzf — A command-line fuzzy finder

https://github.com/junegunn/fzf

* cxreg/smartcd — Alter your bash (or zsh) environment as you cd.

https://github.com/cxreg/smartcd

* wting/autojump — A cd command that learns - easily navigate directories from the command line.

https://github.com/wting/autojump

* gsamokovarov/jump — Jump helps you navigate faster by learning your habits.

https://github.com/gsamokovarov/jump

* muammar/mkchromecast — Cast macOS and Linux Audio/Video to your Google Cast and Sonos Devices

https://github.com/muammar/mkchromecast

* xat/castnow — commandline chromecast player

https://github.com/xat/castnow

* xat/dlnacast — Cast local media to your TV through UPnP/DLNA

https://github.com/xat/dlnacast

* skorokithakis/catt — Cast All The Things allows you to send videos from many, many online sources to your Chromecast.

https://github.com/skorokithakis/catt

* tridactyl — A Vim-like interface for Firefox, inspired by Vimperator/Pentadactyl

https://github.com/tridactyl/tridactyl

* Vimium-FF seemed like a better option than the one above, far more users.

* Firefox Adwaita Theme — This is a bunch of CSS code to make Firefox look closer to GNOME's native apps.

https://github.com/rafaelmardojai/firefox-gnome-theme

* Use your ~/.local folder!

https://askubuntu.com/a/14536

