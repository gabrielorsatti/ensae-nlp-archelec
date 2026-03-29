# Thematic Evolution of French Electoral Manifestos (1973–1993)

**ENSAE Paris - Machine Learning for NLP (2025–2026)**

*Gabriel Orsatti*

---

## What this project is about

Between 1973 and 1993, France went through one of its most turbulent political sequence such as the oil shock and the end of the *Trente Glorieuses*, the rise of the left under Mitterrand, two cohabitations, the implosion of the Communist Party, the sudden emergence of the Front National  and, cutting across all of this, a slow but irreversible transformation of the social landscape, with unemployment becoming a structural rather than a cyclical fact of French life.

Electoral manifestos (*professions de foi*) are a uniquely rich trace of this period. Every candidate in every constituency writes one, the text is printed on official paper, and it is deposited in the national archives. Unlike speeches or party platforms, these documents speak directly to local voters because they are personal, constrained in format, and they had to be written quickly. They capture something that more polished political texts often lose, which is the actual vocabulary through which ordinary politicians tried to make sense of their moment.

This project applies Natural Language Processing to the **Archelec corpus**, a collection of over 20,000 such manifestos spanning five legislative elections: **1973, 1978, 1981, 1988, and 1993**. Using topic modeling (LDA, NMF), zero-shot classification (BERT), and dimensionality reduction (t-SNE), we trace how political discourse shifted over two decades from the optimistic reformism of the early 1970s to the anxious nationalism of the early 1990s.

The central question is: **do candidates' thematic priorities reflect their party affiliation, their socio-professional background, or the economic reality of their constituency?** Or, put more bluntly, when a candidate talks about unemployment, is it because their voters are unemployed, or because their party tells them to?

---

## Why five elections matter

Most existing computational analyses of French political text focus on a single election or a narrow time window. Covering 1973–1993 offers something different: **genuine longitudinal depth**.

The five elections in our corpus each carry a distinct political signature:

- **1973** : The last election of the Gaullist era. Pompidou is still alive; the *Programme Commun* of the left has just been signed. The discourse is shaped by prosperity and by an ideological polarisation that has not yet produced its full effects.
- **1978** : The *Union de la Gauche* collapses just before the vote. The left was expected to win; it doesn't. The manifestos from this election are written under the shadow of a deal falling apart in real time, and the vocabulary reflects it.
- **1981** : Mitterrand wins the presidency two months before the legislative elections. Candidates on the left are writing in a context of historic victory; candidates on the right, in a context of sudden defeat. The word *changement* enters the mainstream.
- **1988** : The middle of cohabitation. Chirac has just lost the presidential election to Mitterrand for the second time. The RPR and UDF are in reconfiguration; the PS is governing with a minority. The FN is, for the first time, a national force.
- **1993** : A landslide for the right in the context of deep economic crisis. Unemployment is above 10%. The vocabulary of fear and exclusion proliferates. A generation of young FN candidates write their first professions de foi.

Having all five elections lets us observe how vocabulary shifts gradually or abruptly and whether the shocks that we know from the historical record actually register in the text at the ground level of thousands of individual candidates.

---

## Dataset

The data comes from two sources:

