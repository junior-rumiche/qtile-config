from libqtile.config import Key, Group, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget , hook, widget

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
        'border_normal': '#a6c8ff',
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
            widget.GroupBox(),
            widget.WindowName()
            ], 30,)
        ),
  
]
