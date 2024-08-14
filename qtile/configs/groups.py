from libqtile.config import Group, Match, Key
from libqtile.lazy import lazy
from .key_bidings import keys
from .config_variables import script_variables




groups = [ 
        Group("1", label="󰌢"),
        Group("2", label="󰁌"),
        Group("3", label="󰈹", matches=[Match(wm_class="firefox")]), 
        Group("4", label="", matches=[Match(wm_class="code"), Match(wm_class="sublime_text"), Match(wm_class="jetbrains-idea-ce")]),
        Group("5", label="󰍳", matches=[Match(wm_class="Minecraft Launcher")]),
        Group("6", label="󰓇", matches=[Match(wm_class="spotify")]),
        Group("7", label="", matches=[Match(wm_class="virt-manager")]),
        ]


for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [script_variables.get("mod")],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [script_variables.get("mod"), "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )
