from talon.voice import Context, Key

enabled = True

def is_android(app, _):
    global enabled
    return enabled and app.name == "jetbrains-studio"

#context = Context("anki", bundle="org.mozilla.anki")
context = Context("android", func=is_android)

context.keymap(
    {
        "state (bool | boolean)": "boolean ",
        "state void": "void ",
        "state int": "int ",
        "state string": "string ",
        "state public": "public ",
        "state private": "private ",
        "state else if": "else if ",
        "few": "view",
        "state find (view | few) by (id | idea)": "findViewById(R.id."
    }
)
