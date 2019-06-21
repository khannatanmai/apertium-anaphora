= GSoc Progress = 

== Work Done == 

* Read the Documentation fully
* Went through code for apertium core (pretransfer, transfer, tagger, etc.)
* Flowchart of the proposed system
* Understand the Apertium pipeline fully
* Modify and Understand individual files
* Get familiar with the files that I need to modify

* Formalise the problem, limit the scope of anaphora resolution (To Anaphora needed for MT)
* Implement a preliminary scoring system for antecedent indicators
* Implement Basic Anaphora for Possessive Pronouns in C++
* Create a transfer-pattern-like file as a way to mark possible NPs as antecedents.
* Implement transfer rules for Possessive Pronouns
* A basic prototype ready
* TEST the prototype with the pipeline


== Ongoing Work ==

* Write Pseudocode for identifying Salience Factors
* '''Study the EuroParl corpus''' and see which anaphors the method will be able to resolve on paper
* Explore Constraint Grammar and use it if it proves to be beneficial
* Implement Basic Anaphora for Reflexive Pronouns (On Verbs) [For Spanish and Catalan]
* Implement Basic Anaphora for Zero Pronouns (On Verbs) [For Spanish and Catalan]
* Implement transfer rules for the above

== Work Plan ==

'''Week 4''' (June 17)
* Implement the system to work out all possible antecedents 
* Add ability to give antecedents a score
* TEST the system extensively
* Document the outline

=== Deliverable #1: Anaphora Resolution for single antecedents, with transfer rules [The full pipeline] ===

'''Evaluation 1: June 24-28'''

'''Week 5''' (June 28)
* Implement Antecedent Indicators:
* Implement Code to Identify Boosting Indicators
* Implement Code to Identify Lappin and Leass Indicators (as many as possible) 

'''Week 6''' (July 4)
* Code to Identify Impeding Indicators
* Code to Identify Adjective Agreement Antecedent
* Implement transfer rules for agreement in adjectives for Cat-Eng & Spa-Eng
* Code to remember antecedents for a certain window
* Give scores to the antecedent indicators

'''Week 7''' (July 10)
* Implement detection of remaining salience features
* Implement remaining transfer rules for anaphora in pronouns Cat-Eng & Spa-Eng
* Code Salience Indicators & Implement tie breaking systems
* Modify the scoring system based on performance in the pairs
* TEST system with French and Russian.

'''Week 8''' (July 16)
* Implement fallback for anaphora (in case of too many antecedents or not past certainty threshold)
* TEST Scoring System
* TEST and Evaluate current system and produce precision and recall
* TEST and Evaluate Agreement for Adjectives
* TEST system with Turkish and any other required language pairs.
* Document Antecedent Indicators, Scoring System, Fallback for Cat-Eng & Spa-Eng

=== Deliverable #2: Anaphora Resolution with saliency features detection, scores, and a fallback mechanism ===

'''Evaluation 2: July 22-26'''

'''Week 9''' [OPTIONAL: If current system not producing good enough results]
* Implement Expectation-Maximization Algorithm using monolingual corpus
* Compare with current system
* Test EM Algorithm and the implemented system

'''Week 9''' [NOT OPTIONAL] (July 26)

* Implement code to ignore embedded clauses
* Evaluate increase in detection
* Insert into Apertium pipeline
* Implement code to accept input in chunks and process it

'''Week 10''' (August 1)
* EXTENSIVELY TEST final system
* Test with French, Russian, Turkish, Galician, etc.
* Evaluate and find out which features are language agnostic
* Decide on list of features for agnostic anaphora and for language specific anaphora

'''Week 11''' (August 7)
* Any remaining coding and improving the system
* TEST on multiple pairs and give Evaluation Scores
* TEST for backwards compatibility and ensure it

'''Week 12''' (August 13)
* Wrap up on the final module
* Complete the overall documentation with observations and future prospects

'''Final Evaluations: August 19-26'''

=== Project Completed ===
'''NOTE''': Week 11 and Week 12 have extra time to deal with unforeseen issues and ideas
----
