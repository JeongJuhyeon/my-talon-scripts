from talon.voice import Context, Key


enabled = True

def is_anki(app, _):
    global enabled
    return enabled and app.name == "Anki"

#context = Context("anki", bundle="org.mozilla.anki")
context = Context("anki", func=is_anki)

keymap = {
"sink": Key("Y"),
"new cards": Key("A"),
"browse": Key("B"),
"add": Key("ctrl-enter"),
"show": Key("space"),
"again": Key("1"),
"hard": Key("2"),
"good": Key("3"),
"easy": Key("4"),
"anki undo": Key("ctrl-z"),
}

context.keymap(keymap)
