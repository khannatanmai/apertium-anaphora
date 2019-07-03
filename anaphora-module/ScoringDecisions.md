Scoring Decisions

- Scoring module will have two kinds of storage for LUs
- Each LU will be given a unique id (unsigned int) --NOTSURE
- All LUs - id and wordform, tlwordform and tags
- Antecedents Vector - LU and score

Need to keep ids for unique identification, for recognising patterns, etc. (NOT NECESSARILY)
Each word will have a score

Add word Function:
adds all words to a sentence and them into a queue
History is a queue of sentences
Each sentence is a vector of words
If queue stores more than 4 sentences, the earliest stored one is removed


Agreement Filters:
First we remove antecedents from the list which don't agree with the pronoun (gender and number)
Context Limits:
We only keep the context limited to 3 sentences before the pronoun.

When a pronoun

PROBABLY NEED A DESTRUCTOR FOR SCORE CLASS