from libqtile.config import Group, Match, Key
from libqtile.lazy import lazy
from .key_bidings import keys
from .config_variables import script_variables




groups = [ 
        Group("1", label="1"),
        Group("2", label="2"),
        Group("3", label="3", matches=[Match(wm_class="firefox")]), 
        Group("4", label="4"),
        Group("5", label="5", matches=[Match(wm_class="virt-manager")]),
        Group("6", label="6", matches=[Match(wm_class="lxterminal")]),
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
