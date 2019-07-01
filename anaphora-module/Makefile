#Makefile for Anaphora

PROGNAME = anaphora

$(PROGNAME): parse_biltrans.cc score.cc anaphora.cc
	g++ -o $(PROGNAME) parse_biltrans.cc score.cc anaphora.cc

clean:
	rm $(PROGNAME)
