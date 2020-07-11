# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

#from libqtile.config import Key, Screen, Group, Drag, Click
#from libqtile.lazy import lazy
#from libqtile import layout, bar, widget

#from typing import List  # noqa: F401

import os
import re
import socket
import subprocess
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from typing import List  # noqa: F401

mod = "mod4"



keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down()),
    Key([mod], "j", lazy.layout.up()),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down()),
    Key([mod, "control"], "j", lazy.layout.shuffle_up()),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "Return", lazy.spawn("alacritty")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "x", lazy.window.kill()),

    Key([mod], "q", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawn("rofi -show drun -show-icons")),
#    Key([mod], "h", lazy.layout.grow(), lazy.layout.increase_nmaster()),
#    Key([mod], "l", lazy.loayut.shrink(), lazy.layout.increase_nmaster())
         Key(
             [mod], "h",
             lazy.layout.grow(),
             lazy.layout.increase_nmaster(),
             desc='Expand window (MonadTall), increase number in master pane (Tile)'
             ),
         Key(
             [mod], "l",
             lazy.layout.shrink(),
             lazy.layout.decrease_nmaster(),
             desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
             ),

         Key(
             [mod], "t",
             lazy.window.toggle_floating(),
             desc='toggle floating'
             ),

    Key([mod, "shift"], "s", lazy.spawn("scrot")),
]

# groups = [Group(i) for i in "

#group_names = [("1", {'layout': 'monadtall'}),
#
#]

group_names = [("1", {'layout': 'monadtall'}),
               ("2", {'layout': 'monadtall'}),
               ("3", {'layout': 'monadtall'}),
               ("4", {'layout': 'monadtall'}),
               ("5", {'layout': 'monadtall'}),
               ("6", {'layout': 'monadtall'}),
               ("7", {'layout': 'monadtall'}),
               ("8", {'layout': 'monadtall'}),
               ("9", {'layout': 'floating'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]


for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

#group_names = [("1", {'layout': 'monadtall'}),
#               ("2", {'layout': 'monadtall'}),
#               ("3", {'layout': 'monadtall'}),
#               ("4", {'layout': 'monadtall'}),
#               ("5", {'layout': 'monadtall'}),
#               ("6", {'layout': 'monadtall'}),
#               ("7", {'layout': 'monadtall'}),
#               ("8", {'layout': 'monadtall'}),
#               ("9", {'layout': 'floating'})]


for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group


layout_theme = {"border_width": 2,
                "margin": 6,
                "border_focus": "b48ead",
                "border_normal": "1D2330"
                }

layouts = [
    # layout.Max(),
    layout.Stack(num_stacks=2, **layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    # layout.Columns(),
    # layout.Matrix(),
    layout.MonadTall(**layout_theme),
    layout.Floating(**layout_theme)
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='Hack',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

colors = [["#2e3440", "#2e3440"], # panel background
          ["#4c566a", "#4c566a"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#bf616a", "#bf616a"], # border line color for current tab
          ["#8d62a9", "#8d62a9"], # border line color for other tab and odd widgets
          ["#5e81ac", "#5e81ac"], # color for the even widgets
          ["#b48ead", "#b48ead"], # window name
          ["#88c0d0", "#88c0d0"],
          ["#4c566a", "#4c566a"]] 


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                        linewidth=0,
                        padding = 6,
                        foreground = colors[2],
                        background = colors[0]
                        ),
                # widget.CurrentLayout(),
                widget.GroupBox(
                        font="Hack",
                        fontsize=12,
                        margin_y = 3,
                        margin_x = 0,
                        padding_y = 5,
                        padding_x = 5,
                        borderwidth = 3,
                        active = colors[2],
                        inactive = colors[2],
                        rounded = False,
                        highlight_color = colors[1],
                        highlight_method = "line",
                        this_current_screen_border = colors[3],
                        this_screen_border = colors [4],
                        other_current_screen_border = colors[0],
                        other_screen_border = colors[0],
                        foreground = colors[2],
                        background = colors[0]
                        ),
                widget.Prompt(
                        background = colors[0]
                        ),
                widget.WindowName(
                        background = colors[0],
                        foreground = colors[6]
                        ),
                widget.TextBox(
                        text='',
                        background = colors[0],
                        foreground = colors[7],
                        padding=0,
                        fontsize=37
                        ),
                # widget.Systray(),
                widget.TextBox(
                        background = colors[7],
                        foreground = colors[8],
                        text=" ⟳"
                        ),
                widget.Pacman(
                        background = colors[7],
                        foreground = colors[8],
                        execute = "alacritty -e sudo pacman -Syyu",
                        update_interval = 20000
                        ),

                widget.TextBox(
                        text='',
                        background = colors[7],
                        foreground = colors[8],
                        padding=0,
                        fontsize=37
                        ),
                widget.CurrentLayout(
                            background = colors[8],
                            foreground = colors[2],
                            padding=5
                            ),
                #widget.Clock(format='%Y-%m-%d %a %I:%M %p',
                #        background = colors[8],
                #        foreground = colors[2]
                #        ),
                # widget.QuickExit(),

                widget.TextBox(
                        text='',
                        background = colors[8],
                        foreground = colors[7],
                        padding=0,
                        fontsize=37
                        ),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p',
                        background = colors[7],
                        foreground = colors[8]
                        ),
                widget.Systray(
                        background = colors[7],
                        foreground = colors[8]
                        )
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
