📈 XGBoost Trading Strategy - NVIDIA (NVDA) Price Prediction
This project implements an algorithmic trading strategy based on Machine Learning, utilizing XGBoost to predict short-term price movements for NVIDIA (NVDA). The model is developed locally (Jupyter) and designed for deployment on the QuantConnect (Lean Engine) platform.

🚀 Project Overview
The core of this strategy is a Gradient Boosting Regressor that forecasts the next closing price based on a combination of raw market data, technical indicators, and cyclical time-based features.

🛠️ Feature Engineering
To capture market dynamics and intraday seasonality, the model utilizes:

OHLCV Data: Open, High, Low, Volume.

Technical Indicators: RSI, PPO, MACD (with Signal line), OBV, and ROC.

Time Cyclical Encoding: Hour, Minute, and Day features are transformed using Sine/Cosine encoding (e.g., Hour_sin, Hour_cos) to help the model understand the circular nature of time.

Data Normalization: All features and targets are scaled using MinMaxScaler for optimal boosting performance.

🏗️ Repository Structure
Plaintext
Machine Learning/
├── XGBOOST/                # Core Algorithm folder
│   ├── main.py             # QuantConnect deployment script
│   ├── research.ipynb      # Training, R&D, and Visualization
│   └── model/              # Serialized binary models (.bst)
├── data/                   # Backtesting data (locally stored / .gitignored)
├── lean.json               # Lean Engine configuration
└── README.md               # Project Documentation
📊 Model Performance & Visualization
The model's accuracy is measured using RMSE (Root Mean Square Error) on a 10% out-of-sample test set.

Objective: Regression on normalized closing prices.

Serialization: The model is saved as a binary .bst file to ensure native compatibility with the QuantConnect Python environment.

⚙️ Installation & Usage
Prerequisites
Ensure you have the following libraries installed:

Bash
pip install numpy pandas xgboost scikit-learn matplotlib yfinance
How to Run
Training: Run the XGBOOST/research.ipynb notebook to fetch data via yfinance, engineer features, and train the model.

Saving: The script automatically exports the model as xgboost.bst.

Backtesting: Use XGBOOST/main.py within the Lean CLI or QuantConnect IDE to run the strategy against historical data.

⚠️ Disclaimer
This project is for educational purposes only. Trading involves significant risk. Past performance is not indicative of future results. Never trade money you cannot afford to lose.

👨‍💻 Author
Paul Arnaud-Battandier - Market Finance & Machine Learning Enthusiast