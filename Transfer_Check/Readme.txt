1. Put the python code in the language repo and run the pipeline with the anaphora module just to see if the modules are backwards compatible.

Usual Command:
lt-proc spa-eng.automorf.bin < input.txt | apertium-tagger -g $2 spa-eng.prob | apertium-pretransfer | lt-proc -b spa-eng.autobil.bin | lrx-proc -m spa-eng.autolex.bin | apertium-transfer -b apertium-eng-spa.spa-eng.t1x spa-eng.t1x.bin | apertium-interchunk apertium-eng-spa.spa-eng.t2x spa-eng.t2x.bin | apertium-postchunk apertium-eng-spa.spa-eng.t3x spa-eng.t3x.bin | lt-proc -g spa-eng.autogen.bin | lt-proc -p spa-eng.autopgen.bin 


Pre Anaphora Command:
lt-proc spa-eng.automorf.bin < test.txt | apertium-tagger -g $2 spa-eng.prob | apertium-pretransfer | lt-proc -b spa-eng.autobil.bin | lrx-proc -m spa-eng.autolex.bin > output_biltrans.txt

Anaphora Command:
python3 anaphora/chunk_anaphora.py < output_biltrans.txt > output_anaphora.txt

Post Anaphora Command:
apertium-transfer -b apertium-eng-spa.spa-eng.t1x spa-eng.t1x.bin < ideal_output_anaphora.txt | apertium-interchunk apertium-eng-spa.spa-eng.t2x spa-eng.t2x.bin | apertium-postchunk apertium-eng-spa.spa-eng.t3x spa-eng.t3x.bin | lt-proc -g spa-eng.autogen.bin | lt-proc -p spa-eng.autopgen.bin

Post Transfer Rules Output:
Tanmais-MacBook-Pro:apertium-eng-spa khannatanmai$ apertium-preprocess-transfer transfer_anaphora.t1x transfer_anaphora.t1x.bin
Tanmais-MacBook-Pro:apertium-eng-spa khannatanmai$ apertium-transfer -b transfer_anaphora.t1x transfer_anaphora.t1x.bin < ideal_output_anaphora.txt
^default<default>{^The<det><def><m><pl>$}$ ^default<default>{^group<n><pl>$}$ ^default<default>{^of<pr>$}$ ^default<default>{^the<det><def><m><sg>$}$ ^default<default>{^Parliament<n><sg>$}$ ^default<default>{^have<vbhaver><pri><p3><pl>$}$ ^default<default>{^show<vblex><pp><m><sg>$}$ ^default<default>{^this<det><dem><m><sg>$}$ ^default<default>{^Tuesday<n><ND>$}$ ^ref<ref>{^their<det><pos><m><pl>$}$ ^default<default>{^support<n><sg>$}$ ^default<default>{^at<pr>$}$ ^default<default>{^the<det><def><m><sg>$}$ ^unknown<unknown>{^*batle$}$ ^default<default>{^of<pr>$}$ ^unknown<unknown>{^*Alaró$}$ ^default<default>{^.<sent>$}$