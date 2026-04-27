# Deep Learning for Natural Language Processing

## Transformers

**Christopher Kermorvant**
ENSAE
2026

---

## Co-reference resolution

### Description du schéma
Le schéma illustre la compréhension du texte selon le contexte à travers deux phrases :
1. "The duck didn't reach the bank because it was too tired" : Une flèche étiquetée "Grammar" relie "it" à "duck".
2. "The duck didn't reach the bank because it was too far." : Une flèche étiquetée "Semantic context" relie "it" à "bank".
Ces exemples montrent comment "Left and right contexts are needed" (les contextes gauche et droit sont nécessaires) pour résoudre les coréférences de manière correcte.

* How context is used in text understanding
* Co-reference resolution
* The duck didn't reach the bank because it was too tired (Grammar)
* The duck didn't reach the bank because it was too far. (Semantic context)
* Left and right contexts are needed

---

## Embedding with transformers and attention

### Description du schéma
Un diagramme montre le passage de la "Layer k" à la "Layer k+1". Les mots d'entrée sont "The chicken didn't cross the road because it was too tired". Une distribution d'auto-attention ("self-attention distribution") est illustrée par des lignes reliant le mot "it" (dans la Layer k+1) aux mots "chicken" et "road" (dans la Layer k). La ligne vers "chicken" est plus épaisse, illustrant un poids d'attention plus fort. 

* columns corresponding to input tokens
* self-attention distribution
* Embeddings are computed at multiple levels in the stack of layers
* Attention is used to weight the influence of the words in the context
* Left and right contexts can be used
* The processing of one layer can be parallelized

---

## Architecture of a transformers

### Description du schéma
Le schéma global de l'architecture d'un Transformer est présenté. De bas en haut :
1. "Input tokens" (So, long, and, thanks, for)
2. "Input Encoding" (boîtes E et additions avec des encodages de position 1, 2, 3, 4, 5) produisant les vecteurs x1 à x5.
3. "Stacked Transformer Blocks" : une série de blocs empilés contenant des mécanismes de "Multi-head attention" représentés par des barres de couleur. Les blocs traitent les vecteurs $x_i$ en parallèle avec des connexions denses entre eux.
4. "Language Modeling Head" : têtes de modélisation du langage appliquant la fonction U et générant les "logits".
5. "Next token" : les mots prédits en sortie (long, and, thanks, for, all).
Une flèche rouge met en évidence la partie "Multi-head attention" au sein des blocs empilés.

---

## Self-Attention layer (simplified version)

### Description du schéma
Un schéma simplifié d'une couche d'auto-attention ("Self-Attention Layer"). En bas, des vecteurs d'entrée $x_1$ à $x_5$. Chacun de ces vecteurs passe par un bloc "attention". Les flèches montrent que pour calculer la sortie d'un bloc (par exemple le bloc pour $x_5$), le mécanisme d'attention prend en compte tous les vecteurs précédents du contexte ($x_1$ à $x_5$). En haut, les vecteurs de sortie sont notés $a_1$ à $a_5$.

* To compute the output at position i, $a_{i}$, the attention layer considers the context $x_{1}...x_{i}$
* Formule (simplified version) :
  $$a_{i}=\sum_{j\le i}\alpha_{ij}x_{j}$$

---

## Self-Attention layer (simplified version) - Suite

### Description du schéma
Le même schéma simplifié de la couche d'auto-attention est repris.

* Context words similar to the current words should have more weight
* Formules :
  $$score(x_{i},x_{j})=x_{i}\cdot x_{j}$$
  $$\alpha_{ij}=softmax(score(x_{i},x_{j}))\forall j\le i$$
  $$a_{i}=\sum_{j\le i}\alpha_{ij}x_{j}$$

---

## Self-Attention layer (real version)

### Description du schéma
Le schéma simplifié de la couche d'attention est mis à jour pour introduire les concepts de Query, Key et Value pour obtenir la version réelle.

* Query : vector of the current word
* Key : vector of the context word
* Value : vector of the contribution of the context word
* Formules (simplified version vs real version) :
  $$a_{i}=\sum_{j\le i}\alpha_{ij}x_{j}$$ (simplified version)
  $$head_{i}=\sum_{j\le i}\alpha_{ij}v_{j}$$ (real version)

---

## Self-Attention layer (real version) - Formules détaillées

### Description du schéma
Le même schéma d'architecture d'attention est affiché.

* Formules détaillées pour Query, Key, Value et le Score :
  $$q_{i}=x_{i}W^{Q} ; k_{j}=x_{j}W^{K} ; v_{j}=x_{j}W^{V}$$
  $$score(x_{i},x_{j})=\frac{q_{i}\cdot k_{j}}{\sqrt{d_{k}}}$$
  $$\alpha_{ij}=softmax(score(x_{i},x_{j}))\forall j\le i$$
  $$head_{i}=\sum_{j\le i}\alpha_{ij}v_{j}$$
* $W^Q$, $W^K$, and $W^V$ are fixed
* $\sqrt{d_{k}}$ is a normalisation factor

---

## Multi-head attention

* Within a given head, the $W^Q$, $W^K$, and $W^V$ are fixed : the features extracted are of the same kind for each word (morphology, syntax, semantics, ...)
* Multiple heads can extract multiple feature type, on the same word embeddings
* $W^{Qc}$, $W^{Kc}$, and $W^{Vc}$ with $1\le c\le A$ for A attentions heads
* Formules pour les multiples têtes d'attention :
  $$q_{i}^{c}=x_{i}W^{Qc} ; k_{j}^{c}=x_{j}W^{Kc} ; v_{j}^{c}=x_{j}W^{Vc} ; \forall c~1\le c\le A$$

---

## Architecture of a transformers - Input focus

### Description du schéma
Le schéma d'architecture globale est repris, avec cette fois-ci une mise en évidence de la section "Input" et "Input Encoding" située tout en bas, où les mots ("Input tokens") sont convertis en encodages E combinés avec leurs positions.

* Input encoding

---

## Input embeddings

### Description du schéma
Le schéma illustre le processus d'embedding. La phrase "Thanks for all the ..." passe par une fonction "Word2index" qui produit les indices `[5, 4000, 10532, 2224]`. Ensuite, un "One hot encoding" crée une matrice binaire de taille $N \times |V|$. Cette matrice est multipliée par une matrice d'embedding E de taille $|V| \times d$ pour produire la matrice finale "Word embeddings" de taille $N \times d$.

* Thanks for all the ↓
* Word2index
* `[5, 4000, 10532, 2224]`
* One hot encoding
* Matrice $N \times |V|$ (lignes avec des 0 et un seul 1 par ligne) multipliée par E ($|V| \times d$) = Word embeddings ($N \times d$)

---

## Input embeddings - Limitations

### Description du schéma
Rappel visuel de la multiplication matricielle : Matrice One-hot ($N \times |V|$) $\times$ Matrice d'embedding E ($|V| \times d$) = Matrice Word embeddings ($N \times d$).

* Limitations :
* The word embeddings are not context-dependent (they will be in the following layers)
* The word embeddings are not position-dependent
* Attention is not aware of the position

---

## Input embeddings - Position embeddings

### Description du schéma
Ce schéma montre comment les embeddings de position sont ajoutés. Pour chaque mot (ex: "Janet", "will", "back", "the", "bill"), son "Word Embedding" est additionné ("+") avec un "Position Embedding" spécifique à son index (1, 2, 3, 4, 5). Le résultat forme les "Composite Embeddings" (X), qui sont ensuite envoyés au "Transformer Block".

* Simple method : combine each word embedding with the embedding of the index of the word position
* Tableau conceptuel des embeddings de position :
  * 0 : $P_{00}$, $P_{01}$ ... $P_{0d}$
  * 1 : $P_{10}$, $P_{11}$ ... $P_{1d}$
  * 2 : $P_{20}$, $P_{21}$ ... $P_{2d}$
  * 3 : $P_{30}$, $P_{31}$ ... $P_{3d}$
* X = Composite Embeddings (word + position)
* Limitations : the first positions are more frequent than the last positions, so they are better estimated.

---

## Input embeddings - Position embedding (Static method)

* Static method : combine each word embedding with a predefined position embedding
* Tableau des embeddings :
  * 0 : $P_{00}$, $P_{01}$ ... $P_{0d}$
  * 1 : $P_{10}$, $P_{11}$ ... $P_{1d}$
  * 2 : $P_{20}$, $P_{21}$ ... $P_{2d}$
  * 3 : $P_{30}$, $P_{31}$ ... $P_{3d}$
* How to define the predefined position embeddings?
* They should be defined for long sequences (e.g. 10 000 tokens)
* Each position embedding must be different but close to embeddings of similar positions
* Values should be continuous and bounded.

---

## Input embeddings - Position embedding (Sin/Cos functions)

### Description du schéma
Le document montre le tableau des embeddings en haut. En bas, une série de graphiques illustrant les ondes sinusoïdales et cosinusoïdales pour différentes valeurs de k (de k=0 à k=30). Les graphiques montrent comment la fréquence des ondes change selon la position k.

* Using sin and cos
  $$P(k,2i)=sin(\frac{k}{n^{2i/d}})$$
  $$P(k,2i+1)=cos(\frac{k}{n^{2i/d}})$$
* Variables définies :
  * k : position of the word
  * n : constant value
  * d : dimension of the embedding
  * i : coordinate in the embedding

---

## Input embeddings - Position Encoding Visualization

### Description du schéma
Une carte de chaleur (heatmap) illustre l'encodage positionnel. L'axe des ordonnées représente la "Sequence Length" (0 à 100), et l'axe des abscisses représente "Embedding Dimension" (0 à 128). Les couleurs varient de jaune (1.00) à bleu foncé (-0.75), formant des motifs d'ondes distincts. Le côté gauche du graphique présente des alternances rapides, tandis que le côté droit montre des transitions très progressives.

* seq_len=100, d=128, n=100000

---

## Architecture of a transformers - Transformer block focus

### Description du schéma
Le schéma d'architecture globale est de nouveau affiché. Cette fois-ci, la section centrale "Stacked Transformer Blocks" est mise en évidence.

* Transformer block

---

## Transformer block

### Description du schéma
Un zoom détaillé sur l'intérieur d'un "Transformer Block" est présenté. Le flux principal, appelé "Residual stream", traverse le bloc de bas ($x_i$) en haut ($h_i$). À partir de ce flux, des données dérivent vers une couche "Layer Norm", puis une "MultiHead Attention". Le résultat est réintégré au flux principal via une addition (+). Le flux dérive ensuite vers un autre "Layer Norm", puis une couche "Feedforward", et est de nouveau réintégré par une addition (+). Les connexions avec les vecteurs adjacents ($x_{i-1}$, $x_{i+1}$) sont visibles en pointillés vers le MultiHead Attention.

* Feedforward : fully-connected 2-layer network ($d_{h1}=2048$)
* Weights are shared between all positions
* Layer norm : standardized vector
  $$LayerNorm(x)=\gamma\frac{(x-\mu)}{\sigma}+\beta$$
* Weight sharing, normalization and residual connexions

---

## Architecture of a transformers - Language head focus

### Description du schéma
Le schéma d'architecture globale est affiché une nouvelle fois. La partie supérieure "Language Modeling Head", qui convertit les vecteurs internes en probabilités (logits) pour le prochain token, est mise en évidence par une flèche verte étiquetée "Language head".

* Language head

---

## Language model head

### Description du schéma
Ce schéma détaille le processus de la tête de modélisation du langage. Une matrice $h_N^L$ (de taille $1 \times d$) provenant de la "Layer L Transformer Block" est multipliée par une matrice "Unembedding layer U" (de taille $d \times |V|$). Le résultat produit des "Logits" (de taille $1 \times |V|$), qui sont ensuite passés par une fonction "Softmax" pour obtenir des probabilités de mots (Word probabilities $1 \times |V|$), permettant de prédire les mots $y_1, y_2, ... y_V$.

* Language Model Head takes $h^{L}_{N}$ and outputs a distribution over vocabulary V
* Layer L Transformer Block
* Unembedding layer : $U=E^{T}$
* Unembedding : matrix tied to the input embedding matrix E
* $h_{N}^{L}$ de dimension $1 \times d$
* Unembedding layer de dimension $d \times |V|$
* Logits de dimension $1 \times |V|$
* Softmax over vocabulary V
* Word probabilities de dimension $1 \times |V|$
* Softmax for computing $P(y|w_{1}...w_{N})$

---

## Text generation

* How to generate text?
* Random sampling
  * $i=1$
  * $\overline{W_{i}}\sim P$ (prompt text)
  * While $\overline{W_{i}}\ne EOS$
  * $i+=1$
  * $\overline{W_{i}}\sim\mathcal{P}(W|\overline{W}_{<i})$
* Top-k random sampling = limit random sampling to the k most probable words
* Top-p random sampling = limit the random sampling to the words representing the p percent of the probability mass
* Temperature random sampling = random sampling after temperature scaling 
  $$y=softmax(u/\tau)$$

---

## Text generation - Examples of interfaces

### Description du schéma
Deux captures d'écran d'interfaces d'API de modèles de langage sont présentées côte à côte.
1. Interface "Playground" (OpenAI / ChatGPT) : Le modèle sélectionné est "gpt-4o". Une zone encadrée en rouge "Model configuration" met en évidence les curseurs permettant d'ajuster les hyperparamètres : "Temperature" (réglé sur 1.00), "Max tokens" (2048), "Top P" (1.00), "Frequency penalty" (0.00) et "Presence penalty" (0.00).
2. Interface Anthropic Console (Claude) : Le modèle sélectionné est "claude-3-7-sonnet-20250219 latest". Une zone encadrée en rouge met en évidence des curseurs de réglage similaires : "Temperature" (réglé sur 1), "Max tokens" (8192), l'option "Thinking" activée, et "Budget Tokens" (6554).

* ChatGPT
  * Model gpt-4o
  * Model configuration (Temperature: 1.00, Max tokens: 2048, Top P: 1.00, Frequency penalty: 0.00, Presence penalty: 0.00)
* Claude
  * Model claude-3-7-sonnet-20250219 latest
  * Options (Temperature: 1, Max tokens: 8192, Thinking: activé, Budget Tokens: 6554)