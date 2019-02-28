from streamparser import parse_file, mainpos, reading_to_string

filein = open('input.txt', 'r')

file = filein.read()

for blank, lu in parse_file(file, with_text=True): 
    analyses = lu.readings
    firstreading = analyses[0]
    surfaceform = lu.wordform
    # rewrite to print only the first reading (and surface/word form):
    print("^{}/{}$".format(surfaceform, 
                           reading_to_string(firstreading)))
    # convenience function to grab the first part of speech of the first reading:
    mainpos = mainpos(lu)