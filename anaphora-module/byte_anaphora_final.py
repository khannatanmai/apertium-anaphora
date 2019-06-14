from streamparser import parse
import sys

with sys.stdin as f:

    input_stream = ''
    last_noun = ''
    flag = 0

    byte = f.read(1)
    while byte:

        if(byte == '^'):
            flag = 1 #processing begins

        if(flag == 1):
            input_stream += str(byte) #add to input stream

        if(flag == 0):
            output_stream = str(byte) #everything except LUs
            sys.stdout.write(output_stream)

        if(byte == '$'): #token processed
            flag = 0

            lexical_units = parse(input_stream)
            output_stream = ''

            for lexical_unit in lexical_units: #Now this should be only one lexical unit -- can be changed
                output_stream += '^' + str(lexical_unit) + '/'

                if(len(lexical_unit.readings) > 0): #sometimes there's no analysis in tl

                    if(len(lexical_unit.readings[0][0][1]) > 0):

                        if(lexical_unit.readings[0][0][1][0] == 'n'):
                            last_noun = str(lexical_unit)
                            last_noun = last_noun.split('/')[-1] #Taking only the last option (the one in English)

                        tags = lexical_unit.readings[0][0][1]

                        if(('det' in tags and 'pos' in tags) or ('prn' in tags)): #If it's a determiner and possessive, it needs anaphora resolution, can add other tags here
                            output_stream += last_noun #If there's no last noun, then nothing will be concatenated

                output_stream += '$'

            sys.stdout.write(output_stream) #Uncomment to see output

            input_stream = ''

        byte = f.read(1)
 