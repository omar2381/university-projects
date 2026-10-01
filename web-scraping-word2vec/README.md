# Cyber Security Keyword Similarity from News Articles

Scrapes BBC News articles for a set of cyber security terms, then trains Word2Vec models on the collected text to measure how closely related each pair of terms is, and plots the result as a heatmap.

University coursework on data collection and cleaning.

## Pipeline

1. **Collect.** For each keyword in `keywords.xlsx`, the script runs a BBC News search, walks 30 pages of results and keeps up to 100 article links that actually mention the keyword. It skips local-news and help pages and removes duplicates.
2. **Clean and store.** It downloads each article, strips out scripts and styling, and writes the visible text to one `.txt` file per keyword.
3. **Measure.** For every pair of keywords, it trains a Word2Vec model on the two keywords' combined articles and scores the pair by cosine similarity, from 0 to 1. Multi-word terms average the similarity of their words. The full matrix is saved to `distance.xlsx`.
4. **Visualise.** It draws the matrix as an annotated Seaborn heatmap and saves it as `heatmap.png`.

The keywords: targeted threat, advanced persistent threat, phishing, DoS attack, malware, computer virus, spyware, malicious bot, ransomware, encryption.

## Running it

```bash
pip install beautifulsoup4 requests pandas openpyxl seaborn nltk "gensim<4" numpy
python -c "import nltk; nltk.download('punkt')"
python scrape_and_compare.py
```

The script uses the gensim 3.x API (`size=`, `model.similarity`). The scraping step depends on the layout of BBC's search pages at the time and may need its link filters updating.

## Tech

Python, BeautifulSoup, requests, NLTK, gensim (Word2Vec), pandas, Seaborn
