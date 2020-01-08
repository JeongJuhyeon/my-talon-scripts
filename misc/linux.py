from talon.voice import Key, Context, Str, press

context = Context("linux")

keymap = {
    "win max": Key("super-up"),
    "win left": Key("super-left"),
    "win small": Key("super-down"),
    "win right": Key("super-right"),
}

context.keymap(keymap)
