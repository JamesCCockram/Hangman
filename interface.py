import textwrap

def print_ASCII(ascii_str):
  "Print ASCII art."
  print(textwrap.dedent(ascii_str))

# draw gallows
def drawBoard(bad_guesses, word):
  length = len(bad_guesses)

  # this is also always drawn
  print_ASCII("""
    ______________
    | /          |
    |/           |
    |{0}          {2}{1}{3}
    |            {4}
    |            {5}
    |           {6} {7}
    |
    |
    | {8}
    |________________|""".format('  ' if length == 1 else '', 'O' if length > 0 else '', '__' if len(bad_guesses) > 1 else '',
                                 '__' if len(bad_guesses) > 2 else '', '|' if length > 3 else '', '|' if length > 4 else '',
                                 '/' if length > 5 else '', '\\' if length > 6 else '',
                                 ' '.join(map(lambda s: '[%s]' % s, bad_guesses))).strip('\n'))
