# Customer Churn Prediction

An educational machine-learning project that predicts customer churn from the supplied customer dataset. It includes exploratory analysis, preprocessing, model training, a saved model and scaler, and a Streamlit prediction interface.

## Tech stack
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- Streamlit
- Joblib

## Project workflow
1. Explore the customer dataset in the notebook.
2. Clean and prepare the data.
3. Encode categorical features and scale numerical features.
4. Train and evaluate classification models.
5. Save the trained model and scaler.
6. Load the saved artifacts in the Streamlit app for interactive predictions.

## Repository contents
- `notebook.ipynb` — analysis and model-development notebook.
- `customer_churn_data.csv` — dataset used by the project.
- `app.py` — Streamlit interface.
- `model.pkl` — saved model.
- `scaler.pkl` — saved feature scaler.
- `requirements.txt` — Python dependencies.

## Run locally

```bash
git clone https://github.com/jeetpatilprofessional-blip/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction
python -m venv .venv
```

Activate the environment:

**Windows**
```powershell
.venv\Scripts\Activate.ps1
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

Install dependencies and launch the app:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Important notes
- Use the same feature order and preprocessing steps used during training when making predictions.
- The model's predictions are educational estimates based on the supplied dataset, not guaranteed predictions of future customer behavior.
- Re-run the notebook to verify evaluation metrics before quoting performance figures.
- Only load trusted pickle files; pickle artifacts can execute code when loaded.

## Author
Jeet Patil
