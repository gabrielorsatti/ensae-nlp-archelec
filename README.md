# Thematic Evolution of French Electoral Manifestos (1973-1993)

**ENSAE Paris - Machine Learning for NLP (2025–2026)**

*Gabriel Orsatti*

---

## What this project is about

Between 1973 and 1993, France went through one of its most turbulent political sequences: the oil shocks, the end of the *Trente Glorieuses*, the historic rise of the left under Mitterrand, two cohabitations, the implosion of the Communist Party, and the sudden emergence of the Front National. Cutting across all of this was a slow but irreversible transformation of the social landscape, with mass unemployment becoming a structural rather than a cyclical fact of French life.

Electoral manifestos (*professions de foi*) are a uniquely rich trace of this period. Every candidate in every constituency writes one, the text is printed on official paper, and it is deposited in the national archives. Unlike speeches or party platforms, these documents speak directly to local voters because they are personal, constrained in format, and written quickly. They capture something that more polished political texts often lose: the actual vocabulary through which ordinary politicians tried to make sense of their moment.

This project applies Natural Language Processing to the **Archelec corpus**, a collection of 21,697 such manifestos spanning five legislative elections: **1973, 1978, 1981, 1988, and 1993**. Using topic modeling (LDA), zero-shot classification (XLM-RoBERTa), and text classification (Logistic Regression), we trace how political discourse shifted over two decades. 

The central insight of this study is that **ideological differentiation in French politics operates primarily at the vocabulary level, rather than the topic level**: candidates across the spectrum are forced by the electoral agenda to discuss the exact same broad issues, but they frame these realities through ideologically irreconcilable languages.

---

## Why five elections matter

Most existing computational analyses of French political text focus on a single election or a narrow time window. Covering 1973–1993 offers **genuine longitudinal depth**. The five elections in our corpus each carry a distinct political signature:

- **1973**: The last election of the Gaullist era. The *Programme Commun* of the left has just been signed. The discourse is shaped by prosperity and ideological polarization.
- **1978**: The *Union de la Gauche* collapses just before the vote. The manifestos are written under the shadow of a deal falling apart in real time.
- **1981**: Mitterrand wins the presidency two months before the legislative elections. The word *changement* enters the mainstream.
- **1988**: The middle of cohabitation. The RPR and UDF are in reconfiguration; the PS is governing with a minority. The FN is, for the first time, a national force.
- **1993**: A landslide for the right in the context of deep economic crisis. Unemployment crosses 11%. The vocabulary of fear and exclusion proliferates, and a new generation of ecology candidates emerges.

---

## Dataset

The data comes from two sources:

**Transcriptions**: OCR-processed text of electoral manifestos, extracted from the [Arkindex platform](https://demo.arkindex.org/browse/1bc39ca6-399b-47ca-9de1-ab2ef481cabb) via the [Teklia GitLab repository](https://gitlab.teklia.com/ckermorvant/arkindex_archelec). 

**Metadata**: A CSV file downloaded from [archelec.sciencespo.fr](https://archelec.sciencespo.fr/explorer). After joining transcriptions with metadata, the working dataset contains **21,697 documents**. 

| Variable | Description | Coverage |
|---|---|---|
| `text` | Raw OCR transcription of the manifesto (lemmatized via spaCy) | 100% |
| `year` | Election year (1973, 1978, 1981, 1988, 1993) | 100% |
| `titulaire-soutien` | Party support / endorsement (aggregated into 6 macro-families) | ~81% |
| `titulaire-profession` | Candidate's declared profession | ~99% |
| `titulaire-sexe` | Gender (homme / femme) | 100% |

---

## Methodology

The project follows a four-stage pipeline, each handled in its own notebook:

**Stage 1: Data collection and assembly** (`01_data_loading.ipynb`). CSV parsing, ZIP extraction, text–metadata join, and German-language filtering (Alsace-Moselle). 

**Stage 2: Exploratory analysis** (`02_exploration.ipynb`). Descriptive statistics and demographic profiling. To handle the 2,000+ distinct free-text profession entries (*"professeur agrégé"*, *"employé des PTT"*), we mapped them to 15 broad PCS categories using a **Zero-shot Natural Language Inference classifier** (`XLM-RoBERTa`). The model evaluates natural-language hypotheses (e.g., *"Cette personne travaille comme [catégorie]"*) to perfectly recover the sociological recruitment base of each party.

**Stage 3: Topic modeling** (`03_topic_modelling.ipynb`). After removing explicitly partisan stop-words, we compared LDA and NMF models. While NMF yielded higher numerical coherence, it suffered from a pathological concentration (~84.5% of documents in a single background topic) and overfit on micro-niches. We ultimately selected an **LDA model ($k=11$)**, which provided a highly balanced and historically accurate thematic decomposition (capturing class struggle, ecology, immigration, and institutional governance).

**Stage 4: Advanced analyses** (`04_advanced_analysis.ipynb`). 
- **Supervised classification**: Logistic Regression on TF-IDF features to predict party family from text alone (5-fold stratified CV).
- **Semantic mapping**: t-SNE projection of the corpus onto two dimensions, visualizing the ideological geometry of the Fifth Republic.
- **Fighting words**: Log-odds ratio analysis (Monroe et al., 2008) revealing how different parties frame shared themes using Dirichlet priors.
- **Discourse vs. macroeconomic reality**: Correlation analysis between topic frequencies and external INSEE indicators (inflation and unemployment).

---

## Key Results

1. **Differentiation operates at the vocabulary level, not the topic level:** A cross-family cosine similarity matrix reveals that all political families share near-identical topic distributions (similarity ~ 1.0). They all address the exact same broad themes, but do so using entirely different, ideologically charged languages.
2. **Divergent framing of shared realities ("Fighting Words"):** When discussing the exact same issue—unemployment—the radical left frames it as a class war (*travailleurs*, *patronat*), the far-right hijacks the topic through the lens of security (*immigration*, *insécurité*), and the mainstream right uses a managerial register (*entreprise*, *charges*).
3. **The hierarchy of classifiability:** A classifier can predict a candidate's political family from raw text with remarkable accuracy, but performance varies by party type. "Niche" parties (*Gauche radicale*, *Extrême droite*) cultivate highly distinctive, insular vocabularies and are mathematically easy to identify. Conversely, mainstream governing parties (*Centre*, *Droite*) deliberately blur their ideological contours to appeal to the median voter, making their lexicons functionally indistinguishable.
4. **The retreat from macroeconomics:** By overlaying discourse with INSEE data, we found a strong, counter-intuitive **negative correlation ($r = -0.866$)** between national unemployment rates and generic economic discourse. As mass unemployment became an intractable structural reality in the late 1980s, mainstream parties seemingly retreated from grand macroeconomic narratives. Instead, the political debate fragmented and pivoted toward new societal cleavages (immigration and ecology).

---

## Repository structure

```text
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
    └── README.md              

> **Note**: Data files (`.pkl`, `.zip`, `.csv`) are excluded from the repository due to size constraints. See `data/README.md` for download instructions.

---

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
- [Arkindex platform - Teklia](https://demo.arkindex.org/)
- Blei, D. M., Ng, A. Y., & Jordan, M. I. (2003). Latent Dirichlet Allocation. *JMLR*.
- Devlin, J., et al. (2019). BERT: Pre-training of Deep Bidirectional Transformers. *NAACL*.
- Monroe, B. L., Colaresi, M. P., & Quinn, K. M. (2008). Fightin' words: Lexical feature selection and evaluation for identifying the content of political conflict. *Political Analysis*.
- Van der Maaten, L., & Hinton, G. (2008). Visualizing data using t-SNE. *JMLR*.

---

*ENSAE Paris, ML for NLP course, 2025-2026.*
