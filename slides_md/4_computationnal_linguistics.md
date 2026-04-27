# Deep Learning for Natural Language Processing
## Natural Language Processing in the age of LLMs
**Auteur :** Christopher Kermorvant  
**Institution :** ENSAE  
**Année :** 2026  

---

# Inside NLP, many sub-subfields, with specific models

### Description du schéma
Le schéma illustre l'architecture des sous-domaines de l'intelligence artificielle et du traitement du langage. On y voit des piliers verticaux représentant des grands domaines : `Computer Vision`, `Speech Recognition`, `Robotics`, `Planning`, et `Bio-Informatics`. 
Au centre, le domaine `NLP` (en rouge) repose sur une pile de sous-domaines spécifiques empilés :
- NLP
- Parsing
- Semantics
- Coreference
- ...
- Discourse analysis

Une mention indique : "Specialisation in verticals".

---

# What is computational linguistics?

### Description du schéma
Un diagramme en cercles concentriques illustre les niveaux d'analyse linguistique, du plus bas niveau (au centre) au plus haut niveau de sens (à l'extérieur) :
1. **Phonetics** : speech sounds
2. **Phonology** : phonemes
3. **Morphology** : words
4. **Syntax** : phrases and sentences
5. **Semantics** : literal meaning of phrases and sentences
6. **Pragmatics** : meaning in context of discourse

### Définitions
- **Morphology** : the study of morphemes, or the internal structures of words and how they can be modified
- **Syntax** : the study of how words combine to form grammatical phrases and sentences
- **Semantics** : the study of lexical and grammatical aspects of meaning
- **Pragmatics** : the study of how utterances are used in communicative acts, and the role played by situational context and non-linguistic knowledge in the transmission of meaning

---

# Why so many subfields ?

The research strategy was:
- **Step 1:** Solve computational linguistics
- **Step 2:** develop applications (machine translation, speech recognition, chatbot, etc.)

It seemed obvious that to develop applications based on Natural Language Processing, each of the linguistic levels had to be modelled.

---

# Morphology

## Morphology: lemmatization and stemming
- **Goal:** reduce inflectional forms / derivationally related forms of a word to a common base form

**Exemples :**
- Apple is looking at buying U.K. startup for $ 1 billion
- Apple looked into buying a U.K. startup for $1 billion.
- Apple was looking at buying a startup in the UK for one billion dollars.

All these sentences should be normalized to a common base form.

## Stemming
- **Stemming:** reduce inflectional forms / derivationally related forms of a word to their word stem
- **Word stem:** part of a word responsible for its lexical meaning. Not necessarily an existing word
- Usually : crude heuristic process that chops off the ends of words

**Exemple d'application du Stemming :**
- **Phrase originale :** Apple is looking at buying U.K. startup for $ 1 billion
- **Résultat :** appl is look at buy u.k. startup for $ 1 billion

### Example of a stemming rule for English (Snowball)
```python
define Step_3 as (
    [substring] R1 among (
        'tional' (<- 'tion')
        'ational' (<- 'ate')
        'alize' (<-'al')
        'icate' 'iciti' 'ical' (<-'ic')
        'ful' 'ness' (delete)
    )
    'ative' (R2 delete) // 'R2' added Dec 2001
)
```

## Lemmatization
- **Lemmatization :** reduce inflectional forms / derivationally related forms of a word to their word lemma
- **Lemma:** the canonical form, dictionary form, or citation form of a set of word forms.
- Based on a full morphological analysis

**Exemple d'application de la Lemmatization :**
- **Phrase originale :** Apple is looking at buying U.K. startup for $ 1 billion
- **Résultat (via spaCy) :** Apple be look at buy U.K. startup for $ 1 billion

### Example of lemmatization rules for English
```json
{
  "verb": [
    ["s", ""],
    ["ies", "y"],
    ["es", "e"],
    ["es", ""],
    ["ed", "e"],
    ["ed", ""],
    ["ing", "e"],
    ["ing", ""]
  ],
  "noun": [
    ["s", ""],
    ["ses", "s"],
    ["ves", "f"],
    ["xes", "x"],
    ["zes", "z"],
    ["ches", "ch"],
    ["shes", "sh"],
    ["men", "man"],
    ["ies", "y"]
  ],
  "adj": [
    ["er", ""],
    ["est", ""],
    ["er", "e"],
    ["est", "e"]
  ]
}
```

