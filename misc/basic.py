from talon.voice import Context, Str, press
import string

alpha_alt = "air bat cap drum each fine gust harp ice jury crunch look made near odd pit quench red sun trap urge vest whale plex yank zip".split()
# digits_alt = 'one two three four five six seven eight nine'

f_keys = {f"F {i}": f"f{i}" for i in range(1, 13)}
# arrows are separated because 'up' has a high false positive rate
arrows = ["left", "right", "up", "down"]
simple_keys = ["tab", "escape", "enter", "space", "pageup", "pagedown"]
alternate_keys = {"delete": "backspace", "forward delete": "delete"}
symbols = {
    "back tick": "`",
    "comma": ",",
    "dot": ".",
    "period": ".",
    "semi": ";",
    "semicolon": ";",
    "quote": "'",
    "L square": "[",
    "left square": "[",
    "square": "[",
    "R square": "]",
    "right square": "]",
    "forward slash": "/",
    "slash": "/",
    "backslash": "\\",
    "minus": "-",
    "dash": "-",
    "equals": "=",
}
modifiers = {
    "command": "ctrl",
    "control": "ctrl",
    "shift": "shift",
    "alt": "alt",
    "option": "alt",
}

alphabet = dict(zip(alpha_alt, string.ascii_lowercase))
digits = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

#digits = dict(zip(digits_alt, string.ascii_lowercase))
simple_keys = {k: k for k in simple_keys}
arrows = {k: k for k in arrows}
keys = {}
keys.update(f_keys)
keys.update(simple_keys)
keys.update(alternate_keys)
keys.update(symbols)

# map alnum and keys separately so engine gives priority to letter/number repeats
keymap = keys.copy()
keymap.update(arrows)
keymap.update(alphabet)
keymap.update(digits)


def insert(s):
    Str(s)(None)


def get_modifiers(m):
    try:
        return [modifiers[mod] for mod in m["basic.modifiers"]]
    except KeyError:
        return []


def get_keys(m):
    groups = ["basic.keys", "basic.arrows", "basic.digits", "basic.alphabet"]
    for group in groups:
        try:
            return [keymap[k] for k in m[group]]
        except KeyError:
            pass
    return []


def uppercase_letters(m):
    insert("".join(get_keys(m)).upper())


def press_keys(m):
    mods = get_modifiers(m)
    keys = get_keys(m)
    if mods:
        press("-".join(mods + [keys[0]]))
        keys = keys[1:]
    for k in keys:
        press(k)


ctx = Context("basic")
ctx.keymap(
    {
        "(uppercase | ship) {basic.alphabet}+ [(lowercase | sunk)]": uppercase_letters,
        "{basic.modifiers}* {basic.alphabet}+": press_keys,
        "{basic.modifiers}* {basic.digits}+": press_keys,
        "{basic.modifiers}* {basic.keys}+": press_keys,
        "(go | {basic.modifiers}+) {basic.arrows}+": press_keys,
    }
)
ctx.set_list("alphabet", alphabet.keys())
ctx.set_list("arrows", arrows.keys())
ctx.set_list("digits", digits.keys())
ctx.set_list("keys", keys.keys())
ctx.set_list("modifiers", modifiers.keys())