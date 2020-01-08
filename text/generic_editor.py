from talon.voice import Key, press, Str, Context
from ..utils import parse_word, numerals, optional_numerals, text_to_number, jump_to_target, delay
from time import sleep

ctx = Context("generic_editor")

# actions and helper functions
def jump_to_bol(m):
    line = text_to_number(m)
    press("ctrl-g")
    Str(str(line))(None)
    press("tab")

def jump_to_end_of_line():
    press("ctrl-right")


def jump_to_beginning_of_text():
    press("ctrl-left")


def jump_to_nearly_end_of_line():
    press("left")


def jump_to_bol_and(then):
    def fn(m):
        if len(m._words) > 1:
            jump_to_bol(m)
        else:
            press("ctrl-a")
            press("ctrl-left")
        then()

    return fn


def jump_to_eol_and(then):
    def fn(m):
        if len(m._words) > 1:
            jump_to_bol(m)
        press("end")
        then()

    return fn


def toggle_comments(*unneeded):
    press("ctrl-/")


def snipline():
    press("ctrl-shift-k")


def get_first_word(m):
    return m.dgndictation.words[0]

def jump_to(m):
    target = get_first_word(m)
    jump_to_target(target)


keymap = {
    "(trundle | comment)": toggle_comments,
    "(trundle | comment)"
    + numerals(): jump_to_bol_and(toggle_comments),  # noop for plain/text
    "snipline" + optional_numerals(): jump_to_bol_and(snipline),
    "bridge" + optional_numerals(): jump_to_bol,
    "spring" + optional_numerals(): jump_to_eol_and(jump_to_beginning_of_text),
    "sprinkoon" + numerals(): jump_to_eol_and(lambda: press("enter")),
    "dear" + optional_numerals(): jump_to_eol_and(lambda: None),
    "smear" + optional_numerals(): jump_to_eol_and(jump_to_nearly_end_of_line),
    # general
    "fullscreen": Key("ctrl-ctrl-f"),
    # file
    # "new": Key("ctrl-n"),
    "(save | safe)": Key("ctrl-s"),
    "close (file | tab)": Key("ctrl-w"),
    # selection
    "(select | cell) up": Key("shift-up"),
    "(select | cell) down": Key("shift-down"),
    "(select | cell) all": Key("ctrl-a"),
    "(select | cell) bottom ": Key("ctrl-shift-down"),
    "(select | cell) right": Key("shift-right"),
    "(select | cell) left": Key("shift-left"),
    "(select | cell) word": Key("shift-alt-left"),
    "(select | cell) (end | push)": Key("ctrl-shift-right"),
    "(select | cell) (start | begin | pop)": Key("ctrl-shift-left"),
    # edit
    "paste match": Key("ctrl-shift-v"),
    "shove": Key("ctrl-]"),
    "tug": Key("ctrl-["),
    "(scrap | scratch | delete) word": Key("alt-backspace"),
    "(scrap | scratch | delete) (begin | start)": Key("ctrl-backspace"),
    # navigation
    "push": Key("ctrl-right"),
    "pop": Key("ctrl-left"),
    "step": Key("alt-right"),
    "stone": Key("alt-left"),
    "jump to <dgndictation>": jump_to,
}

ctx.keymap(keymap)
