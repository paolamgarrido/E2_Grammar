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
