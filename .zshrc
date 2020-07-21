source ~/antigen.zsh

# Load the oh-my-zsh's library.
antigen use oh-my-zsh

# Bundles from the default repo (robbyrussell's oh-my-zsh).
antigen bundle git
antigen bundle heroku
antigen bundle pip
antigen bundle lein
antigen bundle command-not-found
antigen bundle zsh-users/zsh-autosuggestions

# Syntax highlighting bundle.
antigen bundle zsh-users/zsh-syntax-highlighting

# Load the theme.
antigen theme agnoster

# # Tell Antigen that you're done.
antigen apply

alias i="sudo pacman -S"
alias u="sudo pacman -Syyu"
alias rpkg="sudo pacman -R --recursive"


# Im using the Colorscript collection of DistroTube: https://gitlab.com/dwt1/shell-color-scripts
colorscript -r

# alias c='/usr/bin/git --git-dir=$HOME/dotfiles/ --work-tree=$HOME'

eval $(dircolors ~/.dir_colors)


alias c='/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME'
alias vim="/bin/nvim"
export PATH="$PATH:$HOME/.bin"
