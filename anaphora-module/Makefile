#Makefile for Anaphora

prefix = /Users/khannatanmai/Documents/GSoC/repo/main

PROGNAME = anaphora
LIBXML_FLAGS = -I /opt/local/include/libxml2/ -L /usr/lib -lxml2 -lz -lpthread -lm
INCLUDE_FLAGS = -I $(prefix)/include/lttoolbox-3.5

SOURCES = pattern_ref.cc parse_ref.cc parse_biltrans.cc score.cc anaphora.cc ../../main/lttoolbox/lttoolbox/xml_parse_util.cc 

$(PROGNAME): $(SOURCES)
	g++ $(SOURCES) -o $(PROGNAME) $(LIBXML_FLAGS) $(INCLUDE_FLAGS)

clean:
	rm $(PROGNAME)
