from streamparser import parse_file, reading_to_string
import sys
for blank, lu in parse_file(sys.stdin, with_text=True):
    print(blank+" ".join("^{}/{}$".format(lu.wordform, reading_to_string(r))
                         for r in lu.readings),
          end="")