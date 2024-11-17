# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.

neofetch

if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# Created by newuser for 5.9
source ~/powerlevel10k/powerlevel10k.zsh-theme

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

# plugins
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh 
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /usr/share/zsh/plugins/zsh-sudo/sudo.plugin.zsh

# path
export PATH="$PATH:/opt/nvim-linux64/bin"

# necessary line to avoid error messages during neofetch's execution
typeset -g POWERLEVEL9K_INSTANT_PROMPT=quiet

# connect to wifi 
wifi_connect()
{
  nmcli device wifi connect ${1} password ${2}
}

# list active connections
wifi_list()
{
  nmcli c show --active | grep wifi | awk '{print $1}'
}

# alias
alias cat=bat
alias list="nmcli device wifi list"
