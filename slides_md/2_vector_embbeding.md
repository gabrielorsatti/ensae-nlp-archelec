# Deep Learning for Natural Language Processing

## 2. Représentation vectorielle pour le NLP
* [cite_start]**Auteur** : Christopher Kermorvant [cite: 2284]
* [cite_start]**Institution** : ENSAE [cite: 2285]
* [cite_start]**Année** : 2026 [cite: 2286]

---

## Slides et projets
* [cite_start]**Lien** : [https://tinyurl.com/ensae2026](https://tinyurl.com/ensae2026) [cite: 2288]
* [cite_start]**Description du schéma** : Un QR code est présent sur la slide pour accéder directement au lien des slides et des projets[cite: 2287].

---

## Pourquoi une représentation vectorielle est-elle nécessaire ?
1. [cite_start]La plupart des algorithmes de Machine Learning prennent des vecteurs (de taille fixe) en entrée[cite: 2290, 2291].
2. [cite_start]La distance de chaîne de caractères ne définit pas un espace sémantique[cite: 2292].
    * [cite_start]Exemple : "chevaux" est plus proche de "cheveux" que de "cheval" en distance d'édition[cite: 2339].
    * [cite_start]$d=1$ entre "chevaux" et "cheveux"[cite: 2293, 2295].
    * [cite_start]$d=2$ entre "chevaux" et "cheval"[cite: 2294, 2296].

### Description du schéma : Scikit-learn algorithm cheat-sheet
[cite_start]Le schéma présente un arbre de décision pour choisir le bon estimateur en fonction des données[cite: 2318, 2319, 2320]:
* [cite_start]**Classification** : Si l'on prédit une catégorie et que les données sont étiquetées[cite: 2297, 2310]. (Algorithmes : Linear SVC, Naive Bayes, KNeighbors, etc.) [cite_start][cite: 2307, 2304, 2300].
* [cite_start]**Clustering** : Si l'on prédit une catégorie sans étiquettes[cite: 2315]. (Algorithmes : MeanShift, VBGMM, KMeans, etc.) [cite_start][cite: 2333, 2334, 2311].
* [cite_start]**Régression** : Si l'on prédit une quantité[cite: 2321, 2314]. (Algorithmes : SGD Regressor, Lasso, ElasticNet, etc.) [cite_start][cite: 2324, 2322].
* [cite_start]**Réduction de dimension** : Pour visualiser ou compresser les données[cite: 2343]. (Algorithmes : Randomized PCA, Isomap, etc.) [cite_start][cite: 2328, 2342].

---

## Plan du cours
1. [cite_start]Comment représenter des documents avec des vecteurs ? [cite: 2346]
2. [cite_start]Comment représenter des mots avec des vecteurs ? [cite: 2347]
3. [cite_start]Comment apprendre une représentation vectorielle des mots ? [cite: 2348]

---

## Comment transformer un texte en vecteur ?
* [cite_start]**Idée de base** : Chaque mot (chaîne) est une dimension dans un espace multidimensionnel[cite: 2350].
1. [cite_start]Sélectionner le nombre de mots = le nombre de dimensions[cite: 2351].
2. [cite_start]Définir une valeur pour chaque coordonnée[cite: 2352].
* [cite_start]Il s'agit de la représentation **Bag of Words** (Sac de mots)[cite: 2353].

---

## Représentation Bag of Words (Sac de mots)
### Description du schéma
[cite_start]L'image illustre la transformation d'un texte de critique de film en un sac de mots désordonnés mais comptabilisés[cite: 2354, 2360]:
* [cite_start]**Texte source** : "I love this movie! It's sweet, but with satirical humor..."[cite: 2359].
* [cite_start]**Processus** : Les mots sont extraits et placés dans un "sac"[cite: 2363, 2368].
* [cite_start]**Résultat vectoriel** : On obtient un vecteur de taille fixe où chaque entrée correspond au nombre d'occurrences d'un mot[cite: 2390]:
    * [cite_start]"it" : 6 [cite: 2355, 2356]
    * [cite_start]"the" : 4 [cite: 2370, 2376]
    * [cite_start]"to" : 3 [cite: 2377, 2378]
    * [cite_start]"seen" : 2 [cite: 2381, 2382]
    * [cite_start]"humor" : 1 [cite: 2402, 2403]

---

## Bag of Words : Comment sélectionner les dimensions ?
1. [cite_start]Normaliser les formes des mots avec la lemmatisation ou la racinisation (stemming)[cite: 2414].
2. [cite_start]Supprimer les mots non informatifs[cite: 2415]:
    * a. [cite_start]Avec l'étiquetage POS (Part-of-Speech)[cite: 2416].
    * b. [cite_start]Avec une liste de "stop words" (mots vides)[cite: 2417].
    * c. [cite_start]Avec une liste de mots personnalisée[cite: 2418].
3. [cite_start]Choisir un nombre fixe de mots[cite: 2419].
* [cite_start]**En pratique** : La normalisation et la suppression des stop words ont très peu d'influence[cite: 2427]. [cite_start]Le paramètre principal est la taille du vecteur (10k est une valeur commune)[cite: 2427].

---

## Bag of Words : Comment calculer les coordonnées ?
### Représentation TF-IDF
* [cite_start]**Term Frequency (TF)** : Importance (fréquence) d'un terme dans un document[cite: 2430].
    * [cite_start]$$tf(t,d)=\frac{f_{t,d}}{\sum_{t^{\prime}\in d}f_{t^{\prime},d}}$$ [cite: 2432]
* [cite_start]**Inverse Document Frequency (IDF)** : Spécificité d'un terme dans une collection de documents[cite: 2431].
    * [cite_start]$$idf(t,D)=log\frac{N}{|\{d:d\in D~and~t\in d\}|}$$ [cite: 2434]
    * [cite_start]$N$ : nombre total de documents dans le corpus[cite: 2435].
    * [cite_start]Le dénominateur représente le nombre de documents dans lesquels le terme $t$ apparaît[cite: 2436].

---

## TF-IDF : Comment l'utiliser
* [cite_start]Pas de réelle justification théorique, mais cela fonctionne très bien en pratique[cite: 2439].
* [cite_start]Un ensemble d'entraînement est nécessaire pour calculer l'IDF[cite: 2440].
* [cite_start]**Évaluation** : La représentation doit être évaluée sur un ensemble de test indépendant pour éviter la fuite de données (**Data Leakage**)[cite: 2441].
* **Data Leakage** : Utiliser des informations du test durant l'entraînement. [cite_start]Cela conduit à une surestimation des performances du modèle[cite: 2442].

---

## TF-IDF : Variantes
[cite_start]Il existe des variantes, mais le TF-IDF standard est le plus utilisé[cite: 2446].

### [cite_start]Pondérations TF ($f_{t,d}$) [cite: 2447]
| Schéma de pondération | Poids tf |
| :--- | :--- |
| binaire | $0, 1$ |
| comptage brut | $f_{t,d}$ |
| fréquence du terme | $f_{t,d}/\sum_{t^{\prime}\in d}f_{t^{\prime},d}$ |
| normalisation log | $log(1+f_{t,d})$ |

### [cite_start]Pondérations IDF ($n_{t}$) [cite: 2448]
| Schéma de pondération | Poids idf |
| :--- | :--- |
| unaire | $1$ |
| inverse document frequency | $log\frac{N}{n_{t}}$ |
| inverse document frequency smooth | $log(\frac{N}{1+n_{t}})+1$ |

---

## TF-IDF : En pratique
* [cite_start]Baseline solide et simple pour la classification de documents[cite: 2451].
* [cite_start]Les vecteurs sont généralement plus grands que les autres types d'embeddings, mais ils sont creux (sparse)[cite: 2451].
* [cite_start]Utilisé dans les moteurs de recherche (Elastic Search, Solr) pour la similarité requête/document[cite: 2452].
* [cite_start]**Limitation** : Ne peut pas être utilisé pour des tâches au niveau du mot/token comme la reconnaissance d'entités nommées[cite: 2453].

---

## Comment représenter les mots avec des vecteurs ?
Avec une représentation Bag-of-Words :
* [cite_start]"L'altitude du Mont Blanc est de 4810 mètres" [cite: 2456]
* [cite_start]"La hauteur du Mont Blanc est de 4810 mètres" [cite: 2457]
* [cite_start]Problème : Distance(altitude, hauteur) = Distance(altitude, chat)[cite: 2458].
* [cite_start]**Conclusion** : Aucune considération de la proximité sémantique[cite: 2459].

---

## Comment apprend-on le sens des mots ?
1. [cite_start]Approches par dictionnaires, ontologies[cite: 2461].
2. [cite_start]Approches par corpus[cite: 2462].
* [cite_start]**John Rupert Firth (1957)** : "You shall know a word by the company it keeps!"[cite: 2463].
* [cite_start]Apprendre le sens d'un mot via ses contextes d'utilisation : **Hypothèse distributionnelle**[cite: 2464].

---

## Qu'est-ce qu'un Tesgüino ?
* [cite_start]Est-ce un lac finlandais, une boisson mexicaine ou un manga japonais ? [cite: 2466, 2467, 2468, 2469]
* **Contextes d'utilisation** :
    * [cite_start]Le Tesgüino vient de la Sierra Madre au Mexique[cite: 2471].
    * [cite_start]Le Tesgüino est fait à partir de maïs[cite: 2473].
    * [cite_start]Il y a une bouteille de tesgüino sur la table[cite: 2474].
    * [cite_start]Boire du tesgüino peut rendre ivre[cite: 2475].
* [cite_start]**Conclusion** : Le sens d'un mot est représenté par ses contextes d'utilisation[cite: 2476, 2477].

---

## Matrice Terme-Document
[cite_start]Représentation des mots par les documents dans lesquels ils apparaissent[cite: 2479].

| Mot | c1 | c2 | c3 | c4 | c5 | m1 | m2 | m3 | m4 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| human | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| interface | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| computer | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| user | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 |
| system | 0 | 1 | 1 | 2 | 0 | 0 | 0 | 0 | 0 |
| minors | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |

[cite_start]*(Source : Deerwester et al. 1990, Indexing by Latent Semantic Analysis)*[cite: 2498].

---

## Latent Semantic Indexing (LSI)
* [cite_start]**Limitation** : Il faudrait énormément de documents pour représenter correctement les mots[cite: 2501].
* [cite_start]Problème : "Human" et "User" ne partagent pas de contexte (document) dans l'exemple, donc leur distance est indéterminée alors qu'ils sont proches sémantiquement[cite: 2504, 2505].

---

## Espace Latent
* [cite_start]**Intuition** : En réalité, les échantillons n'occupent pas uniformément tout l'espace[cite: 2507].
* [cite_start]**Description du schéma** : L'image montre une forme en "S" en 3D (Figures A et B) qui peut en fait être dépliée sur un plan en 2D (Figure C) sans perdre les relations entre les points[cite: 2512, 2513, 2519].
* [cite_start]On peut donc préserver les relations tout en réduisant la dimension de l'espace de représentation[cite: 2520].

---

## Analyse en Composantes Principales (PCA)
### Description du schéma
1. [cite_start]**Original data space** : Des points distribués en 3D (axes Gene 1, 2, 3)[cite: 2523, 2530].
2. [cite_start]**PCA** : On identifie les axes PC1 et PC2 qui capturent le maximum de variance[cite: 2532, 2533].
3. [cite_start]**Component space** : Les données sont projetées sur ces nouveaux axes en 2D[cite: 2534].
* [cite_start]**Méthode** : Trouver les axes principaux, sélectionner les composants et projeter les données[cite: 2537, 2538].

---

## SVD : Singular Value Decomposition
* [cite_start]**Problème** : La matrice terme-document n'est pas carrée[cite: 2542, 2544].
* [cite_start]**SVD** : Étend la PCA aux matrices non carrées[cite: 2545].
* [cite_start]**Décomposition** : $$X = T S D^T$$ [cite: 2566]
    * [cite_start]$X$ : matrice terme-document ($t \times d$)[cite: 2560].
    * [cite_start]$T$ : vecteurs propres des termes ($t \times m$)[cite: 2561].
    * [cite_start]$S$ : valeurs singulières ($m \times m$)[cite: 2562].
    * [cite_start]$D$ : vecteurs propres des documents ($m \times d$)[cite: 2565].

---

## LSI : Approximation de rang inférieur
* [cite_start]On utilise $k < m$ (souvent $k \approx 300$)[cite: 2585].
* [cite_start]$$\hat{X} = T S D^T$$ [cite: 2591]
* **LSI représente** :
    * [cite_start]Le sens d'un mot comme une moyenne pondérée du sens des documents où il apparaît[cite: 2594].
    * [cite_start]Le sens d'un document comme une moyenne pondérée du sens des mots qu'il contient[cite: 2595].

---

## Limitations de LSI
* [cite_start]Les mots les plus fréquents ont un poids trop important dans la matrice de co-occurrence[cite: 2598].
* [cite_start]Difficulté de passage à l'échelle si le nombre de mots ou de documents augmente[cite: 2599].
* [cite_start]Ne prend pas en compte l'ordre des mots, ni la syntaxe ou la morphologie[cite: 2600].
* [cite_start]**Solutions** : PPMI (Pointwise Mutual Information) ou standardisation par entropie[cite: 2601].

---

## GloVe : Global Vectors for Word Representation
[cite_start]*(Pennington, Socher, Manning, Stanford, 2014)*[cite: 2603, 2604].
* [cite_start]**Concept** : Combine les avantages de la factorisation de matrice globale et des méthodes à fenêtre de contexte locale[cite: 2611].
* [cite_start]Évalue la structure de l'espace vectoriel par des analogies (ex: "roi est à reine ce qu'homme est à femme")[cite: 2619, 2621].

---

## GloVe : Co-occurrences et Ratios
* [cite_start]**Idée** : Prendre en compte les ratios de fréquences de co-occurrence[cite: 2635, 2636].
* [cite_start]$$P_{ij} = P(j|i) = \frac{X_{ij}}{X_i}$$ [cite: 2637]
* [cite_start]Exemple : Le ratio $P(k|ice) / P(k|steam)$ est très grand pour $k=solid$ (8.9) et très petit pour $k=gas$ ($8.5 \times 10^{-2}$)[cite: 2641].
* [cite_start]Un ratio proche de 1 signifie que le mot est neutre (ex: $fashion$)[cite: 2641, 2642].

---

## GloVe : Modélisation
[cite_start]On cherche des représentations vectorielles qui approximent les ratios de co-occurrence[cite: 2644].
* [cite_start]**Forme générale** : $$F(w_i, w_j, \tilde{w}_k) = \frac{P_{ik}}{P_{jk}}$$ [cite: 2648]
* En utilisant le produit scalaire et la fonction exponentielle :
    * [cite_start]$$w_i^T \tilde{w}_k + b_i + \tilde{b}_k = log(X_{ik})$$ [cite: 2656]

---

## GloVe : Entraînement
[cite_start]Minimisation de la fonction de coût $J$ par descente de gradient[cite: 2658, 2660]:
* [cite_start]$$J = \sum_{i,j=1}^{V} f(X_{ij}) (w_i^T \tilde{w}_j + b_i + \tilde{b}_j - log~X_{ij})^2$$ [cite: 2659]
* [cite_start]$V$ : taille du vocabulaire[cite: 2661].
* [cite_start]$f$ : fonction de pondération pour éviter le surpoids des co-occurrences rares ou trop fréquentes[cite: 2662].
* [cite_start]Données : 840 milliards de tokens, fenêtre de 10 mots[cite: 2665, 2666].

---

## Avantages et Inconvénients de GloVe
* [cite_start]**Avantages** : Passage à l'échelle sur des corpus massifs, apprentissage efficace[cite: 2670, 2671].
* [cite_start]**Inconvénients** : Nécessite de calculer d'abord la matrice de co-occurrence $X_{ij}$[cite: 2673]. [cite_start]Vecteurs statiques[cite: 2674]. [cite_start]Ce n'est pas un modèle génératif[cite: 2675].

---

## Apprentissage de vecteurs par Réseaux de Neurones
### Description du schéma
[cite_start]La slide présente un réseau de neurones simple pour apprendre des embeddings[cite: 2676]:
1. [cite_start]**Input Layer** : Un vecteur "One-hot" ou Bag-of-Words (ex: le mot 2 est à 1, les autres à 0)[cite: 2677, 2682, 2688].
2. [cite_start]**Hidden Layer** : La couche de projection qui devient le vecteur appris (ex: valeurs 0.12, 0.92, 0.001)[cite: 2678, 2693].
3. [cite_start]**Output Layer** : Prédit la tâche cible (ex: le mot suivant)[cite: 2679, 2691].
* **Question** : Quelle est la tâche ? (Généralement la prédiction de contexte) [cite_start][cite: 2694].

---

## A Neural Probabilistic Language Model
* [cite_start]**Publication** : Advances in Neural Information Processing Systems, 2000 [cite: 492, 494]
* [cite_start]**Auteurs** : Yoshua Bengio, Réjean Ducharme, Pascal Vincent [cite: 491]

### Introduction et problématique
* [cite_start]**Objectif** : Apprendre la fonction de probabilité jointe de séquences de mots[cite: 499].
* [cite_start]**Le fléau de la dimension** : Modéliser la distribution jointe de 10 mots consécutifs avec un vocabulaire $V$ de 100 000 mots implique potentiellement $100\,000^{10} - 1$ paramètres[cite: 504, 506].
* **Modèles n-grammes** : Ils réduisent la difficulté en utilisant l'ordre des mots et la dépendance statistique locale :
  [cite_start]$$P(w_t | w_{t-1}, \dots, w_{t-n+1})$$[cite: 508, 510].

### Proposition : Représentations distribuées
* [cite_start]**Concept** : Combattre la dimensionnalité en associant à chaque mot un vecteur de caractéristiques distribué (vecteur réel dans $\mathbb{R}^n$)[cite: 524, 526].
* **Fonctionnement** : 
  1. [cite_start]Associer chaque mot du vocabulaire à un vecteur de caractéristiques[cite: 526].
  2. [cite_start]Exprimer la probabilité jointe des séquences en termes de ces vecteurs[cite: 527].
  3. [cite_start]Apprendre simultanément les vecteurs de caractéristiques et les paramètres de la fonction de probabilité[cite: 528].
* [cite_start]**Généralisation** : Une séquence jamais vue obtient une probabilité élevée si elle est composée de mots similaires à une phrase déjà rencontrée (ex: transférer la masse de probabilité entre "chat" et "chien" ou "marcher" et "courir")[cite: 517, 521].

### [cite_start]Description du schéma : Architecture du modèle [cite: 529]
Le schéma décrit un réseau de neurones pour le langage :
1. [cite_start]**Entrée** : Indices des mots de contexte ($w_{t-n+1}, \dots, w_{t-1}$)[cite: 541, 543].
2. [cite_start]**Projection** : Table de recherche (Look-up table) dans une matrice $C$ pour obtenir les vecteurs d'embeddings[cite: 533, 538].
3. [cite_start]**Couche cachée** : Une couche avec une fonction d'activation `tanh`[cite: 535].
4. [cite_start]**Sortie** : Une couche `softmax` produisant $P(w_t = i | context)$ pour chaque mot $i$ du vocabulaire[cite: 530, 531].
* [cite_start]**Paramètres** : $V \approx 100\,000$, $D$ (dimension embedding) $\approx 50$ à 200, $H$ (unités cachées) $\approx 500$ à 1000[cite: 545, 546].
* [cite_start]**Note** : L'entraînement de tant de paramètres était très problématique à l'époque (2000)[cite: 557].

---

## A Unified Architecture for Natural Language Processing
* [cite_start]**Publication** : ICML 2008 [cite: 568, 569]
* [cite_start]**Auteurs** : Ronan Collobert et Jason Weston [cite: 564, 565]
* [cite_start]**Récompense** : "Test of Time Award" à l'ICML 2018[cite: 616].

### Principes du modèle
* [cite_start]**Architecture unique** : Un réseau de neurones convolutif (CNN) qui produit simultanément plusieurs prédictions : étiquettes POS, chunks, entités nommées (NER), rôles sémantiques[cite: 573].
* [cite_start]**Apprentissage multitâche** : Le réseau est entraîné conjointement sur toutes ces tâches en partageant les poids[cite: 574, 587].
* [cite_start]**Apprentissage semi-supervisé** : Le modèle de langage est appris de manière non supervisée sur Wikipédia pour améliorer la généralisation des autres tâches[cite: 589, 590].

### [cite_start]Description du schéma : Processus de traitement [cite: 594]
1. [cite_start]**Input Sentence** : Phrase d'entrée "the cat sat on the mat" avec $K$ caractéristiques par mot[cite: 596, 597].
2. [cite_start]**Lookup Tables** : Transformation des mots en vecteurs via des matrices $LT_{w^1} \dots LT_{w^K}$[cite: 601, 603].
3. [cite_start]**Convolution Layer** : Application de filtres sur les fenêtres de mots[cite: 611].
4. [cite_start]**Max Over Time** : Sélection des valeurs maximales pour obtenir un vecteur de taille fixe[cite: 613].
5. [cite_start]**Softmax** : Classification finale pour chaque tâche[cite: 617].

---

## Word2Vec : Efficient Estimation of Word Representations
* [cite_start]**Publication** : ICLR 2013 [cite: 631]
* [cite_start]**Auteurs** : Tomas Mikolov, Kai Chen, Greg Corrado, Jeffrey Dean (Google) [cite: 622, 628]

### Concept et Objectif
* [cite_start]**Idée** : Prédire les mots à partir de leur contexte[cite: 652].
* [cite_start]**Exemple** : "The cute cat **jumps** over the lazy dog." [cite: 656]
  * [cite_start]Fenêtre $c=1$ : Contexte = {cat, over}[cite: 657, 658].
* **Fonction objective** : Maximiser la log-probabilité de prédiction sur un corpus de taille $T$ :
  [cite_start]$$\sum_{t=1}^{T} \sum_{c \in \mathcal{C}_t} \log p(w_c | w_t)$$[cite: 663].

### Negative Sampling (Échantillonnage négatif)
* [cite_start]**Problème** : Le terme de normalisation de la `softmax` nécessite un calcul sur tous les mots du vocabulaire, ce qui est trop coûteux[cite: 667, 668].
* [cite_start]**Solution** : Transformer le problème en une tâche de classification binaire : prédire si un mot apparaît ou non dans le contexte[cite: 670].
* **Fonction de perte** : 
  [cite_start]$$Loss = -\log\left(\frac{1}{1 + e^{-s(w_t, w_c)}}\right)$$[cite: 671].
  On ajoute une somme sur des exemples négatifs $n$ tirés aléatoirement du vocabulaire :
  [cite_start]$$\log(1 + e^{-s(w_t, w_c)}) + \sum_{n \in \mathcal{N}_{t,c}} \log(1 + e^{s(w_t, n)})$$[cite: 672].

### Architectures Word2Vec
1. **CBOW (Continuous Bag of Words)** : Prédit le mot actuel à partir des mots de son contexte. [cite_start]L'ordre des mots n'est pas conservé (somme des vecteurs)[cite: 674, 686].
2. [cite_start]**Skip-gram** : Prédit les mots du contexte à partir du mot actuel[cite: 687, 690].
* [cite_start]**Optimisation** : Suppression de la couche cachée pour gagner en vitesse[cite: 680, 689].

---

## Visualisation et t-SNE
* [cite_start]**Outil** : Embedding projector (projector.tensorflow.org)[cite: 731].
* [cite_start]**Description du schéma** : Capture d'écran montrant l'espace vectoriel autour du mot "beef"[cite: 736].
  * [cite_start]**Voisins proches** : pork (0.392), meat (0.415), vegetables (0.416), chicken (0.482), dairy (0.486)[cite: 770, 781].
  * [cite_start]Les distances sont calculées par similarité cosinus ou distance euclidienne[cite: 754].

---

## Propriétés de Word2Vec
* [cite_start]**Relations sémantiques et géométriques** : Les vecteurs encodent des régularités linguistiques sous forme de translations[cite: 836, 837].
* [cite_start]**Exemple célèbre** : $vec(Madrid) - vec(Spain) + vec(France) \approx vec(Paris)$[cite: 838].
* [cite_start]**Description du schéma (Analogies Pays/Capitale)** : Un graphique PCA montre des vecteurs parallèles entre les pays et leurs capitales (ex: China/Beijing, Russia/Moscow, Japan/Tokyo)[cite: 842, 869].
* **Analogies de genre et de temps** : 
  * [cite_start]King $\rightarrow$ Queen / Man $\rightarrow$ Woman[cite: 881, 884].
  * [cite_start]Walking $\rightarrow$ Walked / Swimming $\rightarrow$ Swam[cite: 885, 890].

### Raisonnement par analogie (Tableaux)
* [cite_start]**Équipes sportives** : Boston $\rightarrow$ Bruins (NHL) / Detroit $\rightarrow$ Pistons (NBA)[cite: 893].
* [cite_start]**Compagnies aériennes** : Austria $\rightarrow$ Austrian Airlines / Greece $\rightarrow$ Aegean Airlines[cite: 893].
* [cite_start]**Dirigeants** : Larry Page $\rightarrow$ Google / Steve Ballmer $\rightarrow$ Microsoft[cite: 893].

### Arithmétique vectorielle
* [cite_start]Czech + currency = koruna[cite: 896].
* [cite_start]German + airlines = Lufthansa[cite: 896].
* [cite_start]French + actress = Juliette Binoche[cite: 896].

---

## FastText : Subword Information
* [cite_start]**Publication** : Transactions of the Association for Computational Linguistics, 2017 [cite: 909]
* [cite_start]**Auteurs** : P. Bojanowski, E. Grave, A. Joulin, T. Mikolov (Facebook AI)[cite: 905].

### Principes
* **Problème de Word2Vec** : Ignore la structure interne des mots (morphologie). [cite_start]Pas de représentation pour les mots inconnus (OOV)[cite: 899, 912].
* [cite_start]**Solution** : Représenter chaque mot comme un sac de n-grammes de caractères[cite: 914].
* [cite_start]**Exemple pour le mot "where" ($n=3$)** : `<wh`, `whe`, `her`, `ere`, `re>`[cite: 947, 951].
* [cite_start]**Formule** : Le mot est représenté par la somme des vecteurs de ses n-grammes[cite: 915, 930].

---

## Doc2Vec : Représentations de documents
* [cite_start]**Auteurs** : Quoc Le et Tomas Mikolov (ICML 2014)[cite: 987, 988].
* [cite_start]**Concept** : Paragraph Vector, un algorithme non supervisé pour apprendre des vecteurs de taille fixe pour des textes de longueur variable[cite: 996].

### Deux versions :
1. [cite_start]**PV-DM (Distributed Memory)** : On ajoute un vecteur d'ID de paragraphe qui agit comme une "mémoire" du sujet traité, concaténé avec les mots du contexte pour prédire le mot suivant[cite: 1041, 1017].
2. [cite_start]**PV-DBOW (Distributed Bag of Words)** : On utilise uniquement le vecteur d'ID de paragraphe pour prédire les mots du document (similaire au skip-gram)[cite: 1045].

---

## Word Embeddings et CNN
* [cite_start]**Auteur** : Yoon Kim (EMNLP 2014)[cite: 1051, 1054].
* [cite_start]**Architecture** : Utilisation de CNN sur des vecteurs pré-entraînés pour la classification de phrases[cite: 1056].
* **Description du schéma** :
  * [cite_start]Une phrase est représentée par une matrice $n \times k$[cite: 1087].
  * [cite_start]Des filtres de différentes largeurs (ex: 3, 4, 5 mots) capturent des motifs locaux[cite: 1090, 1113].
  * [cite_start]Un **Max-over-time pooling** sélectionne la caractéristique la plus forte pour chaque filtre[cite: 1111].
  * [cite_start]Sortie finale via une couche `softmax`[cite: 1114].

---

## [cite_start]Timeline des représentations vectorielles [cite: 1115, 1140]
1. **1957** : Hypothèse distributionnelle (Firth).
2. **1990** : Latent Semantic Indexing (LSI).
3. **2000** : Modèle de langage par Réseaux de Neurones (Bengio).
4. **2008** : Unified Architecture / Multitask (Collobert).
5. **2013** : Word2Vec (Mikolov).
6. **2014** : FastText / GloVe / Doc2Vec.
7. **2018** : ELMo / BERT (Embeddings contextuels).