# Add the following to ~/.zshrc file for pyenv tags in terminal

if command -v pyenv 1>/dev/nukk 2>&1; then
    eval "$(pyenv init -)"
fi
export PATH=/usr/local/bin:$PATH
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"