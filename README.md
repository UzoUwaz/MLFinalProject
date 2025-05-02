# MLFinalProject

## Team Peacock

### 🏡 Intro and Overview

This repository applies exploratory data analysis, feature engineering, and ensemble learning to predict Airbnb listing prices in Asheville, Boston, Chicago, and New York City. You’ll find city‑specific notebooks (`Asheville_main.ipynb`, `Boston_main.ipynb`, `Chicago_main.ipynb`, `NYC_main.ipynb`).

> **Note:** The notebooks are designed to run in Google Colab. You’ll need a Google account with access to Colab Notebooks and Google Drive to mount your drive and execute the analyses.

---

## 📂 Project Structure

```
MLFinalProject-main/
│
├── data/                                  # Cleaned CSVs used by the notebooks
│   ├── Asheville_listings_cleaned.csv
│   ├── Boston_listings_cleaned.csv
│   ├── chicago_listings_cleaned.csv
│   └── nyc_listings_cleaned.csv 
│
├── Ashville_main.ipynb                    # EDA & modeling for Asheville
├── Boston_main.ipynb                      # EDA & modeling for Boston
├── Chicago_main.ipynb                     # EDA & modeling for Chicago
├── NYC_main.ipynb                         # EDA & modeling for NYC
│
├── project_report_ref.pdf                 # Final report reference
├── Copy of IDS705 Final Report Template.docx
│
└── README.md                              # ← You are here
└── requirements.txt                             

```

---

## 🚀 Getting Started

### 1. Clone & install requirements
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
- **Cleaned data** is already in `/data/`. We've included Asheville, Boston, Chicago, and NYC  
- **Raw Airbnb data** If you need to re-run cleaning or want to add new cities, they must be downloaded from 
  the website, Inside Airbnb. This can be done easily by modifying the first few lines of `data/data_processing.py` to include the needed cities, and running the script via the terminal. The script will automatically download and pre-clean the data.

  ```bash
  python data/data_processing.py
  ```

### 3. Running the notebooks  

> **Note** All the development has been done on Google Colab for this repository --- although it *should* work locally too, we will only provide our workflow on Colab, as that is the only environment we have tested it on. 

#### On Google Colab 
1. Open the notebook in Colab.  
2. Upload the entire repository into the Colab Notebooks folder
3. Mount your Google Drive when prompted:
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```
4. Change directory in the first cell to where you cloned this repo in your Drive:
   ```python
   import os
   os.chdir(r'/content/drive/My Drive/Colab Notebooks/ids705/project')
   ```
5. Run the notebook as needed for NYC, Boston, Ashville, or Chicago to engineer features, do final cleaning on data, EDA, and model.


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
  - Standard metrics (MAE, RMSE, F1, etc.).
  - Evaluation is run on the final best model (XGBoost)

