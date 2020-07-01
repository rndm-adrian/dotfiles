#!/bin/sh
alias config='/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME' &
echo ".cfg" >> .gitignore &
mkdir ~/conf_backup &
mv ~/.zshrc ~/conf_backup  -r &
mv ~/.bashrc ~/conf_backup -r &
mv ~/.config ~/conf_backup -r &
mv ~/.vimrc ~/conf_backup -r &
/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME config --local status.showUntrackedFiles no &
/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME checkout

