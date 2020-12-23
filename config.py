from libqtile.config import Key, Group, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget , hook, widget
from os import path
import subprocess
from settings.scripts import cpu_percent
from settings.keys import *

group_labels = [
    "🏠", "🌎", "",
    "", "", "📷",
    "📺", "🎮", "",
    "🌑",
]

group_names = [
    "1", "2", "3",
    "4", "5", "6",
    "7", "8", "9",
    "0",
]

group_exclusives = [
    False, False, False,
    False, False, False,
    False, False, False,
    False,
]
group_persists = [
    True, True, True,
    True, True, True,
    True, True, True,
    True,
]
group_inits = [
    True, True, True,
    True, True, True,
    True, True, True,
    True,
]

group_layouts = [
    "tile", "max", "monadwide",
    "monadtall", "stack", "zoomy",
    "max", "max", "columns",
    "bsp",
]


layout_style = {
        'font': 'Monospace',
        'margin': 8,
        'border_width': 1,
        'border_normal': '#888888',
        'border_focus' : '#ffaf12'
}


layouts = [
        layout.Max(),
        layout.Stack(stacks=2),
        layout.xmonad.MonadTall(**layout_style),
        layout.Tile(**layout_style),
        layout.RatioTile(**layout_style),
        layout.bsp.Bsp(**layout_style),
        ]

groups = []

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            exclusive=group_exclusives[i],
            layout=group_layouts[i].lower(),
            persist=group_persists[i],
            init=group_inits[i],
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])



screens = [
    Screen(
        top=bar.Bar([
             
            widget.GroupBox(
                active='F6F6F6', 
                inactive='968F92',
                this_current_screen_border='00BCD4',
                this_screen_border='00BCD4',
                highlight_method='line',
                highlight_color=['1A2024', '060A0F'],
                fontsize=14,
                font="UbuntuMono Nerd Font"
            ),
            widget.WindowName(
                fontsize=17,
                font="UbuntuMono Nerd Font"
                           
            ),
             widget.TextBox(
                text="",
                padding=-1,
                fontsize=45,
                #background="#b83dff",
                foreground="#954fbd"

            ),
            widget.Memory(
                
                font="UbuntuMono Nerd Font",
                fontsize=15,
                padding=2,
                background="#954fbd",
                interval=0.5
                
                ),



            widget.TextBox(
                text="",
                padding=-1,
                fontsize=45,
                foreground="#b83dff",
                background="#954fbd",

            ),

            widget.Net(
                interface='wlp0s20f0u1',
                interval=0.3,
                fontsize=15,
                background="#b83dff",
                font="UbuntuMono Nerd Font"


            ),
            widget.TextBox(
                text="",
                padding=-1,
                fontsize=45,
                background="#b83dff",
                foreground="#954fbd"

            ),
            widget.CurrentLayout(
                
                fontsize=15,
                padding=2,
                background="#954fbd",
                font="UbuntuMono Nerd Font"
    
                
                ),
            widget.TextBox(
                text="",
                padding=-1,
                fontsize=45,
                foreground="#b83dff",
                background="#954fbd"

            ),
            widget.Clock(
                **{
                    'format':'%H:%M:%S',
                    #update_interval':1.0,
                    
                    },
                padding=3,
                fontsize=15,
                linewidth=2,
                background="#b83dff",
                font="UbuntuMono Nerd Font"

                ),
             widget.Volume(update_interval=0.2, emoji=True),
            ], 23,)
        ),
  
]


#autostart apps
@hook.subscribe.startup_once
def autostart():
    start = path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([start])

autostart()
