# [cite_start]Deep Learning for Natural Language Processing [cite: 76]

## [cite_start]2. Vector representation for NLP [cite: 77]
* [cite_start]**Auteur** : Christopher Kermorvant [cite: 78]
* [cite_start]**Institution** : ENSAE [cite: 79]
* [cite_start]**Année** : 2026 [cite: 80]

---

## [cite_start]Slides and projects [cite: 81]
* [cite_start]Lien vers les ressources : [https://tinyurl.com/ensae2026](https://tinyurl.com/ensae2026) [cite: 82]

---

## [cite_start]Why is a vector representation needed? [cite: 83]
1. [cite_start]La plupart des algorithmes de Machine Learning prennent des vecteurs (de taille fixe) en entrée[cite: 84, 85].
2. [cite_start]La distance de chaîne (string distance) ne définit pas un espace sémantique[cite: 86].
    * [cite_start]Exemple : "chevaux" est plus proche graphiquement de "cheveux" ($d=1$) [cite: 87, 89, 133] [cite_start]que de "cheval" ($d=2$)[cite: 88, 90, 133]. Or, sémantiquement, "chevaux" devrait être proche de "cheval".

### [cite_start]Description du schéma : scikit-learn algorithm cheat-sheet [cite: 113, 114]
[cite_start]Le schéma présente un arbre de décision pour choisir un algorithme de machine learning[cite: 83]:
* [cite_start]**Start** [cite: 112] [cite_start]: Si l'on a plus de 50 échantillons, on continue[cite: 97].
* [cite_start]**Classification** [cite: 91] [cite_start]: Utilisée si l'on prédit une catégorie [cite: 102] [cite_start]et que les données sont étiquetées[cite: 104]. [cite_start]Algorithmes cités : Linear SVC [cite: 101][cite_start], KNeighbors Classifier [cite: 94][cite_start], SVC [cite: 93][cite_start], Ensemble Classifiers[cite: 93].
* [cite_start]**Clustering** [cite: 109] [cite_start]: Utilisé si l'on prédit une catégorie sans données étiquetées[cite: 104]. [cite_start]Algorithmes cités : KMeans [cite: 105][cite_start], Spectral Clustering [cite: 103][cite_start], GMM[cite: 106].
* [cite_start]**Regression** [cite: 115] [cite_start]: Utilisée si l'on prédit une quantité[cite: 108]. [cite_start]Algorithmes cités : SGD Regressor [cite: 118][cite_start], Lasso [cite: 116][cite_start], ElasticNet [cite: 116][cite_start], RidgeRegression [cite: 121][cite_start], SVR [cite: 117][cite_start], Ensemble Regressors[cite: 117].
* [cite_start]**Dimensionality reduction** [cite: 137] [cite_start]: Utilisée pour visualiser ou réduire les dimensions[cite: 137]. [cite_start]Algorithmes cités : Randomized PCA [cite: 122][cite_start], Isomap [cite: 136][cite_start], Spectral Embedding [cite: 136][cite_start], LLE[cite: 137].

---

## [cite_start]Outline [cite: 139]
1. [cite_start]Comment représenter des documents par des vecteurs ? [cite: 140]
2. [cite_start]Comment représenter des mots par des vecteurs ? [cite: 141]
3. [cite_start]Comment apprendre une représentation vectorielle des mots ? [cite: 142]

---

## [cite_start]How to transform a text into a vector? [cite: 143]
* [cite_start]**Idée de base** : Chaque mot (chaîne de caractères) est une dimension dans un espace multidimensionnel[cite: 144].
    1. [cite_start]Sélectionner le nombre de mots : correspond au nombre de dimensions[cite: 145].
    2. [cite_start]Définir une valeur pour chaque coordonnée[cite: 146].
* [cite_start]Cela mène à la représentation **Bag of words** (Sac de mots)[cite: 147].

---

## [cite_start]Bag of word representation [cite: 206]
### [cite_start]Description du schéma [cite: 148]
L'image montre un sac rempli de mots extraits d'un texte de critique de film. Un texte source est transformé en un vecteur de comptage.
* [cite_start]**Texte exemple** : "I love this movie! It's sweet, but with satirical humor. The dialogue is great and the adventure scenes are fun... It manages to be whimsical and romantic while laughing at the conventions of the fairy tale genre. I would recommend it to just about anyone. I've seen it several times, and I'm always happy to see it again whenever I have a friend who hasn't seen it yet!" [cite: 153, 154, 155]
* **Exemples de comptages extraits** :
    * [cite_start]it : 6 [cite: 149, 150]
    * [cite_start]the : 4 [cite: 164, 170]
    * [cite_start]to : 3 [cite: 171, 172]
    * [cite_start]and : 3 [cite: 173, 174]
    * [cite_start]seen : 2 [cite: 175, 176]
    * [cite_start]yet : 1 [cite: 177, 178]
* [cite_start]**Propriété** : La taille du vecteur est fixe une fois le vocabulaire défini[cite: 184].

---

## [cite_start]Bag of word: how to select the dimensions? [cite: 207]
1. [cite_start]Normaliser les formes de mots par lemmatisation ou racinisation (stemming)[cite: 208].
2. [cite_start]Supprimer les mots non informatifs[cite: 209]:
    * a. [cite_start]Par étiquetage morphosyntaxique (POS tagging)[cite: 210].
    * b. [cite_start]Avec une liste de mots vides (stop words)[cite: 211].
    * c. [cite_start]Avec une liste de mots personnalisée[cite: 212].
3. [cite_start]Choisir un nombre de mots[cite: 213].
* [cite_start]**En pratique** : La normalisation et la suppression des mots vides ont très peu d'influence[cite: 221]. [cite_start]Le seul paramètre réellement crucial est la taille du vecteur (10k est une valeur commune)[cite: 221].

---

## [cite_start]Bag of word : how to compute the coordinates? [cite: 222]
### [cite_start]Représentation TF-IDF [cite: 223]
* [cite_start]**Term Frequency (TF)** : Importance (fréquence) d'un terme dans un document[cite: 224].
    * [cite_start]$$tf(t,d)=\frac{f_{t,d}}{\sum_{t^{\prime}\in d}f_{t^{\prime},d}}$$ [cite: 226]
    * [cite_start]Où $t$ est le terme dans le document $d$[cite: 227].
* [cite_start]**Inverse Document Frequency (IDF)** : Spécificité d'un terme dans une collection de documents[cite: 225].
    * [cite_start]$$idf(t,D)=log\frac{N}{|\{d:d\in D~and~t\in d\}|}$$ [cite: 228]
    * [cite_start]$N$ : nombre total de documents dans le corpus[cite: 229].
    * [cite_start]Dénominateur : nombre de documents dans lesquels le terme $t$ apparaît[cite: 230].

---

## [cite_start]TF-IDF: how to use it [cite: 231, 232]
* [cite_start]Pas de réelle justification théorique mais fonctionne bien en pratique[cite: 233].
* [cite_start]Un ensemble d'entraînement est nécessaire pour calculer l'IDF[cite: 234].
* [cite_start]La représentation doit être évaluée sur un ensemble de test indépendant pour éviter le **Data leakage**[cite: 235].
    * [cite_start]**Data leakage** : utiliser des informations du test durant l'entraînement, ce qui mène à une surestimation des performances du modèle[cite: 236].

---

## [cite_start]TF-IDF: weightings [cite: 237, 238]
[cite_start]Des variantes existent, mais le TF*IDF standard est le plus utilisé[cite: 240].

| [cite_start]Weighting scheme [cite: 241] | [cite_start]TF weight [cite: 241] |
| :--- | :--- |
| binary | 0, 1 |
| raw count | $f_{t,d}$ |
| term frequency | $f_{t,d}/\sum_{t^{\prime}\in d}f_{t^{\prime},d}$ |
| log normalization | $log(1+f_{t,d})$ |

| [cite_start]Weighting scheme [cite: 242] | [cite_start]IDF weight $(n_{t}=|\{d\in D:t\in d\}|)$ [cite: 242] |
| :--- | :--- |
| unary | 1 |
| inverse document frequency | $log\frac{N}{n_{t}}=-log\frac{n_{t}}{N}$ |
| inverse document frequency smooth | $log(\frac{N}{1+n_{t}})+1$ |

---

## [cite_start]TF-IDF: in practice [cite: 243, 244]
* [cite_start]Baseline simple et robuste pour la classification de documents[cite: 245]. [cite_start]Les vecteurs sont généralement plus grands que d'autres types d'embeddings mais ils sont creux (sparse)[cite: 245].
* [cite_start]Utilisé dans les moteurs de recherche (Elasticsearch, Solr) pour la similarité requête/document[cite: 246].
* [cite_start]Ne peut pas être utilisé pour des tâches au niveau du mot/token (ex: reconnaissance d'entités nommées ou détection d'événements)[cite: 247].

---

## [cite_start]How to represent words with vectors? [cite: 248]
[cite_start]Avec une représentation Bag-of-Words[cite: 249]:
* [cite_start]"The **altitude** of Mont Blanc is 4810 meters" [cite: 250]
* [cite_start]"The **height** of Mont Blanc is 4810 meters" [cite: 251]
* [cite_start]Problème : La Distance (altitude, height) est égale à la Distance (altitude, cat)[cite: 252]. [cite_start]Il n'y a aucune prise en compte de la proximité sémantique[cite: 253].

---

## [cite_start]How do you learn the meaning of words? [cite: 254]
1. [cite_start]Approches par dictionnaires, ontologies[cite: 255].
2. [cite_start]Approches par corpus[cite: 256].
    * [cite_start]**John Rupert Firth (1957)** : "You shall know a word by the company it keeps!"[cite: 257].
    * [cite_start]**Hypothèse distributionnelle** : Apprendre le sens d'un mot à travers ses contextes d'utilisation[cite: 258].

---

## [cite_start]What is a Tesgüino? [cite: 260, 264]
Est-ce : 1. Un lac finlandais ? 2. Une boisson mexicaine ? 3. [cite_start]Un manga japonais ?[cite: 261, 262, 263].

Exemples de contextes :
* [cite_start]Tesgüino vient de la Sierra Madre au Mexique[cite: 265, 266].
* [cite_start]Le Tesgüino est fait à partir de maïs[cite: 267].
* [cite_start]Il y a une bouteille de tesgüino sur la table[cite: 268].
* [cite_start]Boire du tesgüino peut vous rendre ivre[cite: 269].
* [cite_start]**Conclusion** : Le contexte définit le sens (ici, une boisson alcoolisée à base de maïs)[cite: 270, 271].

---

## [cite_start]Term-Document Matrix [cite: 273]
Représentation des mots par les documents dans lesquels ils apparaissent.

| [cite_start]Mot [cite: 274] | c1 | c2 | c3 | c4 | c5 | m1 | m2 | m3 | m4 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| human | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| interface | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| computer | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| user | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 |
| system | 0 | 1 | 1 | 2 | 0 | 0 | 0 | 0 | 0 |
| response | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| time | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| trees | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 |
| graph | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 |
| minors | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |

[cite_start]*(Source : Deerwester et al., 1990 - Indexing by Latent Semantic Analysis)[cite: 292].*

---

## [cite_start]Latent Semantic Indexing (LSI) [cite: 294]
* [cite_start]**Limitation** : Il faudrait énormément de documents pour représenter correctement les mots[cite: 295, 296].
* [cite_start]Si "Human" et "User" ne partagent pas de contexte (document), leur distance vectorielle sera élevée même s'ils sont sémantiquement proches[cite: 298, 299].

---

## [cite_start]Latent space [cite: 300, 308]
* [cite_start]**Intuition** : En réalité, les échantillons n'occupent pas tout l'espace de manière uniforme[cite: 301].
* [cite_start]Les points peuvent être représentés en 3 dimensions [cite: 306][cite_start], mais être disposés sur un sous-espace de dimension 2[cite: 307, 313].

### [cite_start]Description du schéma [cite: 302, 303, 304, 305, 309, 310, 311, 312]
Le schéma montre une "S-curve" :
1. **Figure a & b** : Des points colorés formant une surface en S dans un espace 3D.
2. **Figure c** : La même surface "déroulée" en 2D (espace latent).
* [cite_start]On peut préserver les relations entre les points tout en réduisant la dimension de l'espace de représentation[cite: 314].

---

## [cite_start]Principal Component Analysis (PCA) [cite: 315]
### [cite_start]Description du schéma [cite: 317, 328]
1. [cite_start]**Original data space** [cite: 317] [cite_start]: Des points (gènes 1, 2, 3) répartis en 3D autour d'un plan[cite: 324, 323, 316]. [cite_start]Les axes PC 1 [cite: 326] [cite_start]et PC 2 [cite: 318] sont identifiés comme les directions de variance maximale.
2. [cite_start]**Component space** [cite: 328] [cite_start]: Les données sont projetées sur les deux dimensions principales (PC 1 vs PC 2)[cite: 329, 327].
* [cite_start]**Méthode** : Trouver les axes des composantes principales, sélectionner les composantes, projeter les données[cite: 330, 331, 332].

---

## [cite_start]Singular Value Decomposition (SVD) [cite: 339]
* [cite_start]**Problème** : La matrice terme-document n'est pas carrée[cite: 336, 337, 338].
* [cite_start]**SVD** : Extension de la PCA aux matrices non carrées[cite: 339].
* [cite_start]Décomposition : $$X = T S D^T$$ [cite: 360, 361, 362]
    * [cite_start]$X$ ($t \times d$) : Matrice originale[cite: 347, 354].
    * [cite_start]$T$ ($t \times m$) : Vecteurs propres des termes[cite: 349, 355].
    * [cite_start]$S$ ($m \times m$) : Valeurs singulières (diagonale)[cite: 350, 356].
    * [cite_start]$D$ ($m \times d$) : Vecteurs propres des documents[cite: 358, 359].

---

## [cite_start]Lower-rank approximation [cite: 377]
* [cite_start]On choisit $k < m$ (rang de X, souvent $k \approx 300$)[cite: 379].
* [cite_start]$$\hat{X} = T S D^T$$ [cite: 381, 382, 383, 384, 385]
* [cite_start]**LSA/LSI représente**[cite: 386]:
    * [cite_start]Le sens d'un mot comme une moyenne pondérée du sens des documents où il apparaît[cite: 388].
    * [cite_start]Le sens d'un document comme une moyenne pondérée du sens des mots qu'il contient[cite: 389].

---

## [cite_start]Limitations of LSI [cite: 391]
* [cite_start]Les mots les plus fréquents ont un poids trop important dans la matrice de co-occurrence[cite: 392].
* [cite_start]Difficulté de passage à l'échelle (scaling) si le nombre de mots/documents augmente[cite: 393].
* [cite_start]Ne prend pas en compte l'ordre des mots, la syntaxe, la logique ou la morphologie[cite: 394].
* [cite_start]**Solutions proposées** : Standardisation (Entropy), Pointwise Mutual Information (PPMI)[cite: 395].

---

## [cite_start]GloVe: Global Vectors for Word Representation [cite: 396, 397]
[cite_start]*(Pennington, Socher, Manning - Stanford, 2014)*[cite: 398, 399, 400, 401].
* [cite_start]**Idée** : Prendre en compte les co-occurrences globales des mots[cite: 429].
* [cite_start]**Objectif** : Trouver une représentation vectorielle qui préserve les ratios de fréquence de co-occurrence[cite: 430].
    * [cite_start]$$P_{ij} = P(j|i) = \frac{X_{ij}}{X_i}$$ [cite: 431]

### [cite_start]Probabilités et Ratios [cite: 432]
[cite_start]Exemple avec les mots cibles $k$ liés à "ice" (glace) et "steam" (vapeur)[cite: 433]:

| [cite_start]Target $k$ [cite: 435] | $solid$ | $gas$ | $water$ | $fashion$ |
| :--- | :--- | :--- | :--- | :--- |
| $P(k\|ice)$ | $1.9 \times 10^{-4}$ | $6.6 \times 10^{-5}$ | $3.0 \times 10^{-3}$ | $1.7 \times 10^{-5}$ |
| $P(k\|steam)$ | $2.2 \times 10^{-5}$ | $7.8 \times 10^{-4}$ | $2.2 \times 10^{-3}$ | $1.8 \times 10^{-5}$ |
| **Ratio** | **8.9** | **0.085** | **1.36** | **0.96** |

* [cite_start]Un ratio $\gg 1$ est corrélé avec "ice", un ratio $\ll 1$ est corrélé avec "steam"[cite: 436].

---

## [cite_start]GloVe: Modeling and Training [cite: 437, 438]
* [cite_start]**Forme générale** : $F(w_i, w_j, \tilde{w}_k) = \frac{P_{ik}}{P_{jk}}$[cite: 442].
* [cite_start]En imposant une contrainte d'homéomorphisme [cite: 444] [cite_start]et en choisissant $F = exp$[cite: 447]:
    * [cite_start]$$w_i^T \tilde{w}_k + b_i + \tilde{b}_k = log(X_{ik})$$ [cite: 450]
* [cite_start]**Entraînement** : Minimisation de la fonction de coût $J$ par descente de gradient[cite: 452, 454]:
    * [cite_start]$$J = \sum_{i,j=1}^{V} f(X_{ij}) (w_i^T \tilde{w}_j + b_i + \tilde{b}_j - log X_{ij})^2$$ [cite: 453]
    * [cite_start]$V$ : taille du vocabulaire[cite: 455].
    * [cite_start]$f$ : fonction de pondération[cite: 456].

### [cite_start]Avantages et Inconvénients [cite: 461]
* [cite_start]**+** : Apprentissage sur des corpus massifs (ex: 840 milliards de tokens), bon passage à l'échelle[cite: 463, 464, 465].
* [cite_start]**-** : Nécessite de calculer la matrice de co-occurrence $X_{ij}$ au préalable, vecteurs statiques, pas un modèle génératif[cite: 467, 468, 469].

---

## [cite_start]Word vector learning with neural networks [cite: 470]
### [cite_start]Description du schéma [cite: 471, 472, 473]
Le schéma montre un réseau de neurones simple :
* [cite_start]**Input Layer** [cite: 471] [cite_start]: Un vecteur "Bag-of-word" [cite: 482] [cite_start](ex: "word 2" [cite: 476] est activé à 1 [cite: 477], les autres à 0 [cite: 475, 479, 481]).
* [cite_start]**Hidden Layer** [cite: 472] [cite_start]: Les poids appris forment la représentation vectorielle (embedding)[cite: 487]. [cite_start]Valeurs affichées : 0.12, 0.92, 0.001[cite: 483, 484, 486].
* [cite_start]**Output Layer** [cite: 473] [cite_start]: Prédit le résultat de la tâche[cite: 485].
* [cite_start]**Question** : What is the task?[cite: 488]. Souvent, la tâche est la prédiction du mot suivant.

---

## [cite_start]A Neural Probabilistic Language Model [cite: 489, 490]
[cite_start]*(Bengio, Ducharme, Vincent - 2000)*[cite: 491, 494, 495].
* [cite_start]**Objectif** : Apprendre simultanément une représentation distribuée pour chaque mot et la fonction de probabilité des séquences de mots[cite: 501].
* [cite_start]**Généralisation** : Une séquence jamais vue obtient une probabilité élevée si elle est composée de mots similaires à une séquence déjà vue[cite: 501].
    * [cite_start]Exemple : "The cat is walking in the bedroom" permet de généraliser à "A dog was running in a room"[cite: 520, 521, 522].

### [cite_start]Architecture [cite: 529]
1. [cite_start]Associer à chaque mot un vecteur de caractéristiques réel dans $\mathbb{R}^n$[cite: 526].
2. [cite_start]Exprimer la probabilité jointe en termes de ces vecteurs[cite: 527].
3. [cite_start]Apprendre les vecteurs et les paramètres de la fonction simultanément[cite: 528].
* [cite_start]**Calcul** : Utilisation d'une couche `tanh` [cite: 535] [cite_start]puis une couche `softmax` [cite: 531] [cite_start]pour la sortie[cite: 530].
* [cite_start]**Paramètres** : $V=100\,000$, $D=50$ à 200 (taille embedding), $H=500$ à 1000 (unités cachées)[cite: 545, 546]. [cite_start]L'entraînement de tant de paramètres était problématique à l'époque[cite: 557].

---

## [cite_start]A Unified Architecture for NLP [cite: 558, 559]
[cite_start]*(Collobert, Weston - 2008)*[cite: 564, 565, 569, 570].
* [cite_start]Utilisation d'un réseau de neurones convolutif (CNN) unique pour plusieurs tâches : POS tagging, chunking, NER, rôles sémantiques[cite: 573, 579, 586].
* [cite_start]**Apprentissage multitâche** : Partage de poids entre les tâches[cite: 574, 587].
* [cite_start]Le modèle de langage est appris de manière non supervisée sur Wikipédia[cite: 589].

### [cite_start]Description du schéma : Architecture [cite: 594]
1. [cite_start]**Input Sentence** [cite: 597] [cite_start]: Les mots et leurs caractéristiques[cite: 596].
2. [cite_start]**Lookup Tables** [cite: 601] [cite_start]: Conversion des index en vecteurs d'embeddings[cite: 602, 603].
3. [cite_start]**Convolution Layer** [cite: 611] [cite_start]: Capture les contextes locaux[cite: 612].
4. [cite_start]**Max Over Time** [cite: 613] [cite_start]: Sélection des caractéristiques les plus importantes[cite: 614].
5. [cite_start]**Softmax** [cite: 617] [cite_start]: Classification finale[cite: 618].

---

## [cite_start]Word2Vec [cite: 619, 651]
[cite_start]*(Mikolov et al. - Google, 2013)*[cite: 622, 623, 624, 625, 626, 627, 628, 630, 631].
* [cite_start]**Idée** : Prédire les mots à partir de leur contexte[cite: 652].
* [cite_start]Fenêtre de contexte $c$ autour du mot central $W_t$[cite: 653, 654, 655, 657, 659].
    * [cite_start]Exemple : "The cute cat **jumps** over the lazy dog"[cite: 656, 658, 659].
* [cite_start]**Objectif** : Maximiser $\sum log~p(w_{c}|w_{t})$[cite: 661, 663].
* [cite_start]**Calcul de probabilité** : Softmax sur tout le vocabulaire[cite: 664, 665].
    * [cite_start]$$p(w_{c}|w_{t})=\frac{e^{s(w_{t},w_{c})}}{\sum_{j=1}^{W}e^{s(w_{t},j)}}$$ [cite: 665, 669]

### [cite_start]Negative Sampling [cite: 823]
[cite_start]Le calcul de la somme au dénominateur sur tout le vocabulaire est trop coûteux[cite: 667, 668]. [cite_start]Word2Vec remplace cela par une tâche de classification (le mot est-il dans le contexte ?) en utilisant des exemples négatifs[cite: 670, 673].
* [cite_start]$$Loss=-log(\frac{1}{1+e^{-s(w_{t},w_{c})}})$$ [cite: 671]

---

## [cite_start]Word2Vec: Architectures [cite: 674, 687, 706]
1. [cite_start]**Continuous Bag of Words (CBOW)** [cite: 674, 716] [cite_start]: Prédit le mot actuel à partir des mots du contexte gauche et droit[cite: 685]. [cite_start]L'ordre des mots est perdu (somme des embeddings)[cite: 681, 686, 711].
2. [cite_start]**Skip-Gram** [cite: 687, 717] [cite_start]: Prédit chaque mot du contexte à partir du mot central[cite: 690].

---

## [cite_start]Semantic and geometric relationships in Word2Vec [cite: 841, 880]
[cite_start]Les vecteurs appris encodent explicitement des régularités linguistiques sous forme de translations linéaires[cite: 836, 837].
* [cite_start]**Exemple Pays/Capitale** : $vec("Madrid") - vec("Spain") + vec("France") \approx vec("Paris")$[cite: 838].
* **Analogies** :
    * [cite_start]Homme : Femme :: Roi : Reine[cite: 881, 882, 883, 884].
    * [cite_start]Marcher (walking) : Marché (walked) :: Nager (swimming) : Nagé (swam)[cite: 885, 886, 887, 889, 890].

---

## [cite_start]Word2Vec: Arithmetic and Analogy [cite: 891, 892, 894, 895]
[cite_start]Le modèle peut répondre à des questions par calcul vectoriel[cite: 896]:
* [cite_start]"Czech + currency" $\rightarrow$ koruna[cite: 896].
* [cite_start]"Vietnam + capital" $\rightarrow$ Hanoi[cite: 896].
* [cite_start]"German + airlines" $\rightarrow$ Lufthansa[cite: 896].

### [cite_start]Limitations [cite: 898]
* [cite_start]Pas de représentation pour les mots inconnus (mots rares, fautes d'orthographe, néologismes)[cite: 899].
* [cite_start]Pas de partage de paramètres pour les différentes formes fléchies (ex: mange / mangerai)[cite: 900, 901, 902].

---

## [cite_start]FastText [cite: 903, 933]
[cite_start]*(Bojanowski, Mikolov et al. - Facebook AI, 2013/2017)*[cite: 905, 906, 909].
* [cite_start]**Idée** : Enrichir les vecteurs de mots avec des informations sur les sous-mots (n-grammes de caractères)[cite: 904, 908, 931, 934].
* [cite_start]Chaque mot est représenté comme la somme des représentations de ses n-grammes[cite: 915, 930, 935].
    * [cite_start]Exemple pour le mot `<where>` avec des n-grammes de taille 3[cite: 940, 941]:
        * [cite_start]`<wh`, `whe`, `her`, `ere`, `re>`, plus le mot entier `where`[cite: 947, 948, 949, 950, 951, 952].
* [cite_start]**Avantages** : Permet de calculer des vecteurs pour des mots jamais vus en sommant les n-grammes connus[cite: 916]. [cite_start]Très efficace pour les langues morphologiquement riches[cite: 913, 926].

---

## [cite_start]Document Embeddings [cite: 965]
[cite_start]Comment créer un vecteur pour une phrase ou un document à partir des vecteurs de mots ? [cite: 965]
1. [cite_start]**Moyenne simple** : Faire la moyenne des vecteurs des mots constituants[cite: 977, 978, 979].
2. [cite_start]**Doc2Vec (Paragraph Vector)** [cite: 985, 1013, 1026] [cite_start]: *(Le & Mikolov, 2014)*[cite: 987, 988].
    * [cite_start]Ajout d'un vecteur spécifique au document ($D$) dans l'architecture Word2Vec[cite: 1046].
    * [cite_start]**PV-DM (Distributed Memory)**[cite: 1041]: Le vecteur de document agit comme une mémoire du sujet.
    * [cite_start]**PV-DBOW (Distributed Bag of Words)**[cite: 1045]: Prédit les mots du document à partir du seul vecteur de document.

---

## [cite_start]Word embeddings and CNN [cite: 1049, 1078, 1100]
[cite_start]*(Yoon Kim - 2014)*[cite: 1051, 1052, 1053, 1054].
* [cite_start]Utilisation d'un CNN simple au-dessus de vecteurs Word2Vec pré-entraînés[cite: 1056, 1068, 1069].
* [cite_start]Les filtres de convolution de différentes tailles (ex: 3, 4, 5 mots) permettent de considérer des contextes de tailles variées[cite: 1089, 1090, 1091, 1110, 1113].
* [cite_start]Une couche de **Max-over-time pooling** [cite: 1111] [cite_start]extrait la caractéristique la plus importante de chaque filtre pour représenter la phrase entière[cite: 1071].

---

## [cite_start]Timeline of Trainable Word Vector Representations [cite: 1115]
* [cite_start]**1957** [cite: 1116] [cite_start]: Hypothèse distributionnelle (Firth)[cite: 1140].
* [cite_start]**1990** [cite: 1117] [cite_start]: Latent Semantic Indexing (contexte à partir des documents)[cite: 1123, 1128].
* [cite_start]**2000** [cite: 1118] [cite_start]: Utilisation des réseaux de neurones comme modèle de langage (Bengio)[cite: 1136, 1138, 1139].
* [cite_start]**2008** [cite: 1119] [cite_start]: Entraînement sur plusieurs tâches (Collobert)[cite: 1124, 1126, 1132].
* [cite_start]**2013** [cite: 1120] [cite_start]: Word2Vec (classifieur de mots simple)[cite: 1127, 1133, 1137].
* [cite_start]**2014** [cite: 1121] [cite_start]: FastText (sous-mots et modèles prêts à l'emploi)[cite: 1125, 1129, 1134, 1135].
* [cite_start]**2018** [cite: 1122] [cite_start]: ELMO, BERT (représentations contextuelles)[cite: 1130, 1131].