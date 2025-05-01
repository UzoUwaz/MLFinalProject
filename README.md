# MLFinalProject

## Team Peacock 
## 🏡 Predicting AirBnb Prices and characterizing best features for pricing models 

This repository explores and predicts Airbnb listing prices across multiple U.S. cities by combining exploratory data analysis (EDA), feature engineering, and ensemble machine learning. You’ll find Jupyter notebooks for Asheville, Boston, and Chicago, plus a consolidated pipeline in `main_copy.ipynb`.

---

## 📂 Project Structure

```
MLFinalProject-main/
│
├── data/                                  # Cleaned CSVs used by the notebooks
│   ├── Asheville_listings_cleaned.csv
│   ├── Boston_listings_cleaned.csv
│   ├── chicago_listings_cleaned.csv
│   ├── split_1.csv through split_4.csv    # Intermediate train/val splits
│   └── test.csv                           # Hold-out test set
│
├── Ashville_main_copy.ipynb               # EDA & modeling for Asheville
├── Boston_of_main_copy.ipynb              # EDA & modeling for Boston
├── Copy_of_Chicaog_main_copy.ipynb        # EDA & modeling for Chicago
├── main_copy.ipynb                        # Unified pipeline & feature engineering
│
├── project_report_ref.pdf                 # Final report reference
├── Copy of IDS705 Final Report Template.docx
│
└── README.md                              # ← You are here
└── requirements.txt                             

```

---

## 🚀 Getting Started

### 1. Clone & install  
```bash
git clone https://github.com/your-username/MLFinalProject.git
cd MLFinalProject
python3 -m venv venv            # (optional but recommended)
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
pip install --upgrade pip
pip install -r requirements.txt
```

### 2. Data setup  
- **Cleaned data** is already in `/data/`.  
- **Raw Airbnb data** (if you need to re-run cleaning) must be downloaded from [https://www.kaggle.com/datasets/mohithsairamreddy/salary-data] and placed in `/data/raw/`.  

### 3. Running the notebooks  

#### On Google Colab (recommended)
1. Open the notebook in Colab.  
2. Mount your Google Drive when prompted:
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```
3. Change directory to where you cloned this repo in your Drive:
   ```python
   %cd /content/drive/MyDrive/path/to/MLFinalProject
   ```
4. Run each cell, starting with `main_copy.ipynb`.

#### Locally  
1. In each notebook, **comment out** or **remove** the `drive.mount()` and `os.chdir()` lines.  
2. Make sure your working directory is the root of this project (where `data/` lives).  
3. Launch Jupyter:
   ```bash
   jupyter notebook
   ```
4. Open `main_copy.ipynb` and run cells top to bottom.

---

## 🧪 What’s Inside

- **EDA & Profiling**  
  - City-specific notebooks: explore distributions, outliers, and feature correlations.  
  - (Optional) `ydata_profiling.ProfileReport` for quick data overviews.

- **Feature Engineering**  
  - Haversine distance between lat/lon coordinates.  
  - Amenity parsing, text-based features (TF-IDF on descriptions & reviews).  
  - Host signals (acceptance rate, response metrics).

- **Models**  
  - Baselines: DummyRegressor, Ridge.  
  - Tree ensembles: RandomForest, ExtraTrees, XGBoost, LightGBM, CatBoost.  
  - StackingRegressor to combine strengths.

- **Evaluation**  
  - Standard metrics (MAE, RMSE).  
  - Train/validation/test splits under `/data/split_*.csv`.

