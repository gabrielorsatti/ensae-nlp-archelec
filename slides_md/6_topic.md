# [cite_start]Deep Learning for Natural Language Processing [cite: 1]

## [cite_start]Topic modelling [cite: 2]

* [cite_start]Christopher Kermorvant [cite: 3]
* [cite_start]ENSAE [cite: 4]
* [cite_start]2026 [cite: 5]

---

## [cite_start]Topic: definition [cite: 6]

* [cite_start]A topic (thème) is an element of a statement that is assumed to be known to the participants in the communication. [cite: 7]
* [cite_start]Pragmatic level [cite: 8]
    * [cite_start]The topic : the focus (rhème), which is the new information conveyed by the utterance. [cite: 9]
    * [cite_start]The topic : the subject of the sentence, defined by the syntax. [cite: 10]

---

## [cite_start]Topic: definition [cite: 11]

* [cite_start]France's men's biathlon team won the Olympic title on Tuesday. [cite: 12]
    * [cite_start]Topic: "France's men's biathlon team" [cite: 13]
    * [cite_start]Focus: "won the Olympic title on Tuesday" [cite: 14]
    * [cite_start]Subject: France's men's biathlon team [cite: 15]

---

## [cite_start]Topic: definition [cite: 16]

* [cite_start]The 2026 Winter Olympics are taking place in Italy this year. [cite: 17]
* The French men's biathlon team was crowned Olympic champion on Tuesday. [cite_start]Several records were broken during this edition. [cite: 18]
    * [cite_start]Topic: The French men's biathlon team (sentence level) [cite: 19]
    * [cite_start]Discourse topic: 2026 Winter Olympics (paragraph level) [cite: 19]
    * [cite_start]Global Topic: France's performance at the Olympic Games (text level) [cite: 19]

---

## [cite_start]Topic: History (until BERT) [cite: 20]

* **1990:** LSI is introduced by Deerwester et. [cite_start]Al. [cite: 21, 23, 22]
* [cite_start]**1999:** Hofmann replaces the SVD in LSI with a generative model to create pLSI. [cite: 31, 33, 36, 38, 39]
* [cite_start]**2000:** Nigam et. al use the Dirichlet distribution in a generative model to produce DMM. [cite: 22, 45]
* [cite_start]**2002:** Blei et al. create LDA, the first topic model. [cite: 32, 34, 37]
* [cite_start]**2006:** HDP is created, uses Gibbs sampling to improve model accuracy, number of topics no longer required. [cite: 24]
* [cite_start]**2006:** The first temporal topic models, DTM and TOT, are published. [cite: 35, 37, 40]
* [cite_start]**2010:** Online LDA and HDP are created to cope with larger data sets. [cite: 41]
* [cite_start]**2011:** Multiple topic modeling papers start focusing on analysis of social media. [cite: 25]
* [cite_start]**2013:** Yan et al. introduce Biterm Topic Model to create topics based on bigrams instead of unigrams. [cite: 26]
* [cite_start]**2013:** Mikolov et. al introduce Word2Vec embeddings. [cite: 42, 44]
* [cite_start]**2014:** GSDMM is introduced, modernizing the approach proposed by Nigam et al. [cite: 43, 45]
* [cite_start]**2015:** Quan et al. propose aggregating short texts into larger documents to get better topics in SATM. [cite: 27]
* [cite_start]**2016:** Li et al. introduce GPUDMM, a new sampling scheme based on word embeddings. [cite: 28]
* [cite_start]**2016:** Moody proposes Ida2vec, a direct mixture of LDA and Word2vec. [cite: 46]
* [cite_start]**2017:** Bicalho et al. propose DREx, a framework for expanding short texts using word embeddings. [cite: 47, 48, 49]
* [cite_start]**2019:** Dieng et al. introduce Embedded Topic Model, placing words and topics in the same embedding space. [cite: 29]
* [cite_start]**2019:** Supervised Neural Models begin to incorporate reinforcement learning. [cite: 47, 50]
* [cite_start]**2020:** Thompson and Mimno design a topic model that uses BERT for word embeddings. [cite: 51, 52, 53, 54]
* [cite_start]**2021:** Gui et al. use evaluation metrics as the reward in reinforcement learning. [cite: 30]

*Source: Rob Churchill and Lisa Singh. 2022. The Evolution of Topic Modeling. ACM Comput. Surv. [cite_start]54, 10s, Article 215 (January 2022), 35 pages. https://doi-org.ezproxy.u-paris.fr/10.1145/3507900* [cite: 55, 56]

---

## Latent Dirichlet Allocation (LDA) [cite: 57]

* [cite_start]Documents exhibit multiple topics [cite: 58]

