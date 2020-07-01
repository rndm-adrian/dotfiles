call plug#begin('~/.vim/plugged')

Plug 'arcticicestudio/nord-vim'

Plug 'itchyny/lightline.vim'

call plug#end()

colorscheme nord

set laststatus=2

let g:lightline = {
      \ 'colorscheme': 'wombat',
      \ 'active': {
      \   'left': [ [ 'mode', 'paste' ],
      \             [ 'gitbranch', 'readonly', 'filename', 'modified' ] ]
      \ },
      \ 'component_function': {
      \   'gitbranch': 'FugitiveHead'
      \ },
      \ }

set number relativenumber
