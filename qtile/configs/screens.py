from libqtile.config import Screen
from libqtile import bar, widget
from screeninfo import get_monitors
from .widgets import main_monitor_widgets, secondary_monitor_widgets 
from .config_variables import script_variables


def status_bar(bar_widgets):
    return bar.Bar(
        background="#000000",
        margin=[5, 5, 1, 5],
        size=30,
        opacity=0.8,
        widgets=bar_widgets
    )


# multimonitor support
screens = [Screen(top=status_bar(main_monitor_widgets), wallpaper=script_variables.get("wallpaper_path"), wallpaper_mode='fill')]


if len(get_monitors()) >= 2:
    screens.append(Screen(top=status_bar(secondary_monitor_widgets), wallpaper=script_variables.get("wallpaper_path"), wallpaper_mode='fill'))