### Description du schéma
L'image illustre le fonctionnement de l'allocation de Dirichlet latente (LDA) sur un document intitulé "Seeking Life's Bare (Genetic) Necessities" du magazine SCIENCE (VOL 272, 24 MAY 1996). À gauche, on observe une liste de "Topics" avec leurs mots associés et leurs probabilités : un thème jaune (gene 0.04, dna 0.02, genetic 0.01), un thème rose (life 0.02, evolve 0.01, organism 0.01), un thème vert (brain 0.04, neuron 0.02, nerve 0.01) et un thème bleu (data 0.02, number 0.02, computer 0.01). Au centre, le texte du document contient des mots surlignés avec les couleurs correspondantes à ces thèmes. [cite_start]À droite, sous le titre "Topic proportions and assignments", des flèches relient les mots surlignés du texte à des cercles colorés représentant leur assignation thématique, et un histogramme illustre les proportions globales de chaque thème dans le document entier. [cite: 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 73, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 98, 99]

*Source: David M. Blei. 2012. Probabilistic topic models. Commun. ACM 55, 4 (April 2012), 77-84.* [cite: 100]

---

## [cite_start]Latent Dirichlet Allocation (LDA) [cite: 102]

* [cite_start]Document = distributions over the possible topics. [cite: 103]
* [cite_start]Topic = distribution of words over a fixed vocabulary. [cite: 103]

[cite_start]**How to generate a document:** [cite: 104]
1.  [cite_start]Randomly choose a distribution over topics [cite: 105]
2.  [cite_start]For each word in the document [cite: 106]
    * a. [cite_start]Randomly choose a topic from the distribution over topics in step #1. [cite: 107]
    * b. [cite_start]Randomly choose a word from the corresponding distribution over the vocabulary [cite: 108]

### Description du schéma
Le schéma montre la "Distribution of the topics in the document" sous forme d'un graphique en barres avec la probabilité sur l'axe des ordonnées (de 0.0 à 0.4) et l'index des Topics sur l'axe des abscisses (de 1 à 96). [cite_start]Deux pics majeurs apparaissent vers les index 20 et 60. En dessous, des encarts listent la "Distribution of the words in the topics" pour divers thèmes : "Genetics" (genetic, human, genome, dna, genes, sequence, gene, molecular, sequencing, map, genetics, mapping, sequences), "Evolution" (evolution, evolutionary, species, organisms, origin, biology, groups, phylogenetic, diversity, group, common), "Disease" (disease, host, bacteria, diseases, resistance, bacterial, strains, infectious, malaria, parasite, parasites, tuberculosis), et "Computers" (computer, models, information, data, computers, system, network, systems, control, model, parallel, methods, networks, software). [cite: 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172]

---

## [cite_start]Latent Dirichlet Allocation (LDA) [cite: 173]

* [cite_start]Goal of topic modeling: automatically discover the topics from a collection of documents [cite: 174]
* [cite_start]Documents are observed [cite: 175]
* [cite_start]Topics are not observed [cite: 176]
* [cite_start]Words are observed [cite: 177]
* [cite_start]Topic are a hidden (latent) structure. [cite: 178]

[cite_start]**Hypothesis:** [cite: 179]
* [cite_start]The number of topic is known and fixed [cite: 180]
* [cite_start]The order of the words does not matter (bag of word) [cite: 181]
* [cite_start]The order of the document does not matter [cite: 182]

---

## [cite_start]Latent Dirichlet Allocation (LDA) [cite: 183]

### Description du schéma
Le schéma est un modèle graphique probabiliste (plate notation) pour LDA. On y voit un paramètre $\eta$ pointant vers $\beta$ à l'intérieur d'une plaque $K$. $\beta$ représente la "Per-topic word distribution". Un paramètre $\alpha$ pointe vers $\theta$, qui représente la "Per-document topic distribution". $\theta$ pointe vers $z$ ("Topic assignment to a word at position n in doc d"). $\beta$ et $z$ pointent tous deux vers la variable observée $w$ ("Word token at position n in doc d", représentée par un cercle grisé). $z$ et $w$ sont contenus dans une plaque $M$ ("For each word position in a doc of length M"), qui est elle-même contenue avec $\theta$ dans une plaque plus grande $N$ ("For each doc in a collection of N docs"). [cite_start]De petits graphiques en barres illustrent les distributions autour des paramètres. [cite: 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201]

* [cite_start]$\beta_{i:j}$ is the probability of the jth words in the ith topic [cite: 202]
* [cite_start]$\theta_{d,k}$ is the proportion of topic k in document d [cite: 203]
* [cite_start]$Z_{d,n}$ is the topic assignment for the nth word in document d [cite: 204]
* [cite_start]$W_{d,n}$ is the nth word in document d [cite: 205]

[cite_start]*Source: [Moens and Vulic, Tutorial @WSDM 2014]* [cite: 207]

---

## [cite_start]Latent Dirichlet Allocation (LDA) [cite: 208]

* [cite_start]The Dirichlet Distribution is a multivariate probability distribution defined over the space of positive vectors that sum to one. [cite: 212, 213]
    $$Dirichlet(x|\alpha)=\frac{1}{B(\alpha)}\prod_{i=1}^{k}x_{i}^{\alpha_{i}-1}$$ [cite: 214]

