# Deep Learning for Natural Language Processing
## 3. Language models
### Christopher Kermorvant
### ENSAE
### 2026

---

## Cryptography and language models

### Encryption by substitution

* ZLNLSHGLD O'HQFBFORSHGLH OLEUH
* XYZABCDEF
* ABCDEFGHI
* WIKIPEDIA L'ENCYCLOPEDIE LIBRE
* Caesar's Code

#### Description du schéma
Ce schéma illustre le principe du code de César. On y voit un buste de Jules César, ainsi qu'un mécanisme de substitution où une séquence de lettres de l'alphabet "A B C D E F" est décalée d'un certain nombre de positions pour correspondre à "A B C D E F G H I". Par exemple, la lettre "B" du message d'origine est chiffrée par la lettre "E", ce qui correspond à un décalage de trois positions.

---

## Cryptography and language models

* LIVITCSWPIYVEWHEVSRIQMXLEYVEOIEWHRXEXIPFEMVEWH KVSTYLXZIXLIKIIXPIJVSZEYPERRGERIMWQLMGLMXQERIWGPS RIHMXQEREKIETXMJTPRGEVEKEITREWHEXXLEXXMZITWAWS QWXSWEXTVEPMRXRSJGSTVRIEYVIEXCVMUIMWERGMIWXMJ MGCSMWXSJOMIQXLIVIQIVIXQSVSTWHKPEGARCSXRW
* ↓
* Frequencies of letters, bigram, trigram, etc
* ↓
* Hereupon Legrand arose, with a grave and stately air, and brought me the beetle from a glass case in which it was enclosed. It was a beautiful scarabaeus, and, at that time, unknown to naturalists-of course a great prize in a scientific point

#### Description du schéma
Ce schéma montre comment la fréquence d'apparition des lettres dans une langue peut être utilisée pour décrypter un message chiffré par substitution. Un histogramme représente la distribution des fréquences des lettres (de 'a' à 'z') dans le texte cible, avec des pics notables pour les lettres 'e', 't', 'a', et 'o'. Cette analyse statistique permet de passer du bloc de texte chiffré (en haut) au texte en clair déchiffré (en bas).

---

## Language models

* Model sequences of words or characters:
    $P(w_{1},...,w_{T})$
* They evaluate the probability of a sentence:
* Most likely word:
    $P(\text{the, cat, sat, on, tea, mat}) > P(\text{the, cat, sat, on, the, yesterday})$
* Most likely word order:
    $P(\text{the, cat, sat, on, tea, mat}) > P(\text{the, sat, cat, tea, on, mat})$

---

## Language models
### Language Models using Markov Chains

* Markovian hypothesis: the probability of the next symbol depends only on the previous n:
    $P(w_{1},...,w_{m})=\prod_{i=1}^{m}P(w_{i}|w_{1},...,w_{i-1}) \approx\prod_{i=1}^{m}P(w_{i}|w_{i-(n-1)},...,w_{i-1})$

---

## Language models with Markov Chains

* Zerogram : $\frac{1}{|V|},|V|$ is the vocabulary size
* Unigram : probability of each symbol
* Bigram: probability of each symbol given the previous symbol
    $p(w_{2}|w_{1})=\frac{count(w_{1},w_{2})}{count(w_{1})}$
* Trigram probability of each symbol given the two previous symbols
    $p(w_{3}|w_{1},w_{2})=\frac{count(w_{1},w_{2},w_{3})}{count(w_{1},w_{2})}$

---

## Language models with Markov Chains

* The models are trained by counting frequencies on very large corpora of electronic text
* High memory and CPU consumption
* The ClueWeb09 Dataset: 1,040,809,705 de pages web
* Heafield et al., Scalable Modified Kneser-Ney Language Model Estimation, 2013

#### Description du schéma
Deux graphiques illustrent la consommation de ressources en fonction du nombre de tokens (en millions) pour différents modèles (SRI, SRI compact, IRST, This work). Le premier graphique montre que la consommation de mémoire RAM (en GB) augmente de manière linéaire ou quasi-linéaire très rapidement pour la plupart des méthodes, sauf pour "This work" qui reste extrêmement basse et constante. Le second graphique montre une tendance similaire pour le temps CPU (en heures) qui croît proportionnellement au nombre de tokens, où "This work" se montre nettement plus performant que l'approche IRST.

---

## Language models: quality measures

* Cross-Entropy
    $H(w_{1},...,w_{N})=-\frac{1}{N}log_{2}P(w_{1},...,w_{N})$
    $P(w_{1},...,w_{m})=\prod_{i=1}^{m}P(w_{i}|w_{1},...,w_{i-1})$
    = how many bits does it take to encode the sequence of words with the pattern
* Perplexity: $2^{H(w_{1},...,w_{N})}$
    = on average, how many words are possible after a given context

---

## Language models: smoothing

* $P(w_{1},...,w_{N})=\prod_{I=1}^{N}P(w_{i}|w_{i-(n-1)},...,w_{i-1})$
* If only one of the probabilities is zero, the whole sequence is zero:
    P(I drink tesgüino with my friends) $=0$
* We must make sure that $P(W_{i}| \text{context})$ is never null, whatever the context

---

## Language models: smoothing

* Smoothing by Interpolation:
    $$\begin{matrix}p_{1}(w_{n}|w_{n-2},w_{n-1})&=&\lambda_{3}p(w_{n}|w_{n-2},w_{n-1})+\\ &&\lambda_{2}p(w_{n}|w_{n-1})+\\ &\lambda_{1}p(w_{n}).\end{matrix}$$
* $\lambda_{3}+\lambda_{2}+\lambda_{1}=1$.
* Multiple methods have been proposed:
* An empirical study of smoothing techniques for language modeling. Stanley Chen and Joshua Goodman, 1998.

---

## How to build language models with neural networks?

* Limitations:
    * The context length is fixed
    * No weight sharing
* Bengio et al, a Neural probabilistic language model, 2003

#### Description du schéma
Ce schéma représente l'architecture d'un modèle probabiliste de langage basé sur les réseaux de neurones (feed-forward). En bas, les index des mots du contexte ($w_{t-n+1}$ à $w_{t-1}$) font l'objet d'une recherche dans une matrice partagée $C$ (Table look-up in C) pour obtenir des vecteurs continus. Ces vecteurs sont concaténés et passés dans une couche cachée utilisant une fonction d'activation `tanh`. La sortie passe ensuite par une couche `softmax` pour produire une distribution de probabilité sur le vocabulaire : $i$-th output = $P(w_{t}=i | \text{context})$. Le schéma précise que la majorité des calculs se fait au niveau de la couche de sortie.

---

## How to build language models with neural networks?

* Recurrent neural networks can model and predict sequences
* Mikolov et al, Recurrent neural network based language model, Interspeech, 2010

#### Description du schéma
Ce schéma met en évidence la transition d'un réseau de neurones classique (Input Layer, Hidden Layer, Output Layer) vers un réseau de neurones récurrent (RNN). Sur la droite, une vue simplifiée du RNN montre une entrée au temps $t$ (INPUT(t)), qui met à jour un contexte au temps $t$ (CONTEXT(t)), lequel produit une sortie au temps $t$ (OUTPUT(t)). La caractéristique clé est une boucle de rétroaction où le contexte précédent (CONTEXT(t-1)) est également injecté comme entrée pour calculer le nouveau contexte (CONTEXT(t)), permettant ainsi au modèle de conserver une mémoire séquentielle.

---

## Recurrent neural networks

* We can unroll a recurrent neuron over time: at each time step i, the same neuron is used to make a prediction, taking into account the current input $X_{i}$ and its state at the previous step $h_{i-1}$
* The model is trained with backpropagation through time (BPTT). The weights are shared across all time steps.

