<!--
category: Tools
-->

# Vim

## Must Have Options for **.vimrc**

* `set autowrite`: Saves a buffer automatically whenever you leave it

## Clipboard

Must have clipboard feature in order for this to work
To solve this in debian you install the `vim-gtk` package.

Add `set clipboard=unnamedplus` to vimrc

Now you just use vim normally just yank and paste work with system clipboard(not the PRIMARY one but the CLIPBOARD)

[Post where idea is explained](http:vi.stackexchange.com/questions/84/how-can-i-copy-text-to-the-system-clipboard-from-vim)

## Word Count (Built In Command)

`g, CTRL-g`

## Word Count in Lightline

Install lightline plugin using vim-plug

`Plug 'itchyny/lightline.vim'`

Create a function to display the word count

```bash
fun! WordCount()
	if index(g:user_lightline_filetypes_show_wordcount, &ft) < 0
		return ''
	endif
	let result = wordcount()
	if result->has_key('visual_words')
		return result.visual_words . ' words'
	endif
	return result.words . ' words'
endfun
```

Add it to the lightline bar

```bash
let g:lightline = {}
let g:lightline.component_function = {
    'wordcount' : 'WordCount'
}
let g:lightline.active = { 'left' : [ ['mode'], ['readonly', 'filename', 'modified'], ['wordcount'] ] }
```

Define a list of filetypes that you want the word count to appear in

`let g:user_lightline_filetypes_show_wordcount = ['markdown', 'asciidoc']`

## Plugin Management

* vim-plug

Download and install with: 

`curl -fLo ~/.vim/autoload/plug.vim --create-dirs 'https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'`


Put into `.vimrc`

```
set nocompatible
filetype off

call plug#begin('~/.vim/plugged')

Plug 'TheNiteCoder/asciidoc.vim'
Plug 'neoclide/coc.nvim', { 'branch' : 'release' }

call plug#end()
```

Use command to update:

`:PlugUpdate`

Use command to install new plugins:

`:PlugInstall`

Use command to clean or remove plugins:

`:PlugClean`

## Word Count

`g, CTRL-g`

## Possible Plugins to Consider

* lightline.vim
* vifm.vim
* vim-css-color.vim

## Add System Clipboard to VIM on Fedora

1. `sudo dnf install vim-X11`
2. Add the line below to .vimrc
`set clipboard=unnamedplus`
3. Add `alias vim="vimx"` to .bashrc
4. Now y and p work with the system clipboard.

## Add System Clipboard to VIM on Debian

1. `sudo apt install vim-gtk or vim-gtk3`
2. Add the line below to .vimrc
`set clipboard=unnamedplus`
3. Add `alias vim="vim.gtk or vim.gtk3"` to .bashrc
4. Now y and p work with the system clipboard.

## Spell Checking in VIM

Start spell checking the current file in the buffer.

`:setlocal spell`

#####  **]s**  jump forward to misspelled word

#####  **[s**  jump backward to misspelled word

#####  **z=**  give list of correction suggestions

#####  **zg**  add good word to spellfile

#####  **zw**  add wrong word to spellfile

#####  **zug** undo good word in spellfile

#####  **zuw** undo wrong word in spellfile

## Turn Off Search Highlighting Until the Next Search

`:noh`

## Open website URL under text cursor in VIM

`gx`

