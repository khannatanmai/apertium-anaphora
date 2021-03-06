# Anaphora Resolution
## Apertium
## Google Summer of Code 2019

**This module has been moved to the official apertium organisation's repository. Find it here: https://github.com/apertium/apertium-anaphora**

### How to Run
- `cd anaphora-module`
- `make`
- `anaphora`: Executable File
- Usage: `./anaphora -[Flags] ref_file.xml`

- Usage in Pipeline:
`apertium-deshtml < input.txt | lt-proc spa-eng.automorf.bin | apertium-tagger -g $2 spa-eng.prob | apertium-pretransfer | lt-proc -b spa-eng.autobil.bin | lrx-proc -m spa-eng.autolex.bin | ./anaphora ref_file.xml | apertium-transfer -b apertium-eng-spa.spa-eng.t1x spa-eng.t1x.bin | apertium-interchunk apertium-eng-spa.spa-eng.t2x spa-eng.t2x.bin | apertium-postchunk apertium-eng-spa.spa-eng.t3x spa-eng.t3x.bin | lt-proc -g spa-eng.autogen.bin | lt-proc -p spa-eng.autopgen.bin | apertium-retxt`

### Flags

- -z : Null Flush

### Files
- `anaphora-module/`: 		C++ Code for Anaphora Module
- `Europarl	Annotation/`: 	Annotating Errors in Europarl Corpus
- `Saliency_Scores/`: 		Several options for Saliency Scores
- `Research/`: 				Relevant Research Papers
- `Coding Challenge/`: 		Contains the Coding Challenge for GSoC 2019
- `Proposal.pdf`: 			Proposal for the project 'Anaphora Resolution'
- `Progress.md`: 			Progress Report for the Project!



