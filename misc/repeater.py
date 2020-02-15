from talon.voice import Context, Rep, talon
from inspect import signature
from math import floor

from ..utils import optional_numerals, text_to_number

ctx = Context("repeater")

ordinals = {}

def ordinal(n):
    """
    Convert an integer into its ordinal representation::
        ordinal(0)   => '0th'
        ordinal(3)   => '3rd'
        ordinal(122) => '122nd'
        ordinal(213) => '213th'
    """
    n = int(n)
    suffix = ["th", "st", "nd", "rd", "th"][min(n % 10, 4)]
    if 11 <= (n % 100) <= 13:
        suffix = "th"
    return str(n) + suffix

ordinal_words = {}

ordinal_ones = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eight', 'ninth']
ordinal_teens = ['tenth', 'eleventh', 'twelfth', 'thirteenth', 'fourteenth', 'fifteenth', 'sixteenth', 'seventeenth', 'eighteenth', 'nineteenth']
ordinal_tens = ['twentieth', 'thirtieth', 'fortieth', 'fiftieth', 'sixtieth', 'seventieth', 'eightieth', 'ninetieth']
ordinal_tenty = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def ordinal_word(n):
    n = int(n)
    result = ""
    if n > 19:
        if n % 10 == 0:
            result += ordinal_tens[floor((n / 10)) - 2]
        else:
            result += ordinal_tenty[floor(n / 10) - 2]
            result += ordinal_ones[(n % 10) - 1]
    elif n > 9:
        result += ordinal_teens[n - 11]
    else:
        result += ordinal_ones[n - 1]
    return result

for n in range(2, 100):
    ordinals[ordinal(n)] = n - 1
    ordinal_words[ordinal_word(n)] = n - 1

ctx.set_list("ordinals", ordinals.keys())
ctx.set_list("ordinal_words", ordinal_words.keys())


def repeat_ordinal(m):
    o = m["repeater.ordinals"][0]
    repeater = Rep(int(ordinals[o]))
    repeater.ctx = talon
    return repeater(None)

def repeat_ordinal_word(m):
    o = m["repeater.ordinal_words"][0]
    repeater = Rep(int(ordinal_words[o]))
    repeater.ctx = talon
    return repeater(None)

ctx.keymap({
    "{repeater.ordinals}": repeat_ordinal,
    "{repeater.ordinal_words}": repeat_ordinal_word,
})