### Description du schéma
Six graphiques en 3D en forme de simplexe illustrent la distribution de Dirichlet avec différents vecteurs $\alpha$.
- [cite_start]Alpha = [1, 1, 1] : Les points sont répartis de manière uniforme sur le simplexe. [cite: 209]
- [cite_start]Alpha = [0.2, 0.2, 0.2] : Les points sont fortement concentrés aux extrémités (les coins) du simplexe. [cite: 210]
- [cite_start]Alpha = [5.0, 5.0, 5.0] : Les points forment une masse dense au centre du simplexe. [cite: 211]
- [cite_start]Alpha = [5.0, 1.0, 1.0] : La masse est attirée et concentrée vers l'un des coins. [cite: 241]
- [cite_start]Alpha = [1.0, 1.0, 0.2] : La distribution s'étale le long de l'une des arêtes, évitant un coin. [cite: 235]
- [cite_start]Alpha = [1.0, 5.0, 0.2] : Les points se concentrent vers un coin spécifique mais glissent le long d'une arête. [cite: 264]

* [cite_start]$\beta_{i:j}$ probability of the jth words in the ith topic [cite: 246]
* [cite_start]$\theta_{d,k}$ proportion of topic k in document d [cite: 246]
* [cite_start]Follow a Dirichlet distribution [cite: 268]

[cite_start]*Source: https://observablehq.com/@herbps10/dirichlet-distribution* [cite: 269]

---

## [cite_start]Latent Dirichlet Allocation (LDA) [cite: 270]

[cite_start]**In practice:** [cite: 271]
* [cite_start]Symetric Dirichlet (same prior probability for all topics) [cite: 273]

### Description du schéma
Le schéma reprend la "plate notation" de LDA vue précédemment en y intégrant des valeurs et dimensions matricielles concrètes. Le paramètre $\eta$ vaut 0.78 et $\alpha$ vaut 0.3. La matrice $\theta$ (Topic distribution per document) est montrée avec des vecteurs comme `[0.2 0.005 ... 0.3]` et `[0.03 0.08 ... 0.1]` sur une dimension $M$ (ou $N$). La matrice $\beta$ (Word distribution per topic) contient des vecteurs comme `[0.12 0.5 ... 0.33]` et `[0.08 0.18 ... 0.2]` sur une dimension $V$ et $K$. [cite_start]La matrice $z$ (Topic selection per word) est illustrée par des vecteurs encodés en "one-hot" (ex: `[0 0 ... 1 0]`) pointant vers le mot observé $w$. [cite: 272, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309]

---

## [cite_start]Latent Dirichlet Allocation (LDA) [cite: 310]

[cite_start]**With Scikit-Learn :** [cite: 311, 312]
* [cite_start]CountVectorizer + LatentDirichletAllocation [cite: 313]
* [cite_start]Words in Topics - LDA model [cite: 314]

| Topic 1 | Topic 2 | Topic 3 | Topic 4 | Topic 5 |
| :--- | :--- | :--- | :--- | :--- |
[cite_start]| le [cite: 320] [cite_start]| le [cite: 321] [cite_start]| del [cite: 322] [cite_start]| le [cite: 323] [cite_start]| des [cite: 335] |
[cite_start]| les [cite: 324] [cite_start]| des [cite: 327] [cite_start]| carla [cite: 326] [cite_start]| les [cite: 329] | en |
[cite_start]| des [cite: 325] [cite_start]| je vous [cite: 328] [cite_start]| ponte [cite: 331] [cite_start]| du [cite: 330] [cite_start]| sirven [cite: 348] |
[cite_start]| et [cite: 332] [cite_start]| et [cite: 334] | [cite_start]| ail [cite: 333] [cite_start]| un [cite: 352] |
| en [cite_start]| serbes [cite: 336] | | | |
[cite_start]| est [cite: 342] [cite_start]| me [cite: 338] | | | |
[cite_start]| un [cite: 344] [cite_start]| bosnie- [cite: 341] | | | |
[cite_start]| une [cite: 354] [cite_start]| président [cite: 343] | | | |
[cite_start]| il [cite: 357] | en | | | |
[cite_start]| dans [cite: 359] [cite_start]| pénal [cite: 346] | | | |
[cite_start]| pour [cite: 360] [cite_start]| un [cite: 350] | | | |
[cite_start]| le [cite: 363] [cite_start]| procureur [cite: 351] | | | |
[cite_start]| par [cite: 365] [cite_start]| suis [cite: 353] | | | |
[cite_start]| au [cite: 370] [cite_start]| une [cite: 355] | | | |
[cite_start]| qui [cite: 372] [cite_start]| tribunal [cite: 356] | | | |
[cite_start]| sur [cite: 375] [cite_start]| avez [cite: 358] | | | |
[cite_start]| pas [cite: 377] [cite_start]| pour [cite: 360] | | | |
[cite_start]| ont [cite: 379] [cite_start]| témoin [cite: 361] | | | |
[cite_start]| dans [cite: 380] [cite_start]| que [cite: 364] | | | |
[cite_start]| au [cite: 384] [cite_start]| juges- [cite: 366] | | | |
[cite_start]| du [cite: 387] [cite_start]| que [cite: 367] | | | |
[cite_start]| est [cite: 394] [cite_start]| floch [cite: 368] | | | |
[cite_start]| considéré [cite: 396] [cite_start]| par [cite: 369] | | | |
[cite_start]| il [cite: 398] [cite_start]| au [cite: 370] | | | |
| [cite_start]été [cite: 399] [cite_start]| humanité [cite: 371] | | | |
| [cite_start]épreuve [cite: 401] [cite_start]| qui [cite: 374] | | | |
[cite_start]| votre [cite: 403] [cite_start]| elf [cite: 373] | | | |
[cite_start]| il [cite: 404] [cite_start]| institution [cite: 376] | | | |
[cite_start]| plus [cite: 407] [cite_start]| francs [cite: 378] | | | |
[cite_start]| irak [cite: 409] [cite_start]| génocide [cite: 381] | | | |
[cite_start]| témoigner [cite: 411] [cite_start]| dans [cite: 382] | | | |
[cite_start]| ancien [cite: 413] [cite_start]| prigent [cite: 383] | | | |
[cite_start]| sur [cite: 414] [cite_start]| qui [cite: 385] | | | |
[cite_start]| aux [cite: 415] [cite_start]| crime [cite: 386] | | | |
[cite_start]| sur [cite: 417] [cite_start]| pour [cite: 389] | | | |
[cite_start]| ces [cite: 418] [cite_start]| acte [cite: 391] | | | |
| [cite_start]| comptes [cite: 393] | | | |
| [cite_start]| est [cite: 394] | | | |
| [cite_start]| il [cite: 395] | | | |
| [cite_start]| ne [cite: 397] | | | |
| | [cite_start]été [cite: 399] | | | |
| [cite_start]| est [cite: 400] | | | |
| [cite_start]| qu [cite: 402] | | | |
| [cite_start]| tribunaux [cite: 406] | | | |
| [cite_start]| tribunal [cite: 408] | | | |
| [cite_start]| son [cite: 410] | | | |
| [cite_start]| ce [cite: 412] | | | |
| [cite_start]| arguments [cite: 416] | | | |

