Scoring Decisions

- Scoring module will have two kinds of storage for LUs
- Each LU will be given a unique id (unsigned int) --NOTSURE
- All LUs - id and wordform, tlwordform and tags
- Antecedents Vector - LU and score

Need to keep ids for unique identification, for recognising patterns, etc. (NOT NECESSARILY)
Each word will have a score

Add word Function: (Done)
adds all words to a sentence and them into a queue(deque)
History is a queue of sentences
Each sentence is a vector of words
If queue stores more than 4 sentences, the earliest stored one is removed
Context Limits:
We only keep the context limited to 3 sentences before the pronoun.

Agreement Filters:
First we remove antecedents from the list which don't agree with the pronoun (gender and number)

Flow:
Go through queue in reverse
Go through each sentence left to right
When reach a noun, check agreement, if no, continue to next word
If yes,
apply indicators one by one
With final score, add to final antecedent list

Once done,
Go through final antecedent list and see highest scored one



When a pronoun

PROBABLY NEED A DESTRUCTOR FOR SCORE CLASS

