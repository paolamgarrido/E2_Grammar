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

To implement this solution, we will utilize an LL(1) parser, a top-down parsing technique commonly employed in computational linguistics. The term "LL" signifies "left-to-right, leftmost derivation," denoting the parser's approach of reading input and constructing parse trees. It initiates parsing from the leftmost symbol of the input string and progresses towards the right. The "(1)" indicates that the parser employs a single token of lookahead when making parsing decisions, streamlining the parsing process and obviating the need for backtracking. (GeeksforGeeks, 2023)

It's essential to highlight that this method entails the use of a parsing table (which we will elaborate on later). This table serves to map combinations of non-terminal symbols and lookahead tokens to production rules.

## Models

In the process of implementing a parser for our language, constructing an appropriate grammar serves as the cornerstone of successful parsing. To achieve this goal, we will go through three fundamental construction steps meticulously designed to ensure completeness, clarity, and efficiency in parsing sentences.

First, we will initiate the process by generating a grammar that encapsulates the essence and structure of our language's syntax.

**Grammar Model that Recognizes the Language**

![Grammar Model](https://github.com/paolamgarrido/E2_Grammar/assets/111533069/fb8626b4-0ad3-4eac-968e-90c9c733fde1)
![image](https://github.com/paolamgarrido/E2_Grammar/assets/111533069/d75cbc19-5439-45a2-a9c6-8d60bbb143a4)


During this phase, the basic syntactic units and rules governing sentence formation were identified. We defined non-terminal symbols to represent distinct syntactic categories, alongside sequences of terminal symbols representing words or punctuation. This approach guarantees comprehensive coverage of the language's syntax, ensuring accurate representation.

To further refine our grammar, we must address two critical issues: ambiguity and left recursion.

**Grammar Model with the Elimination of Ambiguity**

![Grammar Model](https://github.com/paolamgarrido/E2_Grammar/assets/111533069/c24b349d-e266-4f8b-9f76-21b2849436fe)
![image](https://github.com/paolamgarrido/E2_Grammar/assets/111533069/e48938d9-838f-4188-9e34-05646ff02dbd)


In accordance with Michael Sipser's discussion on ambiguity in context-free grammars in 'Introduction to the Theory of Computation,' it is evident that ambiguity poses significant challenges in parsing and interpretation. Sipser defines ambiguity as the situation where a grammar generates the same string in several different ways, leading to multiple parse trees and varying interpretations of the input.

In our grammar construction process, ambiguity was eliminated by restructuring production rules and introducing additional constraints that indicated precedence, effectively eliminating the “or” states (Sipser, 2013).

**Grammar Model with No Left Recursion**

![Grammar Model](https://github.com/paolamgarrido/E2_Grammar/assets/111533069/faa7c877-9a37-4c08-9ff8-1588f0c005d5)
![image](https://github.com/paolamgarrido/E2_Grammar/assets/111533069/3fd955eb-b4dd-42fe-a7ef-3b67c4ef20a5)


Left recursion in a grammar occurs when a non-terminal symbol can directly or indirectly produce a string beginning with itself, which can lead to parsing inefficiencies (Sipser, 2013). To overcome this obstacle, we need to revise production rules to eliminate left recursion. In our approach, left recursion was addressed using recursion elimination algorithms, as described by Sipser. Therefore, we substituted the productions presenting left recursions with two new productions. In these new productions, the first element is a terminal symbol followed by an intermediate state represented with ', which can lead to empty derivations "ε".

## Implementation + Testing

Once our three models were complete and our grammar was ready, the implementation of our final model began. We chose to work with the Natural Language Toolkit (NLTK), which provides a suite of libraries and programs for symbolic and statistical natural language processing (NLP) tasks, including tokenization, parsing, classification and semantic reasoning.

It is important to note that during the implementation of our third model, we encountered a couple of issues. NLTK, while robust for many NLP tasks, posed challenges in accommodating our specific grammar representation. Consequently, we needed to adapt our notation to align with NLTK's requirements. This adjustment involved incorporating additional states to represent the new productions generated during the elimination of left recursion while maintaining the original model's concept. Despite these modifications, our grammar remained free from ambiguity and left recursion, ensuring equivalence between the original and adapted model.

**Grammar Model with No Left Recursion Adopted**

![image](https://github.com/paolamgarrido/E2_Grammar/assets/111533069/23c0b5ae-494a-4648-8c3d-2b71154a1d38)
![image](https://github.com/paolamgarrido/E2_Grammar/assets/111533069/f52396fc-3699-4755-9277-0628e3b65868)

To run and test the program you can use the following steps as a guide:
Install Python if you haven't already. You can download it from [python.org](https://www.python.org/downloads/).
Clone this repository to your local machine and navigate to the directory containing the program in your terminal. 
Install NLTK by running the following command: pip install nltk
Then run the program using the command: python grammartest.py 

If you have trouble with the installation of NLTK, feel free to run the program here:
https://colab.research.google.com/drive/1ZPy30tY0SpoJvbVV0WUYNP4oxmeN85Ti?usp=sharing


Upon running the program, the output will display the parsed trees for the input test sentences written in the file, indicating whether they conform to the grammar. Any errors or exceptions will also be shown in the terminal.

Part of the Language Expected Output:

![image](https://github.com/paolamgarrido/E2_Grammar/assets/111533069/6cf466c7-aa08-43ed-b4aa-a739ecb352e2)

Not Part of the Language Expected Output:

![image](https://github.com/paolamgarrido/E2_Grammar/assets/111533069/b3b9eb46-f62d-4efb-bf8a-e43fb2981de6)


## Complexity

The complexity of our program, taking into account the original file where only one sentence is tested, can be considered to have an input sentence length of ‘k’, meaning the time complexity of parsing is O(k^3).

**Inductive Step**:
Now, let's consider an input sentence of length 'k+1', meaning tokenizing this input sentence takes O(k+1) time. The parsing process involves constructing parse trees based on the CFG rules, which has a time complexity of O((k+1)^3) according to our inductive hypothesis. Therefore, the overall time complexity for an input sentence of length 'k+1' is O(k+1) + O((k+1)^3).

Expanded as follows: 

O((k+1)^3):
O((k+1)^3) = O(k^3 + 3k^2 + 3k + 1)

The resulting overall time complexity is approximately: 
O((k+1)^3) ≈ O(k^3)

Thus, by induction, we've shown that the time complexity of parsing an input sentence of length 'n' is O(n^3).

Meanwhile, our test program has an approximate time complexity of O(N * (m + n^3)), where 'N' is the number of input sentences, 'm' is the average length of tokenized sentences, and 'n' is the average length of input sentences (assuming that the grammar remains constant across all parsing operations).

**Different approaches**

Another consideration taken into account for the solution was the construction of a pushdown automaton. However, given the complexity of the grammar and the considerable number of states involved, this approach no longer appeared viable to me. This is primarily due to the fact that the complexity of a pushdown automaton is often assessed in terms of both the number of states and the length of the input string. In this scenario, the time complexity could range from linear to potentially exponential. Considering implementation considerations such as coding efficiency, time constraints, and simplicity, utilizing a library such as NLTK seems to be a more user-friendly and pragmatic option.

## Analysis

In this project, once more we embarked on the implementation of lexical analysis to develop a parser capable of accurately detecting whether input sentences conform to a predefined grammar structure. Our focus language, Danish, posed unique challenges due to its intricate syntax and diverse sentence structures.

The constructed grammar model encapsulated the essence and structure of the Danish language, while also addressing issues of ambiguity and left recursion, in order to ensure clarity and efficiency in parsing sentences. This comprehensive approach culminated in the formation of the LL(1) Parsing Table, a crucial component derived from the meticulous procedures undertaken throughout the project.

TABLA 

The LL(1) Parsing Table serves as tangible evidence of our grammar's classification within the Chomsky Hierarchy Extended Level as a context-free grammar. This classification is attributed to several distinguishing traits:

- **Start Symbol**: The grammar designates 'S' as the start symbol, initiating the derivation of valid sentences.
- **Non-terminal Symbols**: Non-terminal symbols ('S', 'Saux1', 'Saux2', 'E1', 'E2', etc.) represent syntactic structures within the language.
- **Terminal Symbols**: Terminal symbols, including words and punctuation marks, are explicitly defined in the grammar rules.
- **Production Rules**: The grammar counts with a finite set of rules specifying how non-terminal symbols can be expanded into sequences of terminal and/or non-terminal symbols. These rules contribute to the formation of coherent sentences.
- **Parsing Efficiency**: Context-free grammars are efficiently parsable using algorithms such as LL(1). Our grammar demonstrates parsing efficiency through the elimination of ambiguity and left recursion."

Still, its most outstanding trait is its context-free nature. In a context-free grammar, production rules are not dependent on the context surrounding a non-terminal symbol. This means that each sentence structure can be formed with different words when replaced with its corresponding right side, regardless of the symbols surrounding it.


## References
Sipser, M. (2013). Introduction to the Theory of Computation. En SIGACT news (Vol. 3, pp. 106-110). Cengage Learning. http://debracollege.dspaces.org/bitstream/123456789/671/1/Introduction%20to%20the%20Theory%20of%20Computation_2013%20Sipser.pdf

GeeksforGeeks. (2023). Construction of LL(1) Parsing Table. https://www.geeksforgeeks.org/construction-of-ll1-parsing-table/
