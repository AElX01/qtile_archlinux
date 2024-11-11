from libqtile.lazy import lazy
from libqtile.config import Key 
from .config_variables import script_variables
from libqtile import qtile


keys = [
    # Switch between windows
    Key([script_variables.get("mod")], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([script_variables.get("mod")], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([script_variables.get("mod")], "j", lazy.layout.down(), desc="Move focus down"),
    Key([script_variables.get("mod")], "k", lazy.layout.up(), desc="Move focus up"),
    Key([script_variables.get("mod")], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Window movements
    Key([script_variables.get("mod"), "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([script_variables.get("mod"), "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([script_variables.get("mod"), "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([script_variables.get("mod"), "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Window size
    Key([script_variables.get("mod"), "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([script_variables.get("mod"), "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([script_variables.get("mod"), "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([script_variables.get("mod"), "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([script_variables.get("mod")], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    Key(
        [script_variables.get("mod"), "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),

    # Toggle between different layouts as defined below
    Key([script_variables.get("mod")], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([script_variables.get("mod")], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [script_variables.get("mod")],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),

    Key([script_variables.get("mod")], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([script_variables.get("mod"), "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([script_variables.get("mod"), "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([script_variables.get("mod")], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # Launch installed programs
    Key([script_variables.get("mod")], "Return", lazy.spawn(script_variables.get("terminal")), desc="Launch terminal"),
    Key([script_variables.get("mod"), "shift"], "f", lazy.spawn(script_variables.get("browser")), desc="Launch browser"),
    Key([script_variables.get("mod"), "shift"], "r", lazy.spawn(script_variables.get("app_launcher_mode")), desc="Launch app launcher"),
    Key([script_variables.get("mod"), "shift"], "p", lazy.spawn("spotify-launcher"), desc="Launch spotify"),
    Key([script_variables.get("mod"), "shift"], "m", lazy.spawn("prime-run minecraft-launcher"), desc="Launch minecraft"),
    Key([script_variables.get("mod"), "shift"], "s", lazy.spawn(script_variables.get("code_editor")), desc="Launch IDE"),
    
    # Volume keys
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),

    # Brightness keys
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

    # Take screenshots
    Key([], "Print", lazy.spawn("bash -c \"maim -s -o | xclip -selection clipboard -t image/png -i\""))]

# Add key bindings to switch VTs in Wayland.
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )
