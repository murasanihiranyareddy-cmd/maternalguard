# Maternal Guard – Setup & Run

## Install dependencies
pip install -r requirements.txt

## Run the app
streamlit run Home.py

## File structure
maternal_guard/
├── Home.py                    ← Landing page
├── maternal_model.pkl         ← Your ML model (place here)
├── requirements.txt
└── pages/
    ├── 1_AI_Risk_Detector.py  ← Input form + prediction
    ├── 2_Emergency_SOS.py     ← SOS trigger + donor alerts
    ├── 3_Donor_Network.py     ← Registration + directory
    └── 4_Dashboard.py         ← Charts + analytics
