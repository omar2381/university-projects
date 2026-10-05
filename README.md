# University projects

Coursework and personal projects from my computer science degree, 2022.
Each folder is a self-contained project with its own README explaining what it
does and how to run it.

They were fourteen separate repositories until October 2026; they are collected
here so the work can be read in one place. Nothing has been rewritten to look
better than it was — this is first- and second-year code, and it reads like it.

## Data and machine learning

| Project | What it does | Built with |
|---|---|---|
| [fhir-patient-pipeline](fhir-patient-pipeline) | Parses FHIR R4 patient bundles into tables: conditions, observations, medications, claims | Python, pandas |
| [ml-fairness-adult-income](ml-fairness-adult-income) | Measures and mitigates racial bias in an income classifier using disparate impact | Python, scikit-learn, AIF360 |
| [covid-outcome-prediction](covid-outcome-prediction) | Predicts patient outcomes from open line-list data; compares Bayesian ridge, logistic regression and k-NN | Python, scikit-learn, Jupyter |
| [web-scraping-word2vec](web-scraping-word2vec) | Scrapes BBC News for cyber security terms and measures their similarity | Python, BeautifulSoup, Word2Vec |
| [wikidata-mp-birthplaces](wikidata-mp-birthplaces) | Maps where UK MPs were born, from Wikidata SPARQL queries and reverse geocoding | Python, SPARQL |

## Machine learning from Colab

Coursework written in Google Colab rather than committed at the time, so these
arrived later than the rest. Cell outputs were stripped before committing.

| Project | What it does | Built with |
|---|---|---|
| [td3-bipedal-walker](td3-bipedal-walker) | A TD3 agent learning to walk in BipedalWalker, with a decaying exploration-noise schedule | Python, PyTorch, OpenAI Gym |
| [fastgan-image-generation](fastgan-image-generation) | A lightweight GAN generating CIFAR-10 and STL-10 images, with LPIPS perceptual loss and DiffAugment | Python, PyTorch |

## Algorithms

| Project | What it does | Built with |
|---|---|---|
| [tsp-search-heuristics](tsp-search-heuristics) | Travelling salesman heuristics: 2-opt, and a Lin-Kernighan style 2-opt/3-opt search with greedy starts | Python |
| [algorithms-data-structures-exercises](algorithms-data-structures-exercises) | Hash probing, digit-factorial cycles, longest palindromic substring, k-way quicksort | Python |
| [dna-sequence-alignment](dna-sequence-alignment) | DNA sequence alignment: brute force against dynamic programming | Python |
| [graph-colouring-bfs](graph-colouring-bfs) | Greedy graph colouring and breadth-first search | Python, NetworkX |
| [hamming-codes](hamming-codes) | Repetition and Hamming error-correcting codes | Python |

## Systems and interfaces

| Project | What it does | Built with |
|---|---|---|
| [python-chat-server](python-chat-server) | Multi-user TCP chat room: threaded server, desktop client, chat commands | Python, sockets, Tkinter |
| [pokemon-data-finder](pokemon-data-finder) | Search page and chart over a Pokemon dataset, served by a small API | Node.js, Express, D3 |
| [image-filters-from-scratch](image-filters-from-scratch) | Light leak, pencil sketch, smoothing and swirl effects, written pixel by pixel | Python, NumPy, OpenCV |
| [connect4-c](connect4-c) | Connect 4 variant with row rotation and a wrap-around board | C |

## Known issues

Left as they are, and noted here rather than quietly fixed:

- **hamming-codes**: `hammingDecoder` does not decode `hammingEncoder` output — the
  bit ordering disagrees — and it flips a bit when there is no error to correct.
- **pokemon-data-finder**: `index.js` calls port 8090 while `server.js` listens on 8080.
- **dna-sequence-alignment**: `ObjectiveThree.py` is unfinished and does not run to completion.
- **ml-fairness-adult-income**: needs pandas 1.x; it uses APIs removed in 2.x.
- **td3-bipedal-walker**: pinned to `gym[box2d]==0.20.0` and `pyglet==1.5.27`;
  it will not run on current Gym without changes. `max_episodes` is 10, which
  trains nothing — raise it.
- **fastgan-image-generation**: reads from my own Google Drive paths, and needs
  the LPIPS pretrained weights, which are not in this repository.

`pokemon-data-finder` loads its dataset from a separate repository,
[pokemon.csv](https://github.com/omar2381/pokemon.csv), over raw.githubusercontent.com.

## External code referenced

Four repositories I forked during the degree rather than wrote. None of them
contains any of my own commits, so they are recorded here instead of being kept
as copies. The commit listed is the one my fork pointed at, so the state I
actually worked against can be recovered with
`git clone <url> && git checkout <commit>`.

| Used for | Original | Commit | Licence |
|---|---|---|---|
| The brief that [fhir-patient-pipeline](fhir-patient-pipeline) answers | [emisgroup/exa-data-eng-assessment](https://github.com/emisgroup/exa-data-eng-assessment) | `1b78bd6` | none stated |
| Postcode and geolocation lookups behind [wikidata-mp-birthplaces](wikidata-mp-birthplaces) | [ideal-postcodes/postcodes.io](https://github.com/ideal-postcodes/postcodes.io) | `e0edafd` | MIT |
| Reinforcement learning module: a TD3 reference implementation | [nikhilbarhate99/TD3-PyTorch-BipedalWalker-v2](https://github.com/nikhilbarhate99/TD3-PyTorch-BipedalWalker-v2) | `1657d70` | MIT |
| Durham University Computing Society Python examples | [ducompsoc/examples.py](https://github.com/ducompsoc/examples.py) | `d7c6112` | none stated |

The EMIS repository is archived upstream, so it is read-only but still
reachable. My own work for the reinforcement learning module is now in
[td3-bipedal-walker](td3-bipedal-walker); it was written in Colab, which is why
it was not in the fork.