---

## [cite_start]Latent Dirichlet Allocation (LDA) [cite: 419]

[cite_start]**With Scikit-Learn :** [cite: 420, 421]
* [cite_start]CountVectorizer + Stop Word + LatentDirichletAllocation [cite: 422]
* [cite_start]Words in Topics - LDA model [cite: 423]

| [cite_start]Topic 1 [cite: 424] | [cite_start]Topic 2 [cite: 425] | [cite_start]Topic 3 [cite: 426] | [cite_start]Topic 4 [cite: 427] | [cite_start]Topic 5 [cite: 428] |
| :--- | :--- | :--- | :--- | :--- |
[cite_start]| art [cite: 429] [cite_start]| sncf voirain tribunal [cite: 432] [cite_start]| chaîne chaînes [cite: 433] [cite_start]| pays président [cite: 434] [cite_start]| film cinéma films cinéaste [cite: 441] |
[cite_start]| oeuvre [cite: 430] [cite_start]| csm [cite: 438] [cite_start]| tf1 [cite: 435] [cite_start]| irak [cite: 436] [cite_start]| oeuvres [cite: 442] |
[cite_start]| musée [cite: 431] [cite_start]| magistrature [cite: 443] [cite_start]| télévision [cite: 439] [cite_start]| guerre [cite: 440] [cite_start]| geoffroy [cite: 447] |
[cite_start]| exposition [cite: 437] | [cite_start]Ici [cite: 444] [cite_start]| canal [cite: 448] [cite_start]| france [cite: 445] [cite_start]| personnages [cite: 463] |
[cite_start]| artiste [cite: 450] [cite_start]| années [cite: 446] [cite_start]| publicité [cite: 452] [cite_start]| etats [cite: 449] [cite_start]| cinématographique [cite: 465] |
[cite_start]| architecture [cite: 454] [cite_start]| instance [cite: 451] [cite_start]| diffusion [cite: 456] [cite_start]| politique [cite: 453] [cite_start]| avocate [cite: 473] |
[cite_start]| images [cite: 458] [cite_start]| magistrat [cite: 455] [cite_start]| m6 [cite: 460] [cite_start]| ministre [cite: 457] [cite_start]| new [cite: 477] |
[cite_start]| dvd [cite: 462] [cite_start]| substitut [cite: 459] [cite_start]| câble [cite: 469] [cite_start]| unis [cite: 461] [cite_start]| caméra [cite: 481] |
[cite_start]| histoire [cite: 464] [cite_start]| tribunaux [cite: 468] [cite_start]| fred [cite: 471] [cite_start]| américains [cite: 475] [cite_start]| tournage [cite: 491] |
[cite_start]| scène [cite: 466] [cite_start]| monde [cite: 470] [cite_start]| satellite [cite: 474] [cite_start]| gouvernement [cite: 480] [cite_start]| ozu fille [cite: 510] |
[cite_start]| saint [cite: 467] | [cite_start]élèves [cite: 476] [cite_start]| canalsatellite [cite: 479] [cite_start]| faut [cite: 485] [cite_start]| cinéastes [cite: 520] |
[cite_start]| artistes [cite: 472] [cite_start]| avocat [cite: 478] [cite_start]| bouquet [cite: 484] [cite_start]| temps [cite: 490] | |
[cite_start]| centre [cite: 482] [cite_start]| judiciaire [cite: 483] [cite_start]| abonnés [cite: 494] [cite_start]| temps [cite: 492] | |
[cite_start]| amour [cite: 486] [cite_start]| justice [cite: 488] [cite_start]| magazines [cite: 498] [cite_start]| conseil [cite: 495] | |
[cite_start]| peintre [cite: 487] [cite_start]| information [cite: 489] [cite_start]| diffuser [cite: 499] [cite_start]| américain [cite: 500] | |
[cite_start]| récit [cite: 496] [cite_start]| cour [cite: 493] [cite_start]| publicitaires [cite: 508] [cite_start]| perben [cite: 503] | |
[cite_start]| architecte [cite: 497] [cite_start]| droits [cite: 504] [cite_start]| rémunération [cite: 518] [cite_start]| français [cite: 505] | |
[cite_start]| resnais [cite: 501] [cite_start]| trains [cite: 507] | [cite_start]| homme [cite: 509] | |
[cite_start]| objets [cite: 502] [cite_start]| homme [cite: 509] | [cite_start]| etat [cite: 514] | |
[cite_start]| paris [cite: 506] [cite_start]| etat [cite: 514] | [cite_start]| cp [cite: 515] | |
| [cite_start]000 [cite: 511] [cite_start]| concurrence- [cite: 513] | [cite_start]| europe [cite: 519] | |
[cite_start]| revue [cite: 512] | | | | |
[cite_start]| portrait [cite: 516] | | | | |
[cite_start]| photos [cite: 517] | | | | |

### Description du schéma
La diapositive comprend un graphique à barres horizontales bleues illustrant l'importance des mots clés d'un thème (probablement lié à la politique et aux conflits). [cite_start]On y retrouve les mots : pays, président, irak, guerre, france, etats, politique, ministre, unis, monde, américains, gouvernement, faut, temps, conseil, américain, français, homme, etat, europe. [cite: 418]

---

## [cite_start]Latent Dirichlet Allocation (LDA) [cite: 521]

* [cite_start]Lemmatization + Stop Word + CountVectorizer + LatentDirichletAllocation [cite: 522]
* [cite_start]Words in Topics - LDA model [cite: 523]

| [cite_start]Topic 1 [cite: 524] | [cite_start]Topic 2 [cite: 525] | [cite_start]Topic 3 [cite: 526] | [cite_start]Topic 4 [cite: 527] | [cite_start]Topic 5 [cite: 528] |
| :--- | :--- | :--- | :--- | :--- |
[cite_start]| retraite impôt [cite: 529] [cite_start]| côte [cite: 530] [cite_start]| devoir pouvoir [cite: 532] | [cite_start]élève école [cite: 533] [cite_start]| européen europe [cite: 534] |
[cite_start]| fiscal [cite: 535] [cite_start]| rebelle [cite: 531] [cite_start]| euro [cite: 537] [cite_start]| noureev [cite: 538] [cite_start]| pays [cite: 539] |
[cite_start]| baisse [cite: 555] | [cite_start]Ivoirien [cite: 536] [cite_start]| groupe [cite: 542] [cite_start]| ferry [cite: 543] [cite_start]| france [cite: 544] |
[cite_start]| projet [cite: 560] [cite_start]| ivoire [cite: 541] [cite_start]| france [cite: 547] [cite_start]| xiao [cite: 548] [cite_start]| pouvoir [cite: 549] |
[cite_start]| régime [cite: 565] [cite_start]| abidjan [cite: 546] [cite_start]| million [cite: 557] [cite_start]| cp [cite: 553] [cite_start]| français [cite: 554] |
[cite_start]| pension [cite: 570] [cite_start]| gbagbo [cite: 551] [cite_start]| président [cite: 562] [cite_start]| redoublement [cite: 558] [cite_start]| union [cite: 559] |
[cite_start]| social [cite: 575] [cite_start]| ministre [cite: 552] [cite_start]| gouvernement [cite: 567] [cite_start]| ren [cite: 563] [cite_start]| allemand [cite: 564] |
[cite_start]| dépense [cite: 580] [cite_start]| f1 [cite: 556] [cite_start]| public [cite: 572] [cite_start]| rudolf [cite: 568] [cite_start]| devoir [cite: 569] |
[cite_start]| cotisation [cite: 585] [cite_start]| pilote [cite: 561] | [cite_start]2002 [cite: 577] [cite_start]| classe [cite: 573] [cite_start]| politique [cite: 574] |
[cite_start]| déficit [cite: 590] [cite_start]| patriote [cite: 566] [cite_start]| entreprise [cite: 582] [cite_start]| enseignant [cite: 578] | [cite_start]équipe [cite: 579] |
[cite_start]| loi [cite: 595] [cite_start]| luyne [cite: 571] [cite_start]| jean [cite: 587] [cite_start]| primaire [cite: 583] [cite_start]| entrer [cite: 584] |
| [cite_start]épargne [cite: 600] [cite_start]| politique [cite: 574] [cite_start]| national [cite: 592] [cite_start]| pédagogique [cite: 588] [cite_start]| monde [cite: 589] |
[cite_start]| mesure [cite: 605] [cite_start]| voiture [cite: 576] [cite_start]| année [cite: 597] [cite_start]| apprentissage [cite: 593] [cite_start]| président [cite: 594] |
[cite_start]| fonctionnaire [cite: 610] [cite_start]| bouches [cite: 581] [cite_start]| entrer [cite: 602] [cite_start]| expérimentation [cite: 598] [cite_start]| allemagne [cite: 599] |
[cite_start]| réforme réform [cite: 615] [cite_start]| laurent [cite: 586] [cite_start]| général [cite: 607] [cite_start]| précoce [cite: 603] [cite_start]| championnat [cite: 604] |
[cite_start]| milliard [cite: 617] [cite_start]| samedi [cite: 591] [cite_start]| social [cite: 612] [cite_start]| essonn [cite: 608] [cite_start]| club [cite: 609] |
| [cite_start]000 [cite: 621] [cite_start]| franck [cite: 596] [cite_start]| milliard [cite: 617] | [cite_start]égal [cite: 613] [cite_start]| commission [cite: 614] |
| [cite_start]| sébastien [cite: 601] | [cite_start]000 [cite: 621] [cite_start]| gala [cite: 618] [cite_start]| champion [cite: 619] |
| [cite_start]| place [cite: 606] | | [cite_start]écrir [cite: 622] [cite_start]| grand [cite: 623] |
| [cite_start]| course [cite: 611] | | | |
| [cite_start]| réconciliation [cite: 616] | | | |
| [cite_start]| rhône [cite: 620] | | | |

