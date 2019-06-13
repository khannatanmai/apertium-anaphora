1. Put the python code in the language repo and run the pipeline with the anaphora module just to see if the modules are backwards compatible.

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

Final Transfer Output: (with macros):
Tanmais-MacBook-Pro:apertium-eng-spa khannatanmai$ apertium-transfer -b apertium-eng-spa.spa-eng.t1x apertium-eng-spa.spa-eng.t1x.bin < ideal_output_anaphora.txt 
^Det_nom<SN><m><pl>{^the<det><def><3>$ ^group<n><3>$}$ ^de<PREP>{^of<pr>$}$ ^det_nom<SN><m><sg>{^the<det><def><3>$ ^Parliament<n><3>$}$ ^haver_pp<SV><vblex><pri><p3><pl>{^have<vbhaver><pres>$ ^show<vblex><pp>$}$ ^det_nom<SN><m><sg>{^this<det><dem><3>$ ^Tuesday<n><3>$}$ ^det_nom<SN><m><sg>{^their<det><pos><3>$ ^support<n><3>$}$ ^a<PREP>{^at<pr>$}$ ^det<DET><m><sg>{^the<det><def><3>$}$ ^unknown<unknown>{^*batle$}$ ^de<PREP>{^of<pr>$}$ ^unknown<unknown>{^*Alaró$}$ ^punt<sent>{^.<sent>$}$

FINAL OUTPUT:
apertium-transfer -b apertium-eng-spa.spa-eng.t1x spa-eng.t1x.bin < ideal_output_anaphora.txt | apertium-interchunk apertium-eng-spa.spa-eng.t2x spa-eng.t2x.bin | apertium-postchunk apertium-eng-spa.spa-eng.t3x spa-eng.t3x.bin | lt-proc -g spa-eng.autogen.bin | lt-proc -p spa-eng.autopgen.bin

The groups of the Parliament have showed this Tuesday their support at the *batle of *Alaró .