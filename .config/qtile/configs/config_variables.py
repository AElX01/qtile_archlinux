from os import system

script_variables = dict(
    mod = "mod4",
    run_startup_programs = "/home/hazor/.config/qtile/./autostart.sh",
    terminal = "kitty",
    browser = "firefox",
    app_launcher_mode = "rofi -show drun",
    code_editor = "sublime_text",
    wireless_interface = system("ifconfig | grep '^w' | awk -F ':' '{print $1}'"),
    ethernet_interface = system("ifconfig | grep '^e' | awk -F ':' '{print $1}'"),
    ethernet_connection = system("ifconfig $(ifconfig | grep '^e' | awk -F ':' '{print $1}') | grep inet"),
    wireless_connection = system("ifconfig $(ifconfig | grep '^w' | awk -F ':' '{print $1}') | grep inet"),
    wallpaper_path = "../arch.png" # JUST, CHANGE THIS LINE ;)
)