### Description du schéma
Trois graphiques en barres horizontales bleues représentent l'importance relative des mots pour trois thèmes distincts. Le premier graphique liste : devoir, pouvoir, euro, groupe, france, ministre, million, président, gouvernement, public, 2002, entreprise, jean, national, année, entrer, général, social, milliard, 000. Le deuxième graphique liste : élève, école, noureev, ferry, xiao, cp, redoublement, ren, rudolf, classe, enseignant, primaire, pédagogique, apprentissage, expérimentation, précoce, essonn, égal, gala, écrir. [cite_start]Le troisième graphique liste : européen, europe, pays, france, pouvoir, français, union, allemand, devoir, politique, équipe, entrer, monde, président, allemagne, championnat, club, commission, champion, grand. [cite: 520]

---

## [cite_start]Nonnegative Matrix Factorisation(NMF) [cite: 624]

* [cite_start]Goal of NMF: Approximate a non-negative matrix [cite: 625]

### Description du schéma
Le schéma illustre la factorisation en matrices non négatives (NMF) de manière visuelle et mathématique. Une grande matrice `V` représente les "Documents" (en colonnes) et les "Words" (en lignes). [cite_start]Elle est approximativement égale ($\approx$) au produit de deux matrices plus petites : `W`, appelée "Dictionary matrix", qui a des "Topics" en colonnes et des "Words" en lignes ; et `H`, appelée "Activation matrix", qui représente les "Topic importance indicators" (lignes) pour chaque Document (colonnes). [cite: 626, 627, 628, 629, 630, 631, 632, 633, 634, 635]

---

## [cite_start]Nonnegative Matrix Factorisation(NMF) [cite: 636]

* [cite_start]Lemmatization + Stop Word + TfidfVectorizer + NMF [cite: 637]
* [cite_start]Words in Topics - NMF model [cite: 638]

