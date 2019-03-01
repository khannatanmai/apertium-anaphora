from streamparser import parse

import time
start = time.time()

count = 0

with open("input.txt", "rb") as f:
    byte = f.read(1)

    input_stream = ''
    last_noun = ''
    flag = 0


    while byte != b'':
        # Do stuff with byte.
        byte = f.read(1)

        byte_str = byte.decode("utf-8", "ignore") #Can Edit whichever UNICODE is followed by Apertium
        #Currently NOT reading ó character - Not sure why, As it Exists in utf-8

        if(byte_str == '^'):
                flag = 1 #processing begins

        if(flag == 1):
                input_stream += str(byte_str) #add to input stream

        if(byte_str == '$'): #token processed
                flag = 0
                count += 1

                #print(str(input_stream))

                lexical_units = parse(input_stream)
                output_stream = ''

                for lexical_unit in lexical_units: #Now this should be only one lexical unit -- can be changed
                        output_stream += '^' + str(lexical_unit)
                        #print(lexical_unit)

                        if(len(lexical_unit.readings[0][0][1]) > 0):
                        	#print(lexical_unit.readings[0][0][1][0])

                        	if(lexical_unit.readings[0][0][1][0] == 'n'):
                        		last_noun = str(lexical_unit)
                        		last_noun = last_noun.split('/')[-1] #Taking only the last option (the one in English)

                        	tags = lexical_unit.readings[0][0][1]

                        	if(('det' in tags and 'pos' in tags) or ('prn' in tags)): #If it's a determiner and possessive, it needs anaphora resolution, can add other tags here
                        		output_stream += '/' + last_noun #If there's no last noun, then nothing will be concatenated

                        output_stream += '$ '

                        #print(last_noun)

                #print(output_stream) #Uncomment to see output

                input_stream = ''

end = time.time()
print("Time Taken:")
print(end - start)

print("Total Token Count" + str(count))
