#Makefile for Anaphora

PROGNAME = anaphora
LIBXML_FLAGS = -I /opt/local/include/libxml2/ -L /usr/lib -lxml2 -lz -lpthread -lm

$(PROGNAME): parse_ref.cc parse_biltrans.cc score.cc anaphora.cc
	g++ parse_ref.cc parse_biltrans.cc score.cc anaphora.cc -o $(PROGNAME) $(LIBXML_FLAGS)
	
clean:
	rm $(PROGNAME)
