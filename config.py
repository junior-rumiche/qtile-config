from libqtile.config import Key, Group, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget , hook, widget
from os import path
import subprocess

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



mod = "mod4"
mod1 = "shift"
mod2 = "control"
auto_fullscreen = False

keys = [
        Key([mod, mod1], 'r', lazy.restart() ), #restar config
        Key([mod, mod1], 'q', lazy.window.kill()), # kill window
        Key([mod], 'Return', lazy.spawn("termite")), #openf termianl
        Key([mod, mod1], "a", lazy.shutdown()), #cerrar session
        Key([mod], 'i', lazy.spawn(' /usr/bin/rofi -show run')), #rofi menu
        Key([mod], 'l', lazy.next_layout()),
        Key([mod], 'd', lazy.spawn('dmenu_run')),

        #Change Focus
        Key([mod], 'h', lazy.layout.up()),
        Key([mod], 'k', lazy.layout.down()),
        Key([mod], 'j', lazy.layout.next()),

        #moved focused windows
        Key([mod, mod1], 'k', lazy.layout.shuffle_up()),
        Key([mod, mod1], 'j', lazy.layout.shuffle_down()),

        Key([],'Print', lazy.spawn("scrot ~/Imágenes/ScreenShot_%H%M%S.png ")),

]
# screen

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
            ),
            widget.WindowName(
                fontsize=14,
                           
            ),


            widget.TextBox(
                text="",
                padding=-1,
                fontsize=45,
                foreground="#b83dff",
                #background="#954fbd"

            ),

            widget.Net(
                interface='wlp0s20f0u1',
                interval=0.8,
                fontsize=13,
                background="#b83dff"


            ),
            widget.TextBox(
                text="",
                padding=-1,
                fontsize=45,
                background="#b83dff",
                foreground="#954fbd"

            ),
            widget.CurrentLayout(
                
                fontsize=14,
                padding=2,
                background="#954fbd"
    
                
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
                fontsize=13,
                linewidth=2,
                background="#b83dff"

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
