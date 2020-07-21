#!/bin/sh
/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME clone https://github.com/rndm-adrian/dotfiles ~/.cfg &
alias config='/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME' &
echo ".cfg" >> .gitignore &
mkdir ~/conf_backup &
mv ~/.zshrc ~/conf_backup &
mv ~/.bashrc ~/conf_backup &
mv ~/.config ~/conf_backup &
mv ~/.vimrc ~/conf_backup &
/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME config --local status.showUntrackedFiles no &
/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME checkout &

