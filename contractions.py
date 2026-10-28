"""Spoken-English contractions (I will → I'll) for the phrases the professor reads aloud."""
import re

# Longest first. Not applied when the phrase ends right after the pair ("Yes, it is."), where English keeps both words.
PAIRS = [
    ("it is not", "it's not"), ("that is not", "that's not"), ("will not", "won't"), ("do not", "don't"), ("does not", "doesn't"), ("did not", "didn't"), ("cannot", "can't"),
    ("is not", "isn't"), ("are not", "aren't"), ("was not", "wasn't"), ("have not", "haven't"),
    ("I will", "I'll"), ("you will", "you'll"), ("we will", "we'll"), ("it will", "it'll"),
    ("I am", "I'm"), ("you are", "you're"), ("we are", "we're"), ("they are", "they're"),
    ("it is", "it's"), ("that is", "that's"), ("there is", "there's"), ("what is", "what's"), ("here is", "here's"),
    ("let us", "let's"),
]
RX = [(re.compile(rf"\b{re.escape(a)}\b(?!\s*[.?!,;:]|\s*$)", re.I), b) for a, b in PAIRS]


def _keep_case(src, rep):
    return rep[0].upper() + rep[1:] if src[0].isupper() else rep


def contract(text):
    if not text or "`" in text:
        return text
    # leave commands and file names alone: only touch the prose before "Run:" or a command line
    for rx, rep in RX:
        text = rx.sub(lambda m: _keep_case(m.group(0), rep), text)
    return text