| [cite_start]Topic 1 [cite: 639] | [cite_start]Topic 2 [cite: 640] | [cite_start]Topic 3 [cite: 641] | [cite_start]Topic 4 [cite: 642] | [cite_start]Topic 5 [cite: 643] |
| :--- | :--- | :--- | :--- | :--- |
[cite_start]| européen europe [cite: 644] [cite_start]| irak [cite: 648] [cite_start]| euro milliard [cite: 650] [cite_start]| film cinéma [cite: 651] [cite_start]| attentat heure police [cite: 655] |
[cite_start]| pays [cite: 645] [cite_start]| américain [cite: 649] [cite_start]| million [cite: 653] [cite_start]| musique [cite: 654] [cite_start]| sud [cite: 663] |
[cite_start]| union [cite: 646] [cite_start]| irakien [cite: 652] [cite_start]| groupe [cite: 657] [cite_start]| théâtre [cite: 662] [cite_start]| luire [cite: 667] |
[cite_start]| politique [cite: 647] [cite_start]| saddam [cite: 656] [cite_start]| dollar [cite: 661] [cite_start]| scène [cite: 672] [cite_start]| terroriste [cite: 673] |
[cite_start]| pouvoir [cite: 658] [cite_start]| al [cite: 659] | [cite_start]2002 [cite: 666] [cite_start]| festival [cite: 677] [cite_start]| devoir [cite: 674] |
[cite_start]| commission [cite: 664] [cite_start]| guerre [cite: 660] [cite_start]| marché [cite: 671] [cite_start]| jeune [cite: 682] [cite_start]| nord [cite: 683] |
[cite_start]| allemand [cite: 669] [cite_start]| hussein [cite: 665] [cite_start]| entreprise [cite: 676] [cite_start]| grand [cite: 687] [cite_start]| lundi- [cite: 688] |
[cite_start]| bush [cite: 675] [cite_start]| mort [cite: 668] [cite_start]| chiffre [cite: 681] [cite_start]| art [cite: 692] [cite_start]| ministre [cite: 694] |
| [cite_start]000 [cite: 678] [cite_start]| bagdad [cite: 670] [cite_start]| banque [cite: 686] [cite_start]| ville [cite: 693] [cite_start]| corse [cite: 698] |
[cite_start]| etat [cite: 679] [cite_start]| onu [cite: 680] | [cite_start]2003- [cite: 691] [cite_start]| artiste [cite: 697] [cite_start]| femme [cite: 702] |
[cite_start]| pouvoir [cite: 684] [cite_start]| etats [cite: 685] [cite_start]| financier [cite: 696] [cite_start]| oeuvre [cite: 707] [cite_start]| homme [cite: 703] |
[cite_start]| france- [cite: 689] [cite_start]| unis [cite: 690] [cite_start]| capital [cite: 701] [cite_start]| histoire [cite: 712] [cite_start]| bruxelle [cite: 721] |
[cite_start]| convention [cite: 699] [cite_start]| washington [cite: 695] [cite_start]| annoncer [cite: 706] | image [cite_start]| régime [cite: 722] |
[cite_start]| allemagne [cite: 704] [cite_start]| militaire [cite: 700] [cite_start]| société [cite: 711] [cite_start]| cinéaste [cite: 730] [cite_start]| entrer [cite: 724] |
[cite_start]| conseil [cite: 709] [cite_start]| al [cite: 705] [cite_start]| année [cite: 715] [cite_start]| vie [cite: 735] [cite_start]| tuer [cite: 733] |
[cite_start]| pouvoir [cite: 710] [cite_start]| afp [cite: 708] [cite_start]| année [cite: 716] [cite_start]| voir [cite: 737] [cite_start]| juillet [cite: 734] |
[cite_start]| président [cite: 714] | [cite_start]étranger [cite: 713] [cite_start]| croissance [cite: 719] [cite_start]| centre [cite: 739] [cite_start]| arrêter [cite: 738] |
[cite_start]| sommet [cite: 717] [cite_start]| arme [cite: 718] [cite_start]| trimestre [cite: 723] | | |
[cite_start]| pays [cite: 725] [cite_start]| résolution [cite: 728] [cite_start]| hausse [cite: 726] | | |
[cite_start]| gouvernement [cite: 727] [cite_start]| dimanche [cite: 732] [cite_start]| baisse [cite: 729] | | |
| [cite_start]| jeudi [cite: 736] | | | |

### Description du schéma
[cite_start]Un graphique en barres horizontales bleues illustre l'importance relative des mots pour le Topic 3. Les mots sont affichés par ordre d'importance décroissante : euro, milliard, million, groupe, dollar, 2002, marché, entreprise, chiffre, banque, 2003, financier, capital, annoncer, société, année, croissance, trimestre, hausse, baisse. [cite: 636]

---

## [cite_start]LDA versus NMF [cite: 740]
[cite_start]Non-Negative Matrix Factorization [cite: 741]

| Aspect | LDA | NMF |
| :--- | :--- | :--- |
| Model type | Probabilistic generative model | Linear algebra factorization |
| Objective function | Maximize log-likelihood | Minimize reconstruction error |
| Statistical assumptions | Multinomial word distribution + Dirichlet priors | No probabilistic assumptions |
| Input representation | Raw word counts | Any non-negative matrix (Counts or TF-IDF) |
| Topic sparsity | Often diffuse topics | Often sharper, more localized topics |
| Best suited for | Modeling generative thematic structure | Discovering discriminative lexical axes |

[cite_start]*Source : The following table:* [cite: 742]

---

## [cite_start]Topic: metrics [cite: 743]

* [cite_start]Comme le Topic Modelling est non supervisé, il est difficile de mesurer sa qualité. [cite: 744]
* [cite_start]On utilise principalement la cohérence thématique pour se rapprocher du jugement humain. [cite: 745]
* [cite_start]Les métriques courantes incluent: [cite: 746]
    * [cite_start]**Perplexity (LDA):** Utile pour comparer des modèles mais peu corrélée au jugement humain. [cite: 747]
    * [cite_start]**UCI Coherence:** Basée sur le Pointwise Mutual Information (PMI) entre les mots. [cite: 748]
    * [cite_start]**Cv Coherence:** Une métrique complexe utilisant des vecteurs NPMI et la similarité cosinus, considérée comme la plus proche des évaluations humaines. [cite: 749]
