def lex(chars):
    while chars.next is not None:
        c = chars.move_next()
        if c in " \n": pass
        elif c in "+-*/": yield ("operation", c)
        elif c in "(){},;=:": yield (c, "")
        elif c in ("'", '"'): yield ("string", _scan_string(c, chars))
        elif re.match("[.0-9]", c): yield ("number", _scan(c, chars, "[.0-9]"))
        elif re.match("[_a-zA-Z]", c): yield ("symbol", _scan(c, chars, "[_a-zA-Z0-9]"))
        else: raise Exception


assert (
    list(lex('print("Hello, world!");'))
    ==
    [ ("symbol", "print")
    , ("(", "")
    , ("string", "Hello, world!")
    , (")", "")
    , (";", "")
    ]
)
