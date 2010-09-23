# -*- coding: utf-8 -*-
"""
    logbook._termcolors
    ~~~~~~~~~~~~~~~~~~~

    Provides terminal color mappings.

    :copyright: (c) 2010 by Armin Ronacher, Georg Brandl.
    :license: BSD, see LICENSE for more details.
"""

esc = "\x1b["

codes = {}
codes[""]          = ""
codes["reset"]     = esc + "39;49;00m"

codes["bold"]      = esc + "01m"
codes["faint"]     = esc + "02m"
codes["standout"]  = esc + "03m"
codes["underline"] = esc + "04m"
codes["blink"]     = esc + "05m"
codes["overline"]  = esc + "06m"

dark_colors  = ["black", "darkred", "darkgreen", "brown", "darkblue",
                "purple", "teal", "lightgray"]
light_colors = ["darkgray", "red", "green", "yellow", "blue",
                "fuchsia", "turquoise", "white"]

x = 30
for d, l in zip(dark_colors, light_colors):
    codes[d] = esc + "%im" % x
    codes[l] = esc + "%i;01m" % x
    x += 1

del d, l, x

codes["darkteal"]   = codes["turquoise"]
codes["darkyellow"] = codes["brown"]
codes["fuscia"]     = codes["fuchsia"]
codes["white"]      = codes["bold"]


def colorize(color_key, text):
    """Returns an ANSI formatted text with the given color."""
    return codes[color_key] + text + codes["reset"]


def ansiformat(attr, text):
    """Format ``text`` with a color and/or some attributes::

        color       normal color
        *color*     bold color
        _color_     underlined color
        +color+     blinking color
    """
    result = []
    if attr[:1] == attr[-1:] == '+':
        result.append(codes['blink'])
        attr = attr[1:-1]
    if attr[:1] == attr[-1:] == '*':
        result.append(codes['bold'])
        attr = attr[1:-1]
    if attr[:1] == attr[-1:] == '_':
        result.append(codes['underline'])
        attr = attr[1:-1]
    result.append(codes[attr])
    result.append(text)
    result.append(codes['reset'])
    return ''.join(result)