**Transcriptions** : OCR-processed text of electoral manifestos, extracted from the [Arkindex platform](https://demo.arkindex.org/browse/1bc39ca6-399b-47ca-9de1-ab2ef481cabb) via the [Teklia GitLab repository](https://gitlab.teklia.com/ckermorvant/arkindex_archelec). The corpus spans five legislative elections (1973, 1978, 1981, 1988, 1993) and totals over **20,000 documents**.

**Metadata** : A CSV file downloaded from [archelec.sciencespo.fr](https://archelec.sciencespo.fr/explorer) containing over 40,000 entries with 42 columns including candidate name, party affiliation (`titulaire-soutien`), profession, age, gender, department, and constituency.

After joining transcriptions with metadata, the working dataset contains approximately 20,000 rows and 52 columns. Key variables include:

| Variable | Description | Coverage |
|---|---|---|
| `text` | Raw OCR transcription of the manifesto | 100% |
| `year` | Election year (1973, 1978, 1981, 1988, 1993) | 100% |
| `titulaire-soutien` | Party support / endorsement | ~76% explicit |
| `titulaire-profession` | Candidate's declared profession | ~99% |
| `titulaire-sexe` | Gender (homme / femme / non déterminé) | 100% |
| `titulaire-age-tranche` | Age bracket | ~37% |
| `departement-nom` | Department name | ~98% |

---

## Methodology

The project follows a four-stage pipeline, each handled in its own notebook.

**Stage 1 : Data collection and assembly** (`01_data_loading.ipynb`). CSV parsing, ZIP extraction, text–metadata join, and initial DataFrame construction. Particular attention is paid to matching OCR transcriptions with the correct candidate records across elections with different identifier conventions.

**Stage 2 : Exploratory analysis** (`02_exploration.ipynb`). Descriptive statistics, party distribution across elections, gender evolution, and socio-professional profiling. The profession field is a particular challenge: it contains over 2,000 distinct free-text entries (*"professeur agrégé de lettres"*, *"directeur commercial adjoint"*, and so on). We map these to 15 broad PCS-inspired categories using a **BERT-based zero-shot classifier** (`joeddav/xlm-roberta-large-xnli`), which assigns each profession to a category by evaluating natural-language hypotheses, no labelled training data required. Results are cached so the model runs only once.

**Stage 3 : Topic modeling** (`03_topic_modelling.ipynb`). Two rounds of modeling: a first pass with standard LDA, which largely recovers partisan identities rather than policy themes; then an improved pass using both LDA and NMF after removing partisan vocabulary (party names, slogans, electoral boilerplate). The second pass extracts genuinely thematic structure like economy, employment, immigration, social policy, environment, agriculture, Europe, and more. Optimal topic count is selected through perplexity analysis and manual coherence assessment.

**Stage 4 : Advanced analyses** (`04_advanced_analysis.ipynb`). Four analyses built on top of the topic model:
- **Semantic mapping**: t-SNE projection of the 20,000-document corpus onto two dimensions, coloured by party family and by dominant topic. This makes the thematic geography of the corpus visible at a glance.
- **Fighting words**: Log-odds ratio analysis (Monroe, Colaresi & Quinn, 2008) revealing how different parties frame the same topics, e.g. how the PS and the FN talk about unemployment using entirely different lexicons even when discussing the same economic reality.
- **Discourse vs. economic reality**: Pearson and Spearman correlations between departmental employment-topic frequencies and INSEE unemployment rates for each election year. Does local economic distress actually show up in local campaign rhetoric?
- **Supervised classification**: Logistic Regression on TF-IDF features to predict party family from text alone, with 5-fold stratified cross-validation, confusion matrix, and per-class F1 scores.

---

## Repository structure

```
ensae-nlp-archelec/
├── README.md
├── .gitignore
├── requirements.txt
├── notebooks/
│   ├── 01_data_loading.ipynb
│   ├── 02_exploration.ipynb
│   ├── 03_topic_modelling.ipynb
│   └── 04_advanced_analysis.ipynb
└── data/
    └── README.md              # Instructions to download the data
```

> **Note**: Data files (`.pkl`, `.zip`, `.csv`) are excluded from the repository due to size constraints. See `data/README.md` for download instructions.

---

## Key results

*To be completed as the analysis matures.*

Some questions the project aims to answer:

- Which themes dominate each party's discourse, and how stable are these signatures across five elections?
- Is the vocabulary shift between 1978 and 1981 sharp (a historical rupture) or gradual (an underlying trend)?
- Does the PCF's lexical profile change between 1973 and 1993 as its electoral base collapses?
- Do candidates in high-unemployment *départements* write more about employment and does this relationship strengthen after 1981?
- Can a logistic classifier trained on 1981–1988 manifestos correctly label 1973 and 1978 documents, or has the language changed enough to confuse it?

---

## How to reproduce

1. Clone this repository
2. Download the data files (see `data/README.md`)
3. Install dependencies: `pip install -r requirements.txt`
4. Run the notebooks in order: `01 → 02 → 03 → 04`

The BERT classification step in `02_exploration.ipynb` runs once and caches results to `data/profession_pcs_mapping.json`. On subsequent runs, only professions not yet in the cache are classified, so adding a new election year is fast.

---

## References

- Gaultier-Voituriez, O. *Archelec, les archives électorales françaises de la Ve République, du papier au numérique : reflet fidèle ou distorsion ?*
- [Fonds Archives électorales - Sciences Po](https://archelec.sciencespo.fr/)
- [Arkindex platform — Teklia](https://demo.arkindex.org/)
- Blei, D. M., Ng, A. Y., & Jordan, M. I. (2003). Latent Dirichlet Allocation. *JMLR*.
- Devlin, J., et al. (2019). BERT: Pre-training of Deep Bidirectional Transformers. *NAACL*.
- Monroe, B. L., Colaresi, M. P., & Quinn, K. M. (2008). Fightin' words: Lexical feature selection and evaluation for identifying the content of political conflict. *Political Analysis*.
- Van der Maaten, L., & Hinton, G. (2008). Visualizing data using t-SNE. *JMLR*.

---

*ENSAE Paris, ML for NLP course, 2025–2026.*
