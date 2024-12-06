from libqtile.config import Drag, Click
from libqtile.lazy import lazy
from .config_variables import script_variables


mouse = [
    Drag(
        [script_variables.get("mod")],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position()
        ),
    
    Drag(
        [script_variables.get("mod")],
        "Button3", lazy.window.set_size_floating(),
        start=lazy.window.get_size()
        ),

    Click(
        [script_variables.get("mod")],
        "Button2",
        lazy.window.bring_to_front()
        ),
]