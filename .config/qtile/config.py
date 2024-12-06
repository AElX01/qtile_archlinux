# AElX01 Qtile config

from libqtile import hook
from configs.config_variables import script_variables
from configs.key_bidings import keys
from configs.groups import groups
from configs.layouts import layouts, floating_layout
from configs.widgets import main_monitor_widgets, secondary_monitor_widgets
from configs.screens import screens
from configs.mouse import mouse
from os import system


@hook.subscribe.startup_once
def autostart():
    system(script_variables.get("run_startup_programs"))


dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

wl_input_rules = None

wl_xcursor_theme = None
wl_xcursor_size = 24

wmname = "LG3D"