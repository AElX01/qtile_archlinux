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
        text="",
        font="Hack Nerd Font",
        fontsize=80,
        padding=-16,
        **colors(bg, fg)
        )

def workspaces():
    return [widget.GroupBox(
    font="SourceCodePro",
    fontsize=15,
    margin_y=3,
    margin_x=3,
    padding_y=3,
    padding_x=10,
    borderwidth=4,
    active="#ffffff",
    inactive="#272727",
    rounded=False, 
    highlight_method="line",
    this_screen_border="#ffffff",
    this_current_screen_border="#ffffff",
    background="#000000"),
    ]


main_monitor_widgets = [
    icon(" ", "SourceCodePro", 17, 20, "#000000", "#2e2e2e"),

    powerline("#000000", "#000000"),
    
    icon("", "Hack Nerd Font", 15, 10, "#000000", "#2e2e2e"),

    widget.KeyboardLayout(**colors("#000000", "#b0b0b0"), configured_keyboards = ['us', 'latam'], font='SourceCodePro'),

    powerline("#000000", "#000000"),

    widget.LaunchBar(),

    space(),

    *workspaces(),

    space(),

    powerline("#000000", "#000000"),

    icon("󰮯", "Hack Nerd Font", 15, 10, "#000000", "#2e2e2e"), 
    
    widget.CheckUpdates(
        font='SourceCodePro',
        background="#000000",
        colour_have_updates="#ffffff",
        colour_no_updates="#2e2e2e",
        no_update_string='0   ',
        display_format='{updates}',
        update_interval=1,
        custom_command='checkupdates',
    ),

    powerline("#000000", "#000000"),
    
    #icon(network_icon(), "Hack Nerd Font", 15, 10, "#ff7e7e", "#212121"),

    # widget.Net(interface=active_interface(), update_interval=1, **colors("#000000", "#464646"), format=f'' + '{interface}: {down:6.2f}{down_suffix:<2}↓↑{up:6.2f}{up_suffix:<2}'),

    widget.BatteryIcon(**colors("#000000", "#2e2e2e"), scale=1.8, update_interval=1, theme_path='/home/hax00r/Downloads/repos/WhiteSur-light/status/16'), 
    
    widget.Battery(
        font='SourceCodePro',
        **colors("#000000", "#2e2e2e"),
        format='{char} {percent:2.0%}',
        update_interval=1,
        discharge_char=' ',
        charge_char=' ',
        full_char='',
        show_short_text=False
        ),
    

    powerline("#000000", "#000000"),

    icon("󰕾", "Hack Nerd Font", 15, 10, "#000000", "#2e2e2e"),

    widget.PulseVolume(**colors("#000000", "#2e2e2e"), font='SourceCodePro'),

    powerline("#000000", "#000000"),

    icon("", "Hack Nerd Font", 15, 10, "#000000", "#2e2e2e"),

    widget.Clock(**colors("#000000", "#2e2e2e"), format='%H:%M', font='SourceCodePro'),

    powerline("#000000", "#000000"),
]

secondary_monitor_widgets = [ 
    *main_monitor_widgets,

    widget.Systray()
]
