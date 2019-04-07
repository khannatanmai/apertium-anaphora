from streamparser import parse
import sys
import time

start = time.time()

def is_intstring(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

csize = 1024

if len(sys.argv) < 2:
    print("Using Default Chunk Size = 1024", file=sys.stderr)
else:
    if not is_intstring(sys.argv[1]):
        print("Chunk size must be an integer! Exit.", file=sys.stderr)
        sys.exit(1)
    else:
        csize = int(sys.argv[1])

count = 0

def read_in_chunks(file_object, chunk_size):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

add_to_next_chunk = ''

with sys.stdin as f: #f = sys.stdin
    last_noun = ''
    for piece in read_in_chunks(f, csize):

        piece = add_to_next_chunk + piece #Adding cut info from last chunk

        i = len(piece) - 1

        while(i >= 0): #looking for the last LU before the chunk ends
            if(piece[i] == '$'):
                break

            i -= 1

        add_to_next_chunk = piece[i+1:]

        lexical_units = parse(piece) #IMPORTANT: the parse excludes any LU that has been cut
        output_stream = ''

        for lexical_unit in lexical_units: 
            count += 1
            output_stream += '^' + str(lexical_unit) + '/'

            if(len(lexical_unit.readings[0][0][1]) > 0):
                
                if(lexical_unit.readings[0][0][1][0] == 'n'):
                    last_noun = str(lexical_unit)
                    last_noun = last_noun.split('/')[-1] #Taking only the last option (the one in English)

                tags = lexical_unit.readings[0][0][1]

                if(('det' in tags and 'pos' in tags) or ('prn' in tags)): #If it's a determiner and possessive, it needs anaphora resolution, can add other tags here
                    output_stream += last_noun #If there's no last noun, then nothing will be concatenated

            output_stream += '$ '

        sys.stdout.write(output_stream) #Uncomment to see output
            #print(last_noun)


end = time.time()
#print("Time Taken:")
#print(end - start)

print("Time Taken:", file=sys.stderr)
print(end - start, file=sys.stderr)

#print("Total Token Count" + str(count))
print("Total Token Count:" + str(count), file=sys.stderr)
