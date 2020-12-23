from libqtile.command import lazy
from libqtile.config import Key
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

