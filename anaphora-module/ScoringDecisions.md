Scoring Decisions

- Scoring module will have two kinds of storage for LUs
- Each LU will be given a unique id (unsigned int)
- All LUs - id and wordform
- Antecedents Vector - id, wordform and score

Need to keep ids for unique identification, for recognising patterns, etc.

Add word Function:
adds all words to history
if noun, add to antecedent list with score 2

Referential Distance Function:
Reach \<sent\> and reduce score for all antecedents in list by 1 (minimum -1)