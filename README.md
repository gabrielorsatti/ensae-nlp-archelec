# Thematic Evolution of French Electoral Manifestos (1981–1993)

**ENSAE Paris — Machine Learning for NLP (2025–2026)**

*Gabriel Orsatti*

---

## Summary

This project applies Natural Language Processing techniques to the **Archelec corpus**, a collection of over 12,000 electoral manifestos (*professions de foi*) from French legislative elections in 1981, 1988, and 1993. Using topic modeling (LDA, NMF), zero-shot classification (BERT), and dimensionality reduction (t-SNE), we analyze how political discourse evolved across three pivotal elections of the French Fifth Republic, from Mitterrand's rise to power, through the cohabitation era, to the return of the right.

The central question is: **do candidates' thematic priorities reflect their party affiliation, their socio-professional background, or the economic reality of their constituency?**

## Dataset

The data comes from two sources:

- **Transcriptions**: OCR-processed text of electoral manifestos, extracted from the [Arkindex platform](https://demo.arkindex.org/browse/1bc39ca6-399b-47ca-9de1-ab2ef481cabb) via the [Teklia GitLab repository](https://gitlab.teklia.com/ckermorvant/arkindex_archelec). The corpus covers three legislative elections (1981, 1988, 1993) totaling **12,746 documents**.
- **Metadata**: A CSV file downloaded from [archelec.sciencespo.fr](https://archelec.sciencespo.fr/explorer) containing **33,030 entries** with 42 columns including candidate name, party affiliation (`titulaire-soutien`), profession, age, gender, department, and constituency.

After joining transcriptions with metadata, the working dataset contains 12,746 rows and 52 columns. Key variables include:

| Variable | Description | Coverage |
|---|---|---|
| `text` | Raw OCR transcription of the manifesto | 100% |
| `titulaire-soutien` | Party support / endorsement | 76% explicit |
| `titulaire-profession` | Candidate's declared profession | ~99% |
| `titulaire-sexe` | Gender (homme / femme / non déterminé) | 100% |
| `titulaire-age-tranche` | Age bracket | 37% |
| `departement-nom` | Department name | ~98% |

## Methodology

The project follows a multi-stage pipeline:

**1. Data collection and preprocessing** (`01_data_loading.ipynb`)
- CSV parsing, ZIP extraction, text-metadata join, and initial DataFrame construction.

**2. Exploratory data analysis** (`02_exploration.ipynb`)
- Descriptive statistics, party distribution, gender analysis, profession classification using a BERT-based zero-shot classifier (`joeddav/xlm-roberta-large-xnli`) to map 2,000+ raw professions into ~15 PCS categories (inspired by INSEE's socio-professional classification).

**3. Topic modeling** (`03_topic_modelling.ipynb`)
- Two rounds of modeling:
  - *Round 1*: Standard LDA on the full vocabulary → captures partisan identities rather than themes.
  - *Round 2*: Improved LDA and NMF after removing partisan vocabulary (party names, slogans, electoral jargon) → extracts genuine policy themes (economy, immigration, environment, social policy, etc.).
  - Comparison of LDA vs. NMF, optimal topic count selection via perplexity analysis, and t-SNE projections of the thematic space.

....


## Repository Structure

```
ensae-nlp-archelec/
├── README.md
├── .gitignore
├── requirements.txt
├── notebooks/
│   ├── 01_data_loading.ipynb
│   ├── 02_exploration.ipynb
│   ├── 03_topic_modelling.ipynb
│   
├── data/
│   └── README.md              # Instructions to download the data
├── report/
│   └── rapport.pdf            # Final report (NeurIPS format)
└── src/
    └── utils.py               # Shared utility functions
```

> **Note**: Data files (`.pkl`, `.zip`, `.csv`) are excluded from the repository due to size constraints. See `data/README.md` for download instructions.

## Key Results

*To be completed.*

<!--
Placeholder for results such as:
- Which themes dominate each party's discourse?
- How did the thematic landscape shift from 1981 to 1993?
- Do candidates' professions predict their thematic focus?
- Does local economic reality shape local political discourse?
-->

## How to Reproduce

1. Clone this repository
2. Download the data files (see `data/README.md`)
3. Install dependencies: `pip install -r requirements.txt`
4. Run the notebooks in order (01 → 06)

## References

- Gaultier-Voituriez, O. *Archelec, les archives électorales françaises de la Ve République, du papier au numérique : reflet fidèle ou distorsion ?*
- [Fonds Archives électorales — Sciences Po](https://archelec.sciencespo.fr/)
- [Arkindex platform — Teklia](https://demo.arkindex.org/)
- Blei, D. M., Ng, A. Y., & Jordan, M. I. (2003). Latent Dirichlet Allocation. *JMLR*.
- Devlin, J., et al. (2019). BERT: Pre-training of Deep Bidirectional Transformers. *NAACL*.

## License

ENSAE Paris, ML for NLP course, 2025–2026.
