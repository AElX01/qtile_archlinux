from libqtile import widget
from os import system
from .config_variables import script_variables
# create a json file to implement themes including font


def colors(bg, fg):
    return {
        "background" : bg,
        "foreground" : fg
    }

def active_interface():
    return 'enp2s0' if script_variables.get("ethernet_connection") == 0 else 'wlo1'

def network_icon():
    if script_variables.get("ethernet_connection") == 0:
        return " 󰈀 " 
    elif script_variables.get("wireless_connection") == 0:
        return " 󰘊 "
    else:
        return " 󰱶 "

def space():
    return widget.Spacer()

def icon(text, font, fontsize, padding, bg, fg):
    return widget.TextBox(
        text=text,
        font=font,
        fontsize=fontsize,
        padding=padding,
        **colors(bg, fg)
        )

def powerline(bg, fg):
    return widget.TextBox(
        text="󰍞",
        font="Hack Nerd Font",
        fontsize=80,
        padding=-16,
        **colors(bg, fg)
        )

def workspaces():
    return [widget.GroupBox(
    font="Hack Nerd Font",
    fontsize=15,
    margin_y=3,
    margin_x=3,
    padding_y=3,
    padding_x=10,
    borderwidth=4,
    active="#ffffff",
    inactive="#272727",
    rounded=False, 
    highlight_method="block",
    this_current_screen_border="#6e0097",
    this_screen_border="#ffffff",
    background="#000000"),
    ]


main_monitor_widgets = [
    icon("  ", "Hack Nerd Font", 17, 20, "#000000", "#1793d1"),

    *workspaces(),

    space(),

    powerline("#000000", "#ffd47e"),

    icon("󰮯", "Hack Nerd Font", 15, 10, "#ffd47e", "#212121"), 
    
    widget.CheckUpdates(
        background="#ffd47e",
        colour_have_updates="#ff3333",
        colour_no_updates="#212121",
        no_update_string='0   ',
        display_format='{updates}',
        update_interval=1,
        custom_command='checkupdates',
    ),

    powerline("#ffd47e", "#ff7e7e"),
    
    #icon(network_icon(), "Hack Nerd Font", 15, 10, "#ff7e7e", "#212121"),

    widget.Net(interface=active_interface(), update_interval=1, **colors("#ff7e7e", "#212121"), format=f'{network_icon()}  ' + '{interface}: {down:6.2f}{down_suffix:<2}↓↑{up:6.2f}{up_suffix:<2}'),

    powerline("#ff7e7e", "#8c7eff"),
    
    icon("󰌓", "Hack Nerd Font", 15, 10, "#8c7eff", "#212121"),

    widget.KeyboardLayout(**colors("#8c7eff", "#212121"), configured_keyboards = ['us', 'latam']),

    powerline("#8c7eff", "#c07eff"),

    widget.BatteryIcon(**colors("#c07eff", "#212121"), theme_path='/usr/share/icons/WhiteSur-dark/status/16', scale=1.8, update_interval=1),

    widget.Battery(
        **colors("#c07eff", "#212121"),
        format='{char} {percent:2.0%}',
        update_interval=1,
        discharge_char=' ',
        charge_char=' ',
        full_char='',
        show_short_text=False
        ),

    powerline("#c07eff", "#7eb5ff"),

    icon("󰕾", "Hack Nerd Font", 15, 10, "#7eb5ff", "#212121"),

    widget.PulseVolume(**colors("#7eb5ff", "#212121")),

    powerline("#7eb5ff", "#595959"),

    icon("󰥔", "Hack Nerd Font", 15, 10, "#595959", "#d8d2d2"),

    widget.Clock(**colors("#595959", "#d8d2d2"), format='%d/%m/%y %H:%M'),

    powerline("#595959", "#000000")
]

secondary_monitor_widgets = [ 
    *main_monitor_widgets,

    widget.Systray()
]
