from os import system

script_variables = dict(
    mod = "mod4",
    run_startup_programs = "/home/hax00r/.config/qtile/./autostart.sh",
    terminal = "kitty",
    browser = "firefox",
    app_launcher_mode = "rofi -show drun",
    code_editor = "code",
    wireless_interface = system("ifconfig | grep '^w' | awk -F ':' '{print $1}'"),
    ethernet_interface = system("ifconfig | grep -E '^e|^b' | awk -F ':' '{print $1}'"),
    ethernet_connection = system("ifconfig $(ifconfig | grep '^e' | awk -F ':' '{print $1}') | grep inet"),
    wireless_connection = system("ifconfig $(ifconfig | grep '^w' | awk -F ':' '{print $1}') | grep inet"),
    wallpaper_path = "/home/hax00r/Pictures/wallpapers/geology.png"
)