#### Description du schéma
Le schéma illustre le concept de "déroulement" (unrolling) d'un réseau de neurones récurrent dans le temps. À gauche, une représentation compacte d'une cellule récurrente $A$ prend une entrée $X_t$ et produit une sortie $h_t$, avec une boucle sur elle-même. À droite du signe égal, cette même boucle est dépliée temporellement pour montrer une séquence de cellules $A$ interconnectées : l'entrée $X_0$ donne $h_0$ et passe un état à l'étape suivante, puis $X_1$ donne $h_1$, et ainsi de suite jusqu'à $X_t$ et $h_t$.

---

## Recurrent neural networks with embeddings

* Unrolling:
    * $h_{1}$, $h_{2}$, ..., $h_N$
    * $x_1$, $x_2$, ..., $x_N$
    * $y_1$, $y_2$, ..., $y_N$

#### Description du schéma
Ces trois schémas montrent l'intégration d'une couche d'embeddings (plongements lexicaux) dans le réseau récurrent. En entrée, un vecteur "one-hot" ($0 0 0 0 1 0...0 0$) est transformé en un vecteur continu $x_t$ dense. Ce vecteur alimente la couche cachée récurrente $h_t$ qui produit une prédiction $y_t$. Les deux autres schémas montrent le dépliage temporel complet de cette architecture pour les étapes $x_1$ à $x_N$.

---

## Recurrent neural networks parameters

* $h_{t}=g(Uh_{t-1}+Wx_{t})$
* $y_{t}=f(Vh_{t})$
* $y_{t}=softmax(Vh_{t})$
* https://web.stanford.edu/~jurafsky/slp3/ chapter 8

#### Description du schéma
Le schéma détaille visuellement les calculs à l'intérieur d'un RNN à une étape de temps $t$. Le nouvel état caché $h_t$ est calculé en additionnant deux projections : la projection de l'entrée actuelle $x_t$ multipliée par la matrice de poids $W$, et la projection de l'état caché précédent $h_{t-1}$ multipliée par la matrice de poids $U$. Une fonction d'activation $g$ est appliquée au résultat de cette somme. La prédiction finale $y_t$ est obtenue en multipliant l'état caché courant $h_t$ par une matrice de poids $V$, suivie d'une fonction d'activation (ici un `softmax`).

---

## Recurrent neural networks parameters

```python
function FORWARDRNN(x, network) returns output sequence y
    h^0 <- 0
    for i = 1 to LENGTH(x) do
        h_i <- g(U h_{i-1} + W x_i)
        y_i <- f(V h_i)
    return y


#### Description du schéma
Le schéma montre l'architecture paramétrique d'un RNN déroulé sur trois étapes de temps ($x_1, x_2, x_3$). Il met en évidence le partage des paramètres : la même matrice $U$ est utilisée pour relier les états cachés entre eux ($h_0 \rightarrow h_1 \rightarrow h_2 \rightarrow h_3$), la même matrice $W$ est utilisée pour transformer toutes les entrées ($x_i \rightarrow h_i$), et la même matrice $V$ est utilisée pour générer les sorties à partir de l'état caché ($h_i \rightarrow y_i$).

### Recurrent neural networks as LM
* **Next word**: long, and, thanks, for, all
* **Loss**: $-\log y_{\text{long}}, -\log y_{\text{and}}, -\log y_{\text{thanks}}, -\log y_{\text{for}}, -\log y_{\text{all}}$
* **Formule**: $\frac{1}{T}\sum_{t=1}^{T}L_{CE}$
* **Training**: Training with Teacher forcing

#### Description du schéma
Ce schéma représente l'utilisation d'un RNN comme modèle de langage sur la phrase "So long and thanks for all". À chaque étape, une entrée (Input Embeddings: "So", "long", "and"...) est fournie au RNN. La cellule cache $h$ transmet son état à la cellule suivante. À chaque pas, une couche softmax produit une distribution de probabilité sur le vocabulaire complet. L'erreur (Loss) est calculée par entropie croisée ($-\log y_{\text{mot\_attendu}}$) entre la prédiction et le mot cible suivant. L'annotation précise que le modèle est entraîné en mode "Teacher forcing" (les vrais mots précédents sont donnés au modèle pendant l'entraînement).

### Recurrent neural networks as POS tagger
* **Argmax**: NNP, MD, VB, DT, NN
* **Words**: Janet, will, back, the, bill
* **Embedding**: Using pre-trained word embedding

#### Description du schéma
Ce schéma illustre l'application d'un RNN à la tâche de l'étiquetage morphosyntaxique (Part-of-Speech tagging). Pour chaque mot de la séquence en entrée ("Janet will back the bill"), un embedding est passé aux couches RNN. Chaque état caché $h$ produit, via une couche softmax, une distribution de probabilité sur l'ensemble des étiquettes (tags). L'opération argmax sélectionne l'étiquette la plus probable à chaque étape de temps (par exemple, "NNP" pour Janet, "MD" pour will, "VB" pour back, etc.).

### Recurrent neural networks for sequence classification
* **FFN**: feed forward classification
* **Training**: No need for intermediate prediction: end-to-end training

#### Description du schéma
Le schéma décrit une architecture RNN de type "many-to-one" utilisée pour la classification de séquences globales (comme l'analyse de sentiment d'une phrase). La séquence d'entrée ($x_1, x_2, x_3, ..., x_n$) est ingérée séquentiellement par le RNN. Aucune prédiction intermédiaire n'est effectuée. Seul le tout dernier état caché ($h_n$), qui est censé condenser l'information de toute la séquence, est passé à un réseau de neurones feed-forward (FFN) suivi d'un softmax pour produire la classification finale de la séquence.

### Recurrent neural networks for generation
* **Mode**: Auto-regressive generation mode

#### Description du schéma
Ce schéma détaille le processus de génération de texte "auto-régressive" par un RNN. À l'étape initiale, un symbole de début de phrase `<S>` est fourni en entrée. Le RNN calcule un état caché et la couche softmax produit une probabilité sur le vocabulaire. Un mot est échantillonné ("So"), et ce même mot prédit est utilisé comme nouvelle entrée (Input Word) pour l'étape de temps suivante, pour générer le mot d'après ("long"). Ce processus en chaîne continue jusqu'à la génération complète de la phrase.

### Recurrent neural networks architecture
* **Stacked RNN**: deep neural networks
* **Performance**: Better performance
* **Complexity**: Learn representation with increasing complexity
* **Cost**: Higher training cost

#### Description du schéma
Ce schéma représente un RNN profond, ou "Stacked RNN". Au lieu d'une seule couche cachée récurrente, il y a ici trois couches (RNN 1, RNN 2, RNN 3) empilées les unes sur les autres. L'entrée $x_i$ est traitée par le RNN 1, dont la sortie (l'état caché courant) sert d'entrée au RNN 2, dont la sortie sert d'entrée au RNN 3, qui produit enfin la prédiction $y_i$. Chaque couche maintient également ses propres connexions récurrentes horizontales.

### Recurrent neural networks architecture (Bi-directional)
* **Bi-directional RNN**: Use left and right context
* **Utility**: Better performance for sentence classification and sequence labelling (POS, NER)

#### Description du schéma
Ce schéma illustre une architecture RNN bidirectionnelle. Pour une séquence d'entrée donnée ($x_1, x_2, x_3, ..., x_n$), il y a deux couches RNN distinctes. RNN 1 lit la séquence de gauche à droite (sens normal), tandis que RNN 2 lit la séquence de droite à gauche (en ordre inverse). Pour chaque étape de temps, les états cachés résultant de ces deux lectures opposées sont concaténés ("concatenated outputs") pour former la représentation finale avant de produire la prédiction $y_i$. Cela permet à chaque prédiction d'avoir conscience du contexte passé et futur.

### Recurrent neural networks: training
* **Difficulty**: Recurrent neural networks have long been considered difficult to train: as the number of time steps increases, it becomes harder to train neurons that are far from the current time step.
* **Problems**:
    * This is the vanishing gradient problem (Bengio 1994).
    * Another issue with these networks is the gradient explosion: exceeding numerical capacity, neuron saturation.

### Recurrent neural networks: training (LSTM)
* **Solution**: To solve the problem of vanishing gradient, a mechanism of memories and gates has been introduced into the recurrent cell: the LSTM (long short-term memory) model [Hochreiter1997]
* **Gates**:
    * The **Forget gate** deletes useless information from the context
    * The **Input gate** selects which information to add to the current context
    * The **Output gate** selects which information to add to the current hidden state

#### Description du schéma
Deux schémas comparent la structure interne d'une cellule RNN classique et d'une cellule LSTM. Le schéma du haut montre une cellule RNN standard où l'état précédent et l'entrée courante sont simplement combinés et passés à travers une fonction tanh. Le schéma du bas détaille la complexité interne d'une cellule LSTM, qui maintient à la fois un état caché ($h$) et un état de cellule ($C$). L'intérieur de la cellule montre plusieurs portes (activations sigmoïdes $\sigma$) couplées à des opérations arithmétiques point à point ($\times$ et $+$), régulant le flux d'informations mémorisées ou oubliées.

### Recurrent neural networks: training (Applications)
* **Mechanism**: This mechanism, whose parameters are learned, allows the network to choose the length of dependencies used for making predictions.
* **Success**: Thanks to this mechanism and a training method (CTC) [Graves 2006], these models have been successfully applied to real-world applications.
* **Paper**: *Offline Handwriting Recognition with Multidimensional Recurrent Neural Networks*, Graves and Schmidhuber, NIPS 2009

#### Description du schéma
Ce schéma montre l'architecture d'un modèle MDLSTM (Multidimensional LSTM) appliqué à la reconnaissance de l'écriture manuscrite hors ligne, spécifiquement sur de l'écriture arabe. On y voit l'image d'entrée (le mot "ميادة") découpée et traitée par une série hiérarchique alternant des couches MDLSTM bidirectionnelles (qui scannent l'image selon de multiples axes spatiaux) et des couches feed-forward. L'output final, une séquence de caractères, est décodé à l'aide d'une fonction de perte CTC (Connectionist Temporal Classification), permettant d'aligner la prédiction séquentielle avec l'image continue.

### Recurrent neural networks: limitations
* **Constraint**: Input and output sequences must have the same length trick: a blank output can be used.
* **Mapping**: The mapping between input and output must be direct: it is difficult to model word reordering in the sequence, as in translation.
    * *Example English*: I love eating mangoes
    * *Example Tagalog*: Mahilig / akong / kumain / ng mangga (fond of / / to eat / mangoes)

### Recurrent neural networks (Different sizes)
* **Dealing with different input/output size**:
    * The same output can be predicted several times, but repetitions are removed from the final output.
    * A special character can be used to model empty prediction and repeated characters.
* **Resource**: https://leimao.github.io/blog/CTC-Alignment-Combinations/

#### Description du schéma
Ce schéma explique le principe de la classification temporelle connexionniste (CTC) pour gérer des tailles d'entrée et de sortie différentes (par exemple, de l'audio vers du texte). L'entrée (un spectrogramme) est découpée en trames qui sont passées à un RNN. Pour chaque trame temporelle, le réseau produit une distribution de probabilité incluant un symbole vide (noté $\epsilon$). Une séquence temporaire brute (ex: h h e $\epsilon$ l l $\epsilon$ e $\epsilon$ o) est générée. L'algorithme CTC fusionne les répétitions adjacentes et supprime les $\epsilon$, permettant à de nombreux alignements différents d'aboutir à la même sortie finale : "hello".

### Encoder-decoder (seq2seq)
* **Encoder**: transforms the input sequence of $X_{i}$ into a sequence of contextual representation $h_{i}$
* **Context**: summarizes the sequence of $h_{i}$ for the decoder
* **Decoder**: generates a sequence of hidden states $\hat{h}_{i}$ from which the output sequence of $y_{i}$ is predicted
* **Advantage**: The input and output sequence length and order are decorrelated

#### Description du schéma
Ce schéma illustre l'architecture conceptuelle Encodeur-Décodeur (seq2seq). À gauche, l'Encodeur lit de manière séquentielle les entrées ($x_1, x_2, ..., x_n$) et compresse toute cette information dans un seul vecteur de "Contexte". Ce vecteur de contexte est ensuite transmis à droite au Décodeur, qui s'en sert pour dérouler et générer une nouvelle séquence de sortie ($y_1, y_2, ..., y_m$), permettant de traduire une séquence de taille $n$ en une séquence de taille $m$.

### Encoder-decoder (seq2seq): Inference
* **Inference with a basic encoder-decoder RNN**:
    * Outputs are ignored for source text.
    * `<s>` and `</s>` are special tokens used to encode the beginning and the end of the sentence.
    * Auto-regressive generation starts with `<s>`.

#### Description du schéma
Ce schéma détaille l'architecture seq2seq appliquée à la traduction de la phrase source anglaise "the green witch arrived" vers la cible espagnole "llegó la bruja verde". Dans la partie bleue claire de l'encodeur, l'entrée est traitée mot par mot pour aboutir au vecteur de contexte final (en vert) $h_n$. Pendant cette phase d'encodage, les prédictions softmax sont ignorées. Le vecteur $h_n$ initialise l'état caché du décodeur. Le processus de génération commence alors en passant un token séparateur spécial `<s>` au décodeur, qui génère le premier mot "llegó", réutilisé en boucle de manière auto-régressive jusqu'à la prédiction du token de fin `</s>`.

### Encoder-decoder (seq2seq): Generation
* **Context vector**: Using context vector at each steps during generation.
* (Aucun point textuel supplémentaire en dehors des annotations du schéma).

#### Description du schéma
Ce schéma est une variante du modèle encodeur-décodeur de base. L'amélioration réside dans la gestion du vecteur de contexte généré par l'encodeur ($h_n^e = c = h_0^d$). Plutôt que d'initialiser seulement le tout premier état du décodeur, ce vecteur de contexte global $c$ est directement connecté et fourni en entrée supplémentaire à chaque étape de la phase de décodage (pour générer $y_1, y_2, y_3, y_4, \dots$). Cela permet de limiter la perte d'informations sur les phrases longues au fur et à mesure que le décodeur génère la sortie.

### Limitation of Encoder-decoder
* **Information bottleneck**: The context vector must encode all the information about the input.
* **Representation**: The beginning of the input sequence is not as well represented as the end : recent context is more present in hidden states of the RNN.
* **Solution**: Possible solution: use all the hidden states from the source sequence using attention to build a dynamic context vector.

### Encoder-decoder with attention
* **Formula**: The context $c_{i}$ is computed as a weighted sum of the hidden states of the encoder:
    * $c_{i} = \sum_{j}\alpha_{ij}h_{j}^{e}$
    * $\alpha_{ij}=softmax(score(h_{i-1}^{d},h_{j}^{e}))$

#### Description du schéma
Ce schéma représente l'introduction du mécanisme d'attention dans l'architecture seq2seq. Au lieu d'utiliser un vecteur de contexte statique unique, le décodeur calcule un contexte dynamique $c_i$ à chaque étape de génération. Le schéma montre des flèches vertes reliant chaque état caché de l'encodeur ($h_1^e, h_2^e, h_3^e, ...$) à un nœud de calcul. Chaque connexion se voit attribuer un "poids d'attention" $\alpha_{ij}$ (ex: .4, .3, .1, .2) qui indique à quel point le décodeur doit prêter attention à ce mot spécifique de l'entrée pour générer la prédiction courante $y_i$. Ces poids dépendent de l'état caché précédent du décodeur $h_{i-1}^d$.

### Contextual word embeddings
* **Limitation of static embeddings (word2vec)**:
    * A single embedding for polysemous words.
    * No use of the word sequence (bag-of-word).
    * No use of word context (static embeddings).
    * No consideration of the document context. Embeddings are independent from one sentence to the next.

#### Description du schéma
Ce schéma démontre le problème de la polysémie pour les plongements de mots statiques, via deux exemples de phrases. D'un côté "an electric guitar and bass player", et de l'autre "stand off to one side". Le mot ambigu "bass" et le mot "player" sont mis en évidence. Un embedding statique associe un seul vecteur invariable à "bass", qu'il s'agisse de la fréquence sonore basse, du poisson (bar), ou de l'instrument de musique, forçant le modèle à moyenner des sens très éloignés sans tenir compte du contexte de la guitare.

### Contextual word embeddings (ELMo)
* **Paper**: *Deep Contextualized Word Representations*, Matthew E. Peters et al., NAACL 2018.
* **Method**: ELMo (Embedding from Language Models).

#### Description du schéma
Ce schéma est une simple capture d'écran du titre, des auteurs, des affiliations et de l'abstract (résumé) de la publication scientifique originelle qui introduit la méthode ELMo, présentée lors de la conférence NAACL HLT 2018.

### Contextual word embeddings: ELMo
* **Layers**: Combine embeddings from different layers.
* **Architecture**: Uses bi-LSTM to compute several contextual embeddings of words.
* **Training**: Pretraining on a large corpus.

#### Description du schéma
Ce schéma technique montre le fonctionnement de la création des embeddings lexicaux ELMo. Pour une séquence d'entrée ("This is `</s>`"), des tokens sont fournis à l'architecture. On y trouve une pile de réseaux de neurones : une couche LSTM qui va vers l'avant (Forward) et une couche LSTM qui va vers l'arrière (Backward), et ce sur plusieurs niveaux (Layer 1, Layer 2...). Le mécanisme ELMo calcule un embedding contextuel final en combinant linéairement les états cachés internes (les $h_{k,j}^{LM}$) issus de toutes ces couches pour un mot donné.

### Contextual word embeddings: ELMo (Tasks)
* **Fine-tuning on a specific task**: $ELMo_{k}^{task}=\gamma^{task}\sum_{j=0}^{L}s_{j}^{task}h_{k,j}^{LM}.$
* **Combination**: ELMo is combined with other embeddings.

#### Description du schéma
Ce schéma illustre la manière dont ELMo s'intègre dans un flux de travail classique en machine learning NLP. Dans un premier temps, un grand corpus (Corpus) sert à pré-entraîner un modèle de langage bidirectionnel profond (biLMs). Une fois entraîné, ce mécanisme est utilisé pour générer des représentations riches. Lorsqu'un modèle effectue une tâche fine spécifique sur la phrase "have a nice", l'entrée habituelle (word2vec, etc.) de chaque mot est concaténée ("Enhance inputs with ELMos") avec l'embedding contextuel profond ELMo généré en fonction du voisinage du mot. Cette entrée augmentée est ensuite envoyée dans les couches supérieures du réseau pour la tâche cible.

### LSTM and NLP Summary
* **Dominance**: Pre-trained word embeddings and LSTMs dominated the field of NLP from 2013 to 2017 (POS tagging, NER, etc.).
* **Evolution**: The idea of the encoder-decoder architecture, along with weighted sums for context, led to the development of **attention**, a fundamental component of Transformers.
* **Strategy**: The pre-training + fine-tuning strategy was developed.