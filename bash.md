<!--
category: Tools
-->

# Bash

## bashrc helps

### User specific aliases and functions

```
alias vim="vimx"
alias note="vimx /home/mowest/Documents/per-projects/scratchpad.txt"
alias bashrc="vimx /home/mowest/.bashrc"
alias vimrc="vimx /home/mowest/.vimrc"
alias weather="curl wttr.in/South_Haven"
alias lt='ls --human-readable --size -1 -S --classify'
alias upup='sudo dnf update -y'
alias mnt="mount | awk -F' ' '{ printf \"%s\t%s\n\",\$1,\$3; }' | column -t | egrep ^/dev/ | sort"
alias gh='history|grep'
alias left='ls -t -1'
alias trash='mv --force -t ~/.local/share/Trash '
alias open='xdg-open'
```

### Alias Function to change folders and list contents

```
function cl() {
     DIR="$*";
         # if no DIR given, go home
         if [ $# -lt 1 ]; then
              DIR=$HOME;
        fi;
        builtin cd "${DIR}" && \
        # use your preferred ls command
            ls -F --color=auto
}
```

### Recommendations from rwaltr

#### Shell Options
`shopt -s autocd` change to named directory
`shopt -s cdspell` autocorrects cd misspellings
`shopt -s cmdhist` save multi-line commands in history as single line
`shopt -s dotglob`
`shopt -s histappend` do not overwrite history
`shopt -s expand_aliases` expand aliases
`shopt -s checkwinsize` checks term size when bash regains control
`bind "set completion-ignore-case on"`

#### Custom Alias

* easy resource
`alias resource="source ~/.bashrc"`

* Easy Open
`alias open="xdg-open"`

* IP colors
`alias ip='ip -br -c'`

`alias tb='nc termbin.com 9999'`
`alias termbin=tb`

### Link for additional .bashrc ideas

https://github.com/terminalforlife/BashConfig/blob/master/source/.bash_functions


## bash scripting best practices

* Variables are best in UPPERCASE
* Variables can be called in the following ways

```
$NAME
${NAME}
```

## bash specify the interpreter

`#!/bin/bash`

The above is the most common way to call `bash` as the interpreter. It can also be called with:

`#!/usr/bin/env bash`

The difference between the two methods is found here: https://stackoverflow.com/questions/16365130/what-is-the-difference-between-usr-bin-env-bash-and-usr-bin-bash/16365367#16365367

Additionally, if you create a new file, and put the `shebang` in the first line of the file, then in vim you can simply run the command `:e` and it will reload the current file that you are editing and the syntax highlighting for `bash` will kick in.


