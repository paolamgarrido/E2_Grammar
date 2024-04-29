# E1 Implementation of Lexical Analysis

## Description
Grammars play a pivotal role in the implementation of computational methods for language processing since they provide a formal foundation for understanding, generating, and manipulating linguistic data in a wide range of applications. Essentially, a grammar describes the structure of a language, consisting of a set of rules that dictate how words and symbols in a language can be combined to form valid sentences or strings. In this context, we will delve into the development of a parser designed to accurately detect whether the sentences in question are indeed part of the grammar’s language.

The language in focus is Danish, for which we will build a grammar that accepts certain Danish words and the following sentence structures:

1. **Main Clauses**: consist of a Noun phrase + Verb phrase
2. **Noun Phrases**: are built mainly with nouns, determiners, and pronouns
3. **Verb Phrases**: are built mainly with verbs, verbs with prepositional phrases, and adverbs
4. **Subordinated Sentences**: they start with a conjunction followed by a Verb phrase + Noun phrase and end with a Main clause
5. **Sentences separated by commas and conjunctions**: a set of nouns and verbs separated by commas or Main clauses separated by conjunctions
Note: All sentences must end with a period.

To implement this solution, we will utilize an LL(1) parser, a top-down parsing technique commonly employed in computational linguistics. The term "LL" signifies "left-to-right, leftmost derivation," denoting the parser's approach of reading input and constructing parse trees. It initiates parsing from the leftmost symbol of the input string and progresses towards the right. The "(1)" indicates that the parser employs a single token of lookahead when making parsing decisions, streamlining the parsing process and obviating the need for backtracking.

It's essential to highlight that this method entails the use of a parsing table (which we will elaborate on later). This table serves to map combinations of non-terminal symbols and lookahead tokens to production rules.

https://www.geeksforgeeks.org/construction-of-ll1-parsing-table/

## Models

In the process of implementing a parser for our language, constructing an appropriate grammar serves as the cornerstone of successful parsing. To achieve this goal, we will go through three fundamental construction steps, meticulously designed to ensure completeness, clarity, and efficiency in parsing sentences.

First, we will initiate the process by generating a grammar that encapsulates the essence and structure of our language's syntax.

**M1**
S -> NP VP | NP | VP | SC Punct VP NP PP | S Punct | S Conj S 
SC -> Conj NP VP
PP -> P NP
NP -> N | DetN | Pron | Det N | Pron N | Det AdjE N | NP PP | NP Punct NP | NP Conj NP
VP -> V | V NP | V AdvE | V NP AdvE | V PP | VP Punct VP | VP Conj VP
AdjE -> Adj Conj Adj | Adj 
AdvE -> Adv Conj Adv | Adv 

During this phase, our focus lies in identifying the basic syntactic units and establishing rules governing sentence formation. We define non-terminal symbols to represent distinct syntactic categories, alongside sequences of terminal symbols representing words or punctuation. This approach guarantees comprehensive coverage of the language's syntax, ensuring accurate representation.

Next, we will address ambiguity within the grammar, ensuring each sentence possesses a singular interpretation.

**M2**
S -> S Punct | S Conj E | E 
E -> MC | NP | VP | SS 
MC -> NP VP
SS -> SC Punct VP NP
SC -> Conj NP VP
PP -> P NP
NP -> NP Punct SimpleNP | NP PP | SimpleNP
SimpleNP -> N | DetN | Pron | Det N | Pron N | Det AdjE N 
VP -> VP Punct SimpleVP | SimpleVP
SimpleVP -> V | V NP | V AdvE | V NP AdvE | V PP 
AdjE -> AdjE Conj SimpleAdj | SimpleAdj
SimpleAdj -> Adj
AdvE -> AdvE Conj SimpleAdv | SimpleAdv
SimpleAdv -> Adv

Ambiguity in a grammar emerges when a sentence can be derived through multiple sequences of production rules, leading to parsing complexities and varying interpretations of the same input.

Lastly, we will confront left recursion, a common hurdle in parsing algorithms, to streamline the parsing process.

**M3**
 S -> E S'
 S' -> Punct S' | Conj E S' | ε
 E -> MC | NP | VP | SS 
 MC -> NP VP
 SS -> SC Punct VP N PP
 SC -> Conj NP VP
 PP -> P NP
 NP -> SimpleNP NP'
 NP' -> P NP NP' | Punct SimpleNP NP' | ε
 SimpleNP -> N | DetN | Pron | Det N | Pron N | Det AdjE N 
 VP -> SimpleVP VP'
 VP' -> Punct SimpleVP VP' | ε
 SimpleVP -> V | V NP | V AdvE | V NP AdvE | V PP 
 AdjE -> SimpleAdj AdjE'
 AdjE' -> Conj SimpleAdj AdjE' | ε
 SimpleAdj -> Adj
 AdvE -> SimpleAdv AdvE'
 AdvE' -> Conj SimpleAdv AdvE' | ε
 SimpleAdv -> Adv

Left recursion occurs when a non-terminal symbol directly or indirectly produces a string beginning with itself. This phenomenon poses risks of algorithmic inefficiencies, including infinite loops and poor parsing efficacy.
