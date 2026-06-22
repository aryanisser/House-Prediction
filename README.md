# 🏠 House Price Prediction

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.x-orange?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.x-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-11557C?style=for-the-badge)

*A machine learning project to predict house prices using regression models built with Scikit-learn.*

</div>

---

## 📌 Overview

This project builds a **House Price Prediction** model using various regression algorithms from Scikit-learn. It explores the relationship between property features (area, location, number of rooms, etc.) and their sale prices — covering the complete ML pipeline from data preprocessing to model evaluation.

---

## ✨ Features

- 📊 **Exploratory Data Analysis (EDA)** — Visualize distributions, correlations, and outliers
- 🧹 **Data Preprocessing** — Handle missing values, encode categorical features, feature scaling
- 🤖 **Multiple Regression Models** — Linear Regression, Decision Tree, Random Forest, Gradient Boosting
- 📈 **Model Evaluation** — RMSE, MAE, R² Score comparison across models
- 🔍 **Feature Importance** — Identify the most influential predictors of house price

---

## 🗂️ Project Structure

```
house-price-prediction/
│
├── data/
│   ├── raw/                  # Original dataset
│   └── processed/            # Cleaned & preprocessed data
│
├── notebooks/
│   ├── 01_eda.ipynb          # Exploratory Data Analysis
│   ├── 02_preprocessing.ipynb
│   └── 03_modeling.ipynb     # Model training & evaluation
│
├── src/
│   ├── preprocess.py         # Data cleaning & feature engineering
│   ├── train.py              # Model training script
│   └── evaluate.py           # Evaluation metrics & plots
│
├── models/
│   └── best_model.pkl        # Saved best-performing model
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

| Tool | Purpose |
|---|---|
| `scikit-learn` | ML models, pipelines, metrics |
| `pandas` | Data manipulation |
| `numpy` | Numerical computation |
| `matplotlib` / `seaborn` | Visualization |
| `joblib` | Model serialization |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/house-price-prediction.git
cd house-price-prediction
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Notebook

```bash
jupyter notebook notebooks/03_modeling.ipynb
```

---

## 🧠 Models Used

| Model | R² Score | RMSE |
|---|---|---|
| Linear Regression | ~0.78 | — |
| Decision Tree | ~0.82 | — |
| Random Forest | ~0.91 | — |
| Gradient Boosting | ~0.93 | — |

> *Exact scores depend on dataset and hyperparameters. Random Forest and Gradient Boosting consistently outperform baseline models.*

---

## 📊 Sample Results

```
Best Model   : Gradient Boosting Regressor
R² Score     : 0.93
MAE          : ₹1,20,000
RMSE         : ₹1,85,000
```

---

## 📦 Requirements

```
scikit-learn>=1.0
pandas>=1.5
numpy>=1.23
matplotlib>=3.6
seaborn>=0.12
jupyter
joblib
```

Install all at once:

```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a new branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -m "Add your feature"`
4. Push: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

**Aryan**
B.Tech — Artificial Intelligence & Data Science
Bennett University

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/your-username)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/your-profile)

---

<div align="center">

⭐ If you found this project helpful, please consider giving it a star!

</div>