## Lemmatization and stemming
- In practice: stemming is a crude and incorrect approximation of lemmatization, but lemmatization takes more time and does not improve the applications
- Stemming improves recall and slightly reduces precision

**Extrait documentaire Elasticsearch :**
> Stemming is the process of reducing a word to its root form. This ensures variants of a word match during a search. For example, walking and walked can be stemmed to the same root word: walk. Once stemmed, an occurrence of either word would match the other in a search. Stemming is used in traditional search engines.

---

# Syntax

## Part-of-speech tagging
**Part-of-speech (POS) tagging:** tagging a word in a text as corresponding to a particular part of speech, based on both its definition and its context.

| TAG | POS | DESCRIPTION |
| :--- | :--- | :--- |
| CC | CONJ | conjunction, coordinating |
| IN | ADP | conjunction, subordinating or preposition |
| JJ | ADJ | adjective |
| JJR | ADJ | adjective, comparative |
| JJS | ADJ | adjective, superlative |
| MD | VERB | verb, modal auxiliary |
| NN | NOUN | noun, singular or mass |
| NNP | PROPN | noun, proper singular |
| NNPS | PROPN | noun, proper plural |
| NNS | NOUN | noun, plural |
| RBR | ADV | adverb, comparative |
| RBS | ADV | adverb, superlative |
| VB | VERB | verb |

- **POS:** simple part-of-speech
- **TAG:** detailed part-of-speech

*In practice: POS tagging is not used as a result, but for other downstream tasks such as named entity recognition and event detection.*

### Exemple de POS Tagging

| TEXT | LEMMA | POS | TAG |
| :--- | :--- | :--- | :--- |
| Apple | apple | PROPN | NNP |
| is | be | AUX | VBZ |
| looking | look | VERB | VBG |
| at | at | ADP | IN |
| buying | buy | VERB | VBG |
| U.K. | u.k. | PROPN | NNP |
| startup | startup | NOUN | NN |
| for | for | ADP | IN |
| $|$ | SYM | $ |
| 1 | 1 | NUM | CD |
| billion | billion | NUM | CD |

## Parsing
**Parsing:** formal analysis of a sentence into a parse tree showing the syntactic relation between each words.

**Formal grammar**
$$S \rightarrow NP \ VP$$
$$NP \rightarrow Det \ Nom \mid PropN$$
$$Nom \rightarrow Adj \ Nom \mid N$$
$$VP \rightarrow V \ Adj \mid V \ NP \mid V \ S \mid V \ NP \ PP$$
$$PP \rightarrow P \ NP$$

### Description du schéma (Parse tree)
Un arbre syntaxique pour la phrase "the dog saw a man in the park".
- Le noeud racine S se divise en NP et VP.
- Le noeud NP contient Det (the) et N (dog).
- Le noeud VP se divise en V (saw), NP et PP.
- Le sous-noeud NP contient Det (a) et N (man).
- Le sous-noeud PP se divise en P (in) et NP (qui contient Det (the) et N (park)).

### Parsing : Ambiguïtés
The parse tree may not be unique.
- **Phrase d'exemple :** "Time flies like an arrow"
- **Deux analyses possibles = deux interprétations** (l'une où "Time" est le sujet et "flies" le verbe, l'autre qui pourrait être un impératif ou utiliser "Time flies" comme un nom composé).

*In practice: parsing is not used in applications.*

---

# Why so many subfields ?
- A multitude of levels of analysis and algorithms
- No generic representation
- Other aspects: multilingualism

### Description du schéma
Un histogramme et un diagramme de Voronoï illustrent les langues les plus parlées et réparties géographiquement dans le monde.
- L'anglais est présent dans 110 pays, l'arabe dans 60, le français dans 51, le chinois dans 33, et l'espagnol dans 31 pays.
- **Citation du graphique :** "The reason why English, French and Spanish are among the world's most widespread languages has its roots in the imperial past of the nations where they originate".
- Le diagramme circulaire de Voronoï montre la proportion de locuteurs natifs : le chinois (1 197 M), l'espagnol (399 M), l'anglais (335 M) occupent les plus grandes surfaces.

---

# Are LLMs NLP killers?

Analyse avec ChatGPT d'une phrase d'actualité : *"Trump Administration to Lay Off Nearly All of U.S. Aid Agency's Staff"*

### 1. Morphology (Word Formation & Structure)
- **Trump Administration** $\rightarrow$ Proper noun, compound noun.
- **to** $\rightarrow$ Particle, marks infinitive verb.
- **Lay Off** $\rightarrow$ Phrasal verb, consisting of verb ("lay") and particle ("off").
- **Nearly** $\rightarrow$ Adverb, modifying "all".
- **All** $\rightarrow$ Determiner/pronoun, indicating the totality.
- **of** $\rightarrow$ Preposition, introduces "U.S. Aid Agency's Staff".
- **U.S.** $\rightarrow$ Abbreviation, proper noun.
- **Aid Agency** $\rightarrow$ Noun phrase, "Aid" as a noun modifying "Agency".
- **'s** $\rightarrow$ Possessive marker, indicating possession by "Agency".
- **Staff** $\rightarrow$ Noun, collective noun referring to employees.

### 2. POS (Part-of-Speech Tagging)

| Word/Phrase | POS Tag | Function |
| :--- | :--- | :--- |
| Trump Administration | Proper Noun | Subject |
| to | Particle | Marks infinitive verb |
| Lay Off | Verb (phrasal) | Main verb |
| Nearly | Adverb | Modifies "all" |
| All | Determiner | Quantifier |
| of | Preposition | Introduces "U.S. Aid Agency's Staff" |
| U.S. | Proper Noun | Modifier of "Aid Agency" |
| Aid Agency | Noun Phrase | Possessive noun |
| 's | Possessive Marker | Indicates possession |
| Staff | Noun | Object |

### 3. Syntax (Sentence Structure & Parsing)
- **Sentence Type:** Declarative.
- **Subject:** "Trump Administration" (a noun phrase).
- **Predicate:** "to lay off nearly all of U.S. Aid Agency's staff" (infinitival construction, indicating future intention).
- **Verb Phrase:** "to lay off nearly all of U.S. Aid Agency's staff."
  - "to lay off" (phrasal verb, infinitive)
  - "nearly all" (quantifier modifying "staff")
  - "of U.S. Aid Agency's staff" (prepositional phrase, complementing "all")
- **Possessive Structure:** "U.S. Aid Agency's staff" (the staff belonging to the agency).

### 4. Semantics (Meaning & Interpretation)
- **Main Meaning:** The Trump administration intends to terminate the employment of nearly all workers of a U.S. aid agency.
- **Agent & Action:** "Trump Administration" (agent) performs the action "lay off" (dismiss workers).
- **Affected Entity:** "Nearly all of U.S. Aid Agency's staff" (receivers of the action).
- **Temporal Aspect:** The infinitive structure ("to lay off") suggests a planned or future action.
- **Quantification:** "Nearly all" implies that the majority, but not necessarily 100%, of the staff will be dismissed.
- **Pragmatics:** The phrase implies a significant workforce reduction, which could suggest political, economic, or policy motivations.

---

# Summary on LLMs capabilities
- **Basic Computational Linguistics Tasks :** Solved
- **Basic Natural Language Processing Tasks :** Solved
  - Named-entity extraction
  - Summarization
  - Translation, etc.

**Named Entities (NER) :**
- **Trump Administration** $\rightarrow$ Organization (Refers to the executive branch under Donald Trump)
- **U.S.** $\rightarrow$ Location (United States)
- **Aid Agency** $\rightarrow$ Organization (Refers to a governmental or non-governmental organization providing aid)

**Italian Translation :**
"L'amministrazione Trump licenzierà quasi tutto il personale dell'agenzia di aiuti degli Stati Uniti."

