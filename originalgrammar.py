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

# Input sentence to be parsed
sentence = "jeg elsker æbler."

# Tokenize the sentence
tokens = nltk.word_tokenize(sentence)

# Parse the sentence
for tree in parser.parse(tokens):
    tree.pretty_print()