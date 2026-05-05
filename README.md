# NVDA Price Prediction - XGBoost Trading Strategy

This repository implements an algorithmic trading strategy for NVIDIA (NVDA) using Gradient Boosting Machine Learning. The project focuses on short term price forecasting and is designed for seamless deployment on the QuantConnect Lean Engine platform.

## Project Overview

The core of this strategy utilizes an XGBoost Regressor to forecast the next closing price. The model integrates raw market data with technical indicators and cyclical time features to capture complex intraday dynamics.

## Repository Structure

| Directory / File | Technical Purpose |
| :--- | :--- |
| `XGBOOST/main.py` | Deployment script for the QuantConnect Lean Engine |
| `XGBOOST/research.ipynb` | Core research environment for training and visualization |
| `XGBOOST/model/` | Serialized binary models in .bst format for native execution |
| `PPE_Presentation.ipynb` | Comprehensive presentation of project methodology and results |
| `XGBOOST.ipynb` | Alternative training and feature engineering notebook |
| `requirements.txt` | Configuration of the Python environment and dependencies |

## Quantitative Features

*   **Technical Indicators**: Integration of RSI, PPO, MACD, OBV, and Rate of Change to define market momentum.
*   **Cyclical Encoding**: Transformation of time features using Sine and Cosine functions to preserve the circular nature of hours and days.
*   **Feature Scaling**: Application of MinMaxScaler to ensure optimal performance for the gradient boosting regressor.
*   **Model Serialization**: Export of models as binary .bst files to ensure native compatibility with Lean Engine environments.

## Technical Stack

*   **Language**: Python 3.11
*   **Machine Learning**: XGBoost, Scikit-Learn
*   **Data Analysis**: Pandas, NumPy, yfinance
*   **Execution Platform**: QuantConnect Lean Engine
*   **Visualization**: Matplotlib

## Implementation Workflow

1.  **Research**: Data acquisition and feature engineering are conducted within the research notebooks.
2.  **Training**: The XGBoost model is trained on historical OHLCV data and validated using an out of sample test set.
3.  **Deployment**: The serialized model is loaded into the QuantConnect environment for backtesting and live execution.

## Disclaimer

This repository is for educational purposes only. Trading involves significant risk and past performance is not indicative of future results. It is essential to conduct thorough risk assessment before deploying capital in financial markets.
