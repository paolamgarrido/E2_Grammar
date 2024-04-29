import nltk
from nltk import CFG
nltk.download('punkt')

# Define a context-free grammar
grammar = CFG.fromstring("""
  S -> Saux1 | Saux2
  Saux1 -> E1 | E2 | E3 | E4 | E5
  E1 -> MC Punct
  E2 -> NP Punct
  E3 -> VP Punct 
  E4 -> SS Punct
  E5 -> MC Conj MC Punct
  Saux2 -> E6 | E7 | E8
  E6 -> NP VP Punct VP Conj VP Punct
  E7 -> NP Punct NP Conj NP VP Punct
  E8 -> NP VP Punct Conj NP VP Punct
  MC -> NP VP
  SS -> SC Punct VP NPaux3
  SC -> Conj NP VP
  PP -> P NP
  AdjE -> Adjaux1 | Adjaux2
  Adjaux1 -> Adj
  Adjaux2 -> Adj Conj Adj 
  AdvE -> Advaux1 | Advaux2
  Advaux1 -> Adv
  Advaux2 -> Adv Conj Adv 
  VP -> SimpleVP
  SimpleVP -> V | V NP | V AdvE | V NP AdvE | V PP | V Punct V
  NP -> NPaux1 | NPaux2 | NPaux3
  NPaux1 -> SimpleNP
  NPaux2 -> SimpleNP Punct SimpleNP
  NPaux3 -> SimpleNP PP
  SimpleNP -> N | DetN | Pron | Det N | Pron N | Det AdjE N 

  Det -> 'den' | 'en'
  Pron -> 'hendes' | 'deres'| 'vi'
  N -> 'jeg' | 'æbler' | 'hund' | 'bil' | 'de' | 'vand' |'ret'| 'datter'|'solskinnet' | 'varmen' | 'tur' | 'hun' | 'han'
  DetN -> 'pigen' | 'parken' | 'stranden' | 'kvinden' | 'solen'
  V -> 'elsker' | 'løber' | 'leger' | 'kører' | 'spiser' | 'drikker' |'danser' | 'taler' | 'griner' | 'nyder' | 'hader' | 'skinner' | 'går' | 'sover'
  Adj -> 'store' | 'røde' | 'lækker' | 'velsmagende'
  Adv -> 'hurtigt' | 'smidigt' |'derinde'
  P -> 'i' | 'til' | 'på' | 'en'
  Conj -> 'og' | 'men' | 'når'
  Punct -> ',' | '.' | '?'

""")

# Create a parser with the defined grammar
parser = nltk.ChartParser(grammar)

# Input sentences to be parsed
original_sentences = [
    # Part of the language
    "Jeg elsker æbler.",
    "Den  store  hund  løber  hurtigt.",
    "Pigen leger i parken.",
    "De kører i den røde bil til stranden.",
    "Jeg spiser æbler og han drikker vand.",
    "De danser, taler og griner.", 
    "Kvinden, hendes datter og deres hund nyder solen på stranden.",
    "Hun elsker solskinnet, men hun hader varmen.",
    "Når solen skinner, går vi en tur.", 
    "Sover han derinde?",
    "En lækker og velsmagende ret.",
    "Han løber hurtigt og smidigt.",
    # Not part of the language
    "Drikker og spiser Jeg.",
    "Jeg elsker æbler",
    "Går en vi tur, når solen skinner.",
    "Han løber hurtigt smidigt.",
    ".",
    "Derinde han sover han?",
    "Kvinden, hendes datter og deres hund nyder solen stranden.",
    "De danser taler og griner.",
    "Jeg æbler spiser og han vand drikker.",
    ".?,",
    "Hendes datter hurtigt.",
    ""
]

# Convert all sentences to lowercase for parsing
sentences_lowercase = [sentence.lower() for sentence in original_sentences]

# Parse each sentence and print the parse tree or "Unable to parse"
for sentence, sentence_lowercase in zip(original_sentences, sentences_lowercase):
    print()
    print("Input Sentence:", sentence)
    tokens = nltk.word_tokenize(sentence_lowercase)  # Tokenize the lowercase sentence
    trees = list(parser.parse(tokens))
    if trees:
        print("LL(1) Parsing:")
        for tree in trees:
            tree.pretty_print()
    else:
        print("Unable to parse")