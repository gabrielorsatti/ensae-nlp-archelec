
Markdown


# Deep Learning for Natural Language Processing
## Named-Entity Recognition
### Christopher Kermorvant
### ENSAE
### 2026

---

# Named-Entity
Text segment referencing a real-world entity
Le president français a été le premier à signer l'accord de Paris sur le climat à l'ONU le 22 avril 2016.
365
Avril 2016

**Description du schéma :** Trois images sont présentées : la Tour Eiffel symbolisant "Paris", une photographie de François Hollande symbolisant le "président français", et le logo des Nations Unies symbolisant "l'ONU".

---

# Information extraction
1. Locating and typing named-entities in text
 NER, Named-Entity Recognition
2. Linking named-entities to reference lists
 NEL, Named-Entity Linking
3. Building and using a graph of information
 Semantic graph, Semantic inference

---

# Named-entities
Francois Hollande -> DBpedia About: François Hollande
An Entity of Type: animal, from Named Graph: http://dbpedia.org, within Data Space: dbpedia.org
President of France from 2012 to 2017

## Type of information extraction
* Named-entities
 * Francois Hollande
* Temporal Expressions
 * from 2012 to 2017
* Events
 * Remporte l'élection présidentielle en 2012

**Description du schéma :** Exemples d'extraction avec des liens vers DBpedia pour "François Hollande" (indiquant la durée 2012-01-01 à 2017-12-31) et l'événement "2012 French presidential election".

---

# History of information extraction
## Message Understanding Conferences (MUC)
* Cycle of 7 evaluation campaigns between 1987 and 1998
* Funded by the DARPA (Defense Advance Research Project Agency)

**Text**
John Simon, Chief Financial Officer of Prime Corp. since 1986, saw his pay jump 20%, to $1.3 million, as the 37-year-old also became the financial-services company's president.
[...]

**Scenario Template**
<TEMPLATE-93-1> : DOC NR: "93"
CONTENT:<SUCCESSION EVENT-93-1>
<SUCCESSION EVENT-93-1> :=
SUCCESSION ORG: <ORGANIZATION-93-1>
POST: "president"
IN AND OUT <IN AND OUT-93-1>
VACANCY REASON: OTH UNK
<IN AND OUT-93-1>: IO PERSON: <PERSON-93-1>
NEW STATUS: IN
ON THE JOB: YES
OTHER ORG: SAME ORG
<ORGANIZATION-93-1> :=
ORG_NAME: "Prime Corp."
ORG_DESCRIPTOR: "the financial-services company"
ORG TYPE: COMPANY
<PERSON-93-1> : PER NAME: "Jhon Simon"

---

# History of information extraction
## Text Analysis Conference (TAC, 2008-2023)
* Analyse text to extraction information about entities
* Enrich a Knowledge Base

Conferences and Evaluations define :
* Tasks
* Standard annotation formats
* Metrics
* Best practices

---

# Task definition: the typology of entities
A typology defines:
* The list of entities
* Their definition
* The annotation rules

---

# Typology of Entities: MUC
* Organization: named corporate, governmental, or other organizational entity
* Person: named person or family
* Location: name of politically or geographically defined location (cities, provinces, countries, international regions, bodies of water, mountains, etc.)
* Date: complete or partial date expression
* Time: complete or partial expression of time of day
* Money: monetary expression
* Percent: percentage

https://aclanthology.org/M98-1028.pdf

---

# Typology of Entities : ACE (2006)
* Person : Person entities are limited to humans. A person may be a single individual or a group.
* Organization : Organization entities are limited to corporations, agencies, and other groups of people defined by an established organizational structure.
* GPE (Geo-political Entity) : GPE entities are geographical regions defined by political and/or social groups. A GPE entity subsumes and does not distinguish between a nation, its region, its government, or its people.
* Location : Location entities are limited to geographical entities such as geographical areas and landmasses, bodies of water, and geological formations.
* Facility : Facility entities are limited to buildings and other permanent man-made structures and real estate improvements.
* Vehicle : A vehicle entity is a physical device primarily designed to move an object from one location to another, by (for example) carrying, pulling, or pushing the transported object.
* Weapon : Weapon entities are limited to physical devices primarily used as instruments for physically harming or destroying other entities.

https://www.ldc.upenn.edu/sites/www.ldc.upenn.edu/files/english-entities-guidelines-v5.6.6.pdf

---

# Hierarchical Typology of Entities : Quaero
Looks more and more like an ontology (WordNet)

**Description du schéma :** Deux graphes heuristiques ou cartes mentales. Le premier montre une arborescence autour du nœud central "entity" se divisant en loc, pers, org, amount, time, prod, avec des sous-catégories complexes (ex: loc -> town, reg, nat, sup, geo, hydro, astro, etc.). Le second schéma est un graphe sémantique illustrant les connexions du mot "cat" avec des synonymes et concepts associés (ex: true cat, CAT, computerized axial tomography, caterpillar, whip, etc.).

---

# Typology of Entities: comparison

| Typology | Example |
| :--- | :--- |
| MUC | d'après le Bureau du recensement des LOC[Etats-Unis], les revenus des ménages ont reculé pour la quatrième année consécutive en DATE[2011]. |
| ACE | d'après le ORG [Bureau du recensement des Etats-Unis], les revenus des ménages ont reculé pour la quatrième année consécutive en DATE[2011]. |
| ESTER | d'après le ORG[Bureau du recensement des LOC[Etats-Unis]], les revenus des ménages ont reculé pour la quatrième année consécutive en DATE[2011]. |
| QUA | d'après le ORG [name [Bureau du recensement] des LOC [ name[Etats-Unis]]], les revenus des ménages ont reculé pour la quatrième année consécutive en DATE[ year[2011]]. |

---

# Annotation formats
## BIO format

| Tags | Description |
| :--- | :--- |
| B-XXX | Beginning of an entity of type XXX |
| I-XXX | Inside (continuation) of an entity of type XXX |
| O | Not an entity |

| Text | Le | président | François | Hollande | a | signé | le | traité | de | Paris |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Ref | O | O | B-PER | I-PER | I-PER | O | O | O | O | B-LOC |

---

# Annotation formats
## BIEOS format

| Tags | Description |
| :--- | :--- |
| B-XXX | Beginning of an entity of type XXX |
| I-XXX | Inside (continuation) of an entity of type XXX |
| E-XXX | End of an entity of type XXX |
| O | Not an entity |
| S-XXX | Single token entity of type XXX |

Also L-XXX
Also U-XXX

| Text | Le | président | François | Hollande | a | signé | le | traité | de | Paris |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Ref | O | O | B-PER | I-PER | E-PER | O | O | O | O | S-LOC |

---

# Nested entities

**Historical source**
Jagou, comm, mont de piété, Condé, 7.
Jazu, dist. Harpe, 121.
Jaguet, étuis à lunett, p. du Caire, 48.

**OCR output**
Jaguet, étuis à lunett, p. du Caire, 48.

**Nested NER output**
Jaguet (PER) , étuis à lunett (ACT) , p. du Caire (LOC) , 48 (CARD)
Le tout sous une entité SPAT et ACT.

| Level | Entity | Description |
| :--- | :--- | :--- |
| 1 | PER | Person(s) or business name. |
| 1 or 2 | ACT | Person or company's activities |
| 1 | DESC | Complete description. |
| 1 | SPAT | Address |
| 2 | TITREH | Military or civil title relative to company's owner |
| 2 | TITREP | Professional rewards |
| 1 | TITRE | Other title. |
| 2 | LOC | Street name |
| 2 | CARDINAL | Street number |
| 2 | FT | Kind of geographic feature |

* Better modelling of the information
* More complex to train
* More complex to evaluate

https://soduco.geohistoricaldata.org
https://hal.science/hal-03994759v1/file/Nested_NER_ICDAR_2023-1.pdf

**Description du schéma :** Un arbre de "NAMED ENTITY" montre la décomposition hiérarchique en sous-entités : PER (vers TITREH), TITRE (vers TITREP), DESC (vers ACT), ACT, SPAT (vers LOC, CARD, FT).

---

# Metrics

**Description du schéma :** Matrice de confusion classique à 4 quadrants croisant les valeurs "Predicted" (Prédictions) et "Actual" (Valeurs Réelles) pour donner : True Positive, False Positive, False Negative, True Negative.

Precision = True Positive / Actual Results
or
Precision = True Positive / (True Positive + False Positive)

Recall = True Positive / Predicted Results
or
Recall = True Positive / (True Positive + False Negative)

$$F1-Score=2\times\frac{Precision\times Recall}{Precision+Recall}$$ (Harmonic mean of P and R)

---

# Metrics
## Match

| Text | Le | président | François | Hollande | a | signé | le | traité | de | Paris |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Ref | O | O | B-PER | I-PER | I-PER | O | O | O | O | B-LOC |
| Pred | O | O | B-PER | I-PER | I-PER | O | O | O | O | B-LOC |

## Deletion

| Text | Le | président | François | Hollande | a | signé | le | traité | de | Paris |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Ref | O | O | B-PER | I-PER | I-PER | O | O | O | O | B-LOC |
| Pred | O | O | O | O | O | O | O | O | O | B-LOC |

---

# Metrics (simple version)
## Insertion

| Text | Le | président | François | Hollande | a | signé | le | traité | de | Paris |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Ref | O | O | B-PER | I-PER | I-PER | O | O | O | O | B-LOC |
| Pred | O | B-PER | I-PER | I-PER | I-PER | O | O | O | B-PER | B-LOC |

Metrics: Precision, Recall, F1
$$P=\frac{TP}{TP+FP}$$
$$R=\frac{TP}{TP+FN}$$
$$F_{1}=2\cdot\frac{P\cdot R}{P+R}$$

---

# Metrics (complex version)
## Wrong type

| Text | Le | président | François | Hollande | a | signé | le | traité | de | Paris |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Ref | O | O | B-PER | I-PER | I-PER | O | O | O | O | B-LOC |
| Pred | O | O | B-PER | I-PER | I-PER | O | O | O | O | B-PER |

## Wrong boundaries

| Text | Le | président | François | Hollande | a | signé | le | traité | de | Paris |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Ref | O | O | B-PER | I-PER | I-PER | O | O | O | O | B-LOC |
| Pred | O | O | O | I-PER | I-PER | O | O | O | O | B-LOC |

---

# Metrics (complex version)
## Wrong type + wrong boundaries

| Text | Le | président | François | Hollande | a | signé | le | traité | de | Paris |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Ref | O | O | B-PER | I-PER | I-PER | O | O | O | O | B-LOC |
| Pred | O | O | O | O | B-LOC | O | O | O | O | B-LOC |

---

# Metrics (complex version)
## Error types

| Error type | Explanation |
| :--- | :--- |
| Correct (COR) | both are the same |
| Incorrect (INC) | the output of a system and the golden annotation don't match |
| Partial (PAR) | system and the golden annotation are somewhat "similar" but not the same |
| Missing (MIS) | a golden annotation is not captured by a system |
| Spurious (SPU) | system produces a response which doesn't exist in the golden annotation |

## Evaluation types

| Evaluation schema | Explanation |
| :--- | :--- |
| Strict | exact boundary surface string match and entity type |
| Exact | exact boundary match over the surface string, regardless of the type |
| Partial | partial boundary match over the surface string, regardless of the type |
| Type | some overlap between the system tagged entity and the gold annotation is required |

nervaluate 1.1.0
```python
pip install nervaluate
print(evaluator.summary_report())


https://pypi.org/project/nervaluate/
Scenario: all


incorrect
correct
partial
missed
spurious
precision
recall
ent_type
0
5
0
0
0
1.00
1.00
exact
2
3
0
0
0
0.40
0.40
partial
0
2
3
0
0
0.40
0.40
strict
2
3
0
0
0
0.40
0.40

Metrics (more complex version)
Transcription errors (OCR)
Text
Le
président
François
Hollande
a
signé
le
traité de
Paris
Ref
O
O
B-PER
I-PER
I-PER
O
O
O
O
Reco
Le
résident
François
Marmande
a
signé
le
traité de
Paris
Pred
O
O
O
I-PER
B-LOC
O
O
O
O


$$if \; x_j = x \vee y_k = y \rightarrow FP \; or \; FN$$

$$c(x) \rightarrow entity \; ground-truth$$

$$t(x) \rightarrow text \; ground-truth$$

$$c(y) \rightarrow entity \; prediction$$

$$t(y) \rightarrow text \; prediction$$

$$S_{NERVAL-M}(x_j, y_k) =$$
$$if \; c(x_j) \neq c(y_k) \rightarrow FP \; and \; FN$$
$$otherwise :$$
$$if \; CER(t(x_j), t(y_k)) > M \rightarrow FP \; and \; FN$$
$$if \; CER(t(x_j), t(y_k)) \leq M \rightarrow TP$$

$$P=\frac{TP}{TP+FP}$$

$$R=\frac{TP}{TP+FN}$$

$$F_{1}=2\cdot\frac{P\cdot R}{P+R}$$
Metrics without reading order
Original <title>AUBERT Huissier priseur à Paris <analysis>Contre Baraise <date>10 mars 1773 <serie>X1A <article>4723 <reference>205
Shuffled <article>4723 <title>AUBERT Huissier priseur à Paris <serie>X1A <reference>205 <date>10 mars 1773 <analysis>Contre Baraise
Bag-of-Word (BoW): checks whether predicted word appear in the ground truth and if ground truth words appear in the prediction, regardless of their position.
Bag-of-Tagged-Word (BoTW): checks whether predicted words appear in the ground truth and if ground truth words appear in the prediction, regardless of their position. (O is ignored)
Bag-of-Entities (BoE): checks whether predicted entities appear in the ground truth and if ground truth entities appear in the prediction, regardless of their position.
ie-eval 0.1.0

Python


pip install ie-eval


Reading Order Independent Metrics for Information Extraction in Handwritten Documents https://arxiv.org/pdf/2404.18664
Libraries: spaCy
https://spacy.io/
Support for 75+ languages
84 trained pipelines for 25 languages
Multi-task learning with pretrained transformers like BERT
Pretrained word vectors
State-of-the-art speed
Production-ready training system
Linguistically-motivated tokenization
Components for named entity recognition, part-of-speech tagging, dependency parsing, sentence segmentation, text classification, lemmatization, morphological analysis, entity linking and more
Built in visualizers for syntax and NER
Description du schéma : Capture d'écran du widget de configuration de spaCy montrant les options : Operating system (macOS/OSX, Windows, Linux), Platform (x86, ARM/M1), Package manager (pip, conda, from source), Hardware (CPU, GPU), Configuration (virtual env, train models), Trained pipelines (English sélectionné parmi de nombreuses langues), Select pipeline for (efficiency, accuracy).
Libraries: spaCy
EXPLO
displaCy Named Entity Visualizer
Le président François Hollande a signé pour la France, le 12 décembre 2015 à la convention cadre des Nations Unies, le traité de Paris sur le climat.
Model : French-fr_core_news_sm (v3.5.0)
https://spacy.io/
Entity labels (select all)
PER, ORG, LOC, MISC
Le président François Hollande (PER) a signé pour la France (LOC) le 12 décembre 2015 à la convention cadre des Nations Unies (ORG) le traité de Paris (MISC) sur le climat.
Description du schéma : Capture d'écran de l'interface "displaCy Named Entity Visualizer" mettant en évidence la reconnaissance des entités nommées en couleur directement dans le texte (PER en vert, LOC en orange, ORG en bleu clair, MISC en violet).
Libraries: Stanza
https://stanfordnlp.github.io/stanza/
Native Python implementation requiring minimal efforts to set up;
Full neural network pipeline for robust text analytics, including tokenization, multi-word token (MWT) expansion, lemmatization, part-of-speech (POS) and morphological features tagging, dependency parsing, and named entity recognition;
Pretrained neural models supporting 70 (human) languages;
A stable, officially maintained Python interface to CoreNLP.
Description du schéma : Architecture de la bibliothèque Stanza. "RAW TEXT" (Multilingual: 66 Languages) passe par des "PROCESSORS" (Fully Neural: Language-agnostic) comprenant : Tokenization & Sentence Split (TOKENIZE), Multi-word Token Expansion (MWT), Lemmatization (LEMMA), POS & Morphological Tagging (POS), Dependency Parsing (DEPPARSE), Named Entity Recognition (NER). Le tout génère un "DOCUMENT" sous forme de "Native Python Objects" structuré en Sentence, Word (Lemma, POS, Head, Deprel), et Token.
Libraries: Stanza
Stanza 1.11.0 (updated October 2025)
https://stanfordnlp.github.io/stanza/
Text to annotate:
Le président François Hollande a signé pour la France, le 12 décembre 2015 à la convention cadre des Nations Unies, le traité de Paris sur le climat.
Annotations: parts-of-speech, named entities, lemmas, dependency parse, constituency parse
Language: French
Lemmas:
Le président François Hollande a signé pour la France, le 12 décembre 2015 à la convention cadre de les Nations Unies, le traité de Paris sur le climat.
Named Entity Recognition:
1 Le président François Hollande (PER) a signé pour la France (LOC), le 12 décembre 2015 à la convention cadre de les Nations Unies (ORG), le traité de Paris (MISC) sur le climat.
Universal Dependencies:
Visualisation provided using the brat visualisation/annotation software.
Description du schéma : Interface de démo de Stanza montrant l'analyse complète d'une phrase avec des étiquettes POS, NER, et un arbre complexe de dépendances syntaxiques (Universal Dependencies) affichant les relations (nsubj, obl, amod, etc.) entre chaque token.
Libraries: GLINER2
https://github.com/fastino-ai/GLiNER2/tree/main
GLINER: Pretrained transformer encoder with entity types for zero-shot named entity recognition.
Characteristic
GLINER
GLINER2
Open LLMs
Closed LLMS
Features








Scope
NER only
Various IE & Classification
General
General
Label description
X
✓
✓
✓
CPU Deployment
✓
✓
X
X
Privacy Preserving
✓
✓
✓
X
No API Costs
✓
✓
✓
X
Fine-tuning Support
✓
✓
✓
X
Technical Specifications








Parameters
195M
205M
7B-175B
Unknown
Model Architecture
Encoder
Encoder
Decoder
Decoder
Context Length
512 tokens
2048 tokens
2K-1M tokens
8K-10M tokens
Usage & Licensing








License Type
Apache 2.0
Apache 2.0
Various
Proprietary
Commercial Use
✓
✓
✓
2


Python


text = "Apple Inc. CEO Tim Cook announced new products in Cupertino."
entities = ["company", "person", "location", "product"]
results = extractor.extract_entities(text, entities)

#{'entities': {'company': ['Apple Inc.'],
#              'person': ['Tim Cook'],
#              'location': ['Cupertino']}}

entity_descriptions = {
    "company": "Business organizations and corporations",
    "person": "Names of individuals including executives",
    "location": "Geographical places including cities"
}
results = extractor.extract_entities(text, entity_descriptions)


[Task Prompt [SEP] Input Text]
Libraries: GLINER2
https://github.com/fastino-ai/GLiNER2/tree/main
Entity Recognition

Python


text = "Apple Inc. CEO Tim Cook announced new products in Cupertino."
entities = ["company", "person", "location", "product"]
results = extractor.extract_entities(text, entities)

#{'entities': {'company': ['Apple Inc.'],
#              'person': ['Tim Cook'],
#              'location': ['Cupertino']}}

entity_descriptions = {
    "company": "Business organizations and corporations",
    "person": "Names of individuals including executives",
    "location": "Geographical places including cities"
}
results = extractor.extract_entities(text, entity_descriptions)


Hierarchical Structure Extraction

Python


text = "The new MacBook Pro costs $1999..."
product_schema = {
    "product": [
        "name::str:: Product name and model",
        "price::str:: Product cost",
        "features::list:: Key product features",
        "category:: [electronics|software|hardware]::str"
    ]
}
results = extractor.extract_json(text, product_schema)


Text Classification + Task Composition

Python


text = "This movie was absolutely fantastic! Great acting and plot."
labels = ["positive", "negative", "neutral"]
results = extractor.classify_text(text, {"sentiment": labels})
#{'sentiment': 'positive'}

tasks = {
    "aspects": {
        "labels": ["acting", "plot", "visuals", "music"],
        "multi_label": True,
        "descriptions": {
            "acting": "Quality of character performances",
            "plot": "Story structure and narrative",
            "visuals": "Cinematography and visual effects",
            "music": "Soundtrack and audio design"
        }
    }
}
results = extractor.classify_text(text, tasks)
#{'aspects': ['acting', 'plot']}


Models: NuExtract
https://huggingface.co/numind
NuExtract 2.0 is a family of vLLM models trained specifically for structured information extraction tasks.
It supports both multimodal inputs and is multilingual.
They are fine-tuned from Qwen2.5 models

JSON


{
    "first_name": "verbatim-string",
    "last_name": "verbatim-string",
    "description": "string",
    "age": "integer",
    "gpa": "number",
    "birth_date": "date-time",
    "nationality": ["France", "England", "Japan", "USA", "China"],
    "languages_spoken": [["English", "French", "Japanese", "Mandarin"]]
}

{
    "first_name": "Susan",
    "last_name": "Smith",
    "description": "A student studying computer science.",
    "age": 20,
    "gpa": 3.7,
    "birth_date": "2005-03-01",
    "nationality": "England",
    "languages_spoken": ["English", "French"]
}


Models: LangExtract
https://github.com/google/langextract/tree/main
LangExtract is a Python library that uses LLMs to extract structured information from unstructured text documents based on user-defined instructions.
Precise Source Grounding: Maps every extraction to its exact location in the source text, enabling visual highlighting for easy traceability and verification.
Reliable Structured Outputs: Enforces a consistent output schema based on your few-shot examples, leveraging controlled generation in supported models like Gemini to guarantee robust, structured results.
Models: LangExtract
https://github.com/google/langextract/tree/main

Python


import langextract as lx
import textwrap

#1. Define the prompt and extraction rules
prompt = textwrap.dedent("""\
    Extract characters, emotions, and relationships in order of appearance.
    Use exact text for extractions. Do not paraphrase or overlap entities.
    Provide meaningful attributes for each entity to add context.""")

#2. Provide a high-quality example to guide the model
examples = [
    lx.data.ExampleData(
        text="ROMEO. But soft! What light through yonder window breaks? It is the east, and Juliet is the sun",
        extractions=[
            lx.data.Extraction(
                extraction_class="character",
                extraction_text="ROMEO",
                attributes={"emotional_state": "wonder"}
            ),
            lx.data.Extraction(
                extraction_class="emotion",
                extraction_text="But soft!",
                attributes={"feeling": "gentle awe"}
            ),
            lx.data.Extraction(
                extraction_class="relationship",
                extraction_text="Juliet is the sun",
                attributes={"type": "metaphor"}
            )
        ]
    )
]


Description du schéma : Capture d'écran d'une interface de visualisation (Highlights Legend) montrant le surlignage d'entités extraites (character, emotion, relationship). Une infobulle indique : class: emotion, attributes: {feeling: yearning, character: Lady Juliet} pour le texte "Lady Juliet gazed longingly at the stars, her heart aching for Romeo".
Sources
1. https://github.com/gsdean/ontolearn
2. https://github.com/gsdean/ontolearn
3. https://github.com/gsdean/ontolearn
4. https://github.com/gsdean/ontolearn
5. https://github.com/HECTA-UoM/M3
