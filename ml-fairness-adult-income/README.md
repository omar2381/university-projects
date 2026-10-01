# Measuring and Reducing Bias in an Income Classifier

Trains a logistic regression model to predict whether a person earns more than $50K a year, measures how biased its predictions are by race, then applies a bias-mitigation step and measures again.

University coursework on fairness in machine learning.

## Approach

**Data:** the [UCI Adult (Census Income)](https://archive.ics.uci.edu/dataset/2/adult) dataset, included as `adult.csv`.

1. **Preparation.** Encodes the protected attributes (race, sex, national origin) and the income label as binary columns, and the categorical features (job type, marital status, relationship, occupation) as integer codes. Prints how the groups are split in the data: about 85% White and 67% male.
2. **Bias in the data.** Calculates the *disparate impact* of the labels: the rate of the favourable outcome (>$50K) for the unprivileged group divided by the rate for the privileged group. A value of 1.0 means parity; below 0.8 is the usual threshold for concern.
3. **Bias in the model.** Trains a standardised logistic regression (70/30 split) and calculates the disparate impact of its predictions, alongside its accuracy.
4. **Mitigation.** Applies IBM's [AIF360](https://github.com/Trusted-AI/AIF360) `DisparateImpactRemover` (repair level 1.0), which adjusts the feature distributions so they carry less information about race. It then retrains the model and reports accuracy and disparate impact again, showing the fairness/accuracy trade-off.

## Running it

```bash
pip install "pandas<2" numpy seaborn matplotlib scikit-learn aif360
python fairness_analysis.py
```

The script uses `DataFrame.append` and `iteritems`, which were removed in pandas 2.0, so it needs pandas 1.x.

## Tech

Python, pandas, scikit-learn, AIF360