* [cite_start]Training topic modeling is unsupervised. [cite: 750]
* [cite_start]The quality of a topic is generally evaluated by its coherence. [cite: 751]
* [cite_start]« Fitting » metrics such as Perplexity (LDA) or reconstruction error (NMF) are usefull to compare models but are not related to human ratings of topic coherence. [cite: 752]
* [cite_start]Topic coherence by human are based on the top n words in topics. [cite: 753]

---

## [cite_start]Topic: metrics [cite: 754]

* [cite_start]**UCI Coherence** [cite: 755]
    * [cite_start]Computed on a sliding window on the training texts [cite: 756]
    [cite_start]$$C_{UCI}=\frac{2}{N\cdot(N-1)}\sum_{i=1}^{N-1}\sum_{j=i+1}^{N}PMI(w_{i},w_{j})$$ [cite: 759]
    [cite_start]$$PMI(w_{i},w_{j})=log\frac{P(w_{i},w_{j})+\epsilon}{P(w_{i})\cdot P(w_{j})}$$ [cite: 759]

* [cite_start]**UMass Coherence** [cite: 757]
    * [cite_start]Computed on the word sequence of the training texts [cite: 758]
    $$C_{UMass}=\frac{2}{N\cdot(N-1)}\sum_{i=2}^{N}\sum_{j=1}^{i-1}log\frac{P(w_{i},w_{j})+\epsilon}{P(w_{j})}$$ [cite: 760]

---

## [cite_start]Topic: metrics [cite: 761]

* [cite_start]**Cv Coherence** [cite: 762]
    * [cite_start]A metric 'discovered' through systematic experiments to find the correlation between coherence metrics and human ratings. [cite: 763]

    1.  [cite_start]Compute NPMI for each topic words in sliding window [cite: 766]
        $$PMI(w_{i},w_{j})=log\frac{P(w_{i},w_{j})}{P(w_{i})P(w_{j})}$$ [cite: 764]
        $$NPMI(w_{i},w_{j})=\frac{PMI(w_{i},w_{j})}{-log~P(w_{i},w_{j})}$$ [cite: 764]
    2.  Create a NPMI vector for each word [cite: 767]
        $$v(w_{i})=[NPMI(w_{i},w_{1}),...,NPMI(w_{i},w_{N})]$$ [cite: 765]
    3.  Compute the average of the cosine similarty between each words in each topic [cite: 769]
        $$cosine(v(w_{i}),v(w_{j}))$$ [cite: 768]
        $$c_{v}=\frac{\sum_{k=1}^{K}\sum_{n=1}^{N}s_{cos}(\vec{w}_{n,k},\vec{w}_{k}^{*})}{N\times K}$$ [cite: 768]

*Source: Michael Röder, Andreas Both, and Alexander Hinneburg. 2015. Exploring the Space of Topic Coherence Measures. In Proceedings of the Eighth ACM International Conference on Web Search and Data Mining (WSDM '15)* [cite: 770, 771]

---

## [cite_start]Libraries [cite: 772]

### Description du schéma
Une composition de plusieurs captures d'écran présentant des outils populaires de modélisation de sujets :
1. [cite_start]La documentation officielle de Scikit-learn pour la classe `LatentDirichletAllocation`, listant ses paramètres (comme `n_components`, `doc_topic_prior`, `topic_word_prior`, `learning_method`, etc.). [cite: 779, 780, 782, 783, 786, 787, 788, 790, 791]
2. Une page promotionnelle de Gensim, annoncée comme une bibliothèque Python gratuite : "Topic modelling for humans". [cite_start]On y mentionne ses capacités pour entraîner des modèles NLP sémantiques, représenter du texte en vecteurs et trouver des documents similaires. [cite: 793, 794, 799] [cite_start]Un module `models.coherencemodel` est mis en avant pour calculer la cohérence selon l'article de Röder et al. [cite: 795, 796, 797, 798] [cite_start]Un graphique y montre la "Normalized Coherence Comparison" comparant `u_mass`, `c_v`, `c_uci`, `c_npmi` en fonction du nombre de topics (k). [cite: 804, 805, 809]
3. [cite_start]L'interface interactive de PyLDAViz, affichant une "Intertopic Distance Map" (une carte en 2D où chaque topic est une bulle proportionnelle à sa taille) et un histogramme des 30 termes les plus pertinents ("Top-30 Most Relevant Terms") pour le Topic 1 sélectionné. [cite: 812, 813, 814, 815]

---

## [cite_start]Topic modeling recap [cite: 816]

* [cite_start]Topic modelling is unsupervised and requires human interpretation. [cite: 817]
* [cite_start]The number of topics is a meta-parameter that needs to be optimised. [cite: 818]
* [cite_start]For human interpretation, the number of topics and the number of topic words should not be too large. [cite: 819]
* [cite_start]These methods define and describe topics per document, forming the basis for further analysis. [cite: 820]