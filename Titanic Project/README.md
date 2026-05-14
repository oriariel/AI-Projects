# Titanic Survival Predictor

A machine learning project predicting passenger survival on the Titanic using the classic dataset. Built as a first end-to-end ML pipeline — covering data cleaning, feature engineering, model training, evaluation, and comparison.

**Final model accuracy: 83% (Random Forest, cross-validated)**

---

## Results

| Model | CV Accuracy | Std Dev |
|---|---|---|
| Random Forest | 81.4% | ±6.3% |
| Logistic Regression | 79.2% | ±4.3% |
| SVM (with scaling) | ~82–83% | ±4–5% |

Cross-validation used 5 folds across the full dataset — a more reliable estimate than a single train/test split.

---

## What I built

A full sklearn pipeline that takes raw CSV data to a trained, evaluated classifier:

1. **Exploratory analysis** — identified missing data patterns, class imbalance (62% died / 38% survived), and strong predictors before touching the model
2. **Feature engineering** — created `FamilySize` and `IsAlone` from `SibSp` and `Parch`; dropped `Cabin` (77% missing), `Ticket`, and `Name` as uninformative
3. **Imputation** — filled `Age` with the median (177 missing values, ~20%); filled 2 missing `Embarked` with mode ('S')
4. **Encoding** — mapped `Sex` to binary; one-hot encoded `Embarked` with `drop_first=True` to avoid multicollinearity
5. **Model comparison** — evaluated three classifiers with 5-fold cross-validation rather than a single split
6. **Scaling** — discovered SVM dropped to 67% without `StandardScaler` due to `Fare`'s large range (0–512) dominating kernel distance calculations; wrapped distance-based models in a Pipeline

---

## Key findings

**Sex was the strongest predictor** — women survived at 74% vs men at 19%, consistent with "women and children first" evacuation protocol. The model assigned Sex ~25–30% feature importance.

**Fare and Pclass together encode socioeconomic status** — first-class passengers had dramatically higher survival rates. Fare also captured within-class variation that Pclass alone missed.

**Class imbalance matters for evaluation** — with 62% of passengers dying, a naive model that always predicts "died" would score 62% accuracy. Reporting precision, recall, and F1 separately (especially for the minority survivor class) gives a more honest picture. My model achieved 80% precision and 77% recall on survivors.

**SVM needs feature scaling** — tree-based models (Random Forest) are invariant to feature scale because splits are based on rank order. Distance-based models (SVM, Logistic Regression) are not. Wrapping them in a StandardScaler Pipeline brought SVM from 67% to competitive performance.

**Stability vs accuracy tradeoff** — Logistic Regression was the most stable model (±4.3% variance across folds) despite lower mean accuracy. In a production setting where consistency matters, this would be worth considering over the marginally higher but less stable Random Forest.

---

## What I would do differently

- **Extract titles from Name** (Mr, Mrs, Miss, Master) before dropping the column — these encode both gender and age information and are a well-known feature on this dataset
- **Use IterativeImputer for Age** instead of median fill — Age correlates with Pclass and Sex, so a model-based imputation would be more accurate
- **Log-transform Fare** — it's heavily right-skewed (skew > 4) which hurts distance-based models even after scaling
- **Tune hyperparameters** with GridSearchCV — especially `max_depth` and `min_samples_split` for Random Forest to reduce the ±6.3% variance
- **Add SHAP values** for interpretability — feature importance from Random Forest shows global importance but not directional effect per prediction

---

## Setup

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
python titanic_predictor.py
```

Dataset: [Titanic - Machine Learning from Disaster](https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv)

---

## Stack

Python · pandas · scikit-learn · matplotlib · seaborn