## Limitations of LLMs :
- No evaluation of the performances
- Ground-truth and evaluation methodology still needed
- No guarantee on formatting
- Control tools required (see Pydantic)
- No guarantee of completeness
- Automatic/manual Quality control required
- No confidence rating

## Still to be solved...
- No evaluation of the bias
- EU AI Act: Open Source LLMs must disclose their training data
- High resource consumption
- Use "just enough" models

---

# NLP Libraries

## spaCy
**Linguistic Features :** POS Tagging, Morphology, Lemmatization, Dependency Parse, Named Entities, Entity Linking, Tokenization, Merging & Splitting, Sentence Segmentation, Mappings & Exceptions, Vectors & Similarity, Language Data.

**Code d'exemple :**
```python
import spacy

nlp = spacy.load("fr_core_news_sm")
doc = nlp("Sophie Adenot doit partir pour l'ISS le 13 février 2026")

for token in doc:
    print(token.text, token.lemma_, token.pos_, sep="\t")
```
**Résultat attendu :**
```text
Sophie    Sophie    PROPN
Adenot    Adenot    PROPN
doit      devoir    VERB
partir    partir    VERB
pour      pour      ADP
l'        le        DET
ISS       ISS       PROPN
le        le        DET
13        13        NUM
février   février   NOUN
2026      2026      NUM
```

## Stanza
**Linguistic Features :** Tokenization & Sentence Segmentation, Multi-Word Token (MWT) Expansion, Part-of-Speech & Morphological Features, Lemmatization, Dependency Parsing, Constituency Parser, Named Entity Recognition, Sentiment Analysis, Language Identification, Coreference.

**Code d'exemple (Analyse lexicale) :**
```python
import stanza

nlp = stanza.Pipeline(lang='fr', processors='tokenize,mwt,pos,lemma')
doc = nlp("Sophie Adenot doit partir pour l'ISS le 13 février 2026")

for sent in doc.sentences:
    for word in sent.words:
        print(f'word: {word.text}\tlemma: {word.lemma}\tupos: {word.upos}\tfeats: {word.feats if word.feats else "_"}')
```

**Code d'exemple (Coréférence) :**
```python
nlp = stanza.Pipeline(lang='fr', processors='tokenize,coref')
doc = nlp("Sophie Adenot doit partir pour l'ISS le 13 février 2026. Elle est la première femme à partir pour cette destination")
print(doc)
```

**Structure JSON de la coréférence (Extrait illustré) :**
```json
{
  "id": 1,
  "text": "Sophie",
  "start_char": 0,
  "end_char": 6,
  "coref_chains": [
    {
      "index": 0,
      "representative_text": "la première femme",
      "is_start": true
    }
  ]
}
```

---

# What does it mean to understand?
- Process is not Understand
- Natural Language Processing is not Natural Language Understanding.

### Description du schéma
Un dessin humoristique (de Larson) en deux cases.
- **En haut ("What we say to dogs") :** un maître gronde son chien en pointant du doigt : "Okay, Ginger! I've had it! You stay out of the garbage! Understand, Ginger? Stay out of the garbage, or else!".
- **En bas ("What they hear") :** ce que le chien comprend réellement du discours de son maître : "blah blah GINGER blah blah blah blah blah blah blah blah GINGER blah blah blah blah blah...".

### Thought Experiment: The Chinese Room
- John is locked in a room; he doesn't know how to speak Chinese.
- He has a catalogue of rules allowing him to write an answer to any question in Chinese.
- From the perspective of an outside Chinese speaker, John understands Chinese.

**Description du schéma**
Un dessin illustrant l'expérience de la "Chambre Chinoise" de John Searle (1980). Un homme est dans une boîte fermée. À gauche, une personne insère une question écrite en symboles chinois via une fente "IN". L'homme à l'intérieur utilise un grand livre de règles pour trouver la correspondance des symboles, sans en comprendre le sens, puis glisse la réponse formée par d'autres symboles dans la fente "OUT" à droite vers une autre personne.

---

# Are LLMs stochastic parrots ?
**Référence au papier de recherche :**
- *"On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?"* - **Auteurs :** Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, Shmargaret Shmitchell.
- **Publié lors de :** FAccT '21 (Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency).