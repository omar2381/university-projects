# COVID-19 Patient Outcome Prediction

A Jupyter notebook that predicts whether a COVID-19 patient recovered or died, using the open line-list data from the early pandemic, and compares three models.

University coursework on machine learning.

## Data

Downloads the [Open COVID-19 Data Working Group](https://github.com/beoutbreakprepared/nCoV2019) line list: individual case records from around the world. The notebook:

- drops the free-text and administrative columns;
- keeps cases that have an age, sex, location and a recorded outcome;
- maps the 30+ inconsistent outcome labels in the source data ("discharged", "Died", "stable condition", "released from quarantine" and so on) to a binary label: alive (1) or died (0).

**Features:** age, sex, latitude, longitude, whether symptoms were reported, and whether the patient had a chronic disease.

## Models

Each model trains on the first 70% of cases and is tested on the rest. It is scored on accuracy, R², and the Matthews correlation coefficient, which is more informative than accuracy when one outcome is much rarer than the other.

| Model | Notes |
|---|---|
| Bayesian ridge regression | With degree-4 polynomial features; predictions are rounded to a class |
| Logistic regression | Standardised features |
| k-nearest neighbours | k = 16, standardised features |

Each model also plots the distribution of its predicted outcomes.

## Running it

```bash
pip install pandas numpy scikit-learn matplotlib seaborn jupyter
jupyter notebook covid_outcome_prediction.ipynb
```

The first cell downloads and extracts the full dataset archive, which takes a while.

## Tech

Python, pandas, scikit-learn, Jupyter
