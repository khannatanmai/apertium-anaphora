from streamparser import parse

input_stream = input()
#'^El<det><def><m><pl>/The<det><def><m><pl>$ ^grup<n><m><pl>/group<n><pl>$ ^de<pr>/of<pr>/from<pr>$ ^el<det><def><m><sg>/the<det><def><m><sg>$ ^Parlament<n><m><sg>/Parliament<n><sg>$ ^haver<vbhaver><pri><p3><pl>/have<vbhaver><pri><p3><pl>$ ^mostrar<vblex><pp><m><sg>/show<vblex><pp><m><sg>/display<vblex><pp><m><sg>$ ^aquest<det><dem><m><sg>/this<det><dem><m><sg>$ ^dimarts<n><m><sp>/Tuesday<n><ND>$ ^el seu<det><pos><m><sg>/his<det><pos><m><sg>$ ^suport<n><m><sg>/support<n><sg>$ ^a<pr>/at<pr>/in<pr>/to<pr>$ ^el<det><def><m><sg>/the<det><def><m><sg>$ ^*batle/*batle$ ^de<pr>/of<pr>/from<pr>$ ^*Alaró/*Alaró$^.<sent>/.<sent>$'
lexical_units = parse(input_stream)
output_stream = ''
last_noun = ''
for lexical_unit in lexical_units:
        #print('%s → %s\n' % (lexical_unit.wordform, lexical_unit.readings))
        output_stream += '^' + str(lexical_unit)

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

print(output_stream)

