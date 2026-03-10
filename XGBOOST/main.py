from AlgorithmImports import *
import xgboost as xgb
import os
import pickle
import numpy as np

class XGBoostModelTest(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2022, 1, 1)
        self.SetEndDate(2022, 1, 10)
        self.SetCash(100000)

        self.symbol = self.AddEquity("AAPL", Resolution.Daily).Symbol

        # ✅ Utilise un chemin relatif depuis le répertoire du projet
        model_path = os.path.join("XGBOOST", "model", "xgboost.bst")

        if not os.path.exists(model_path):
            self.Debug(f"❌ Model file not found at {model_path}")
            raise FileNotFoundError(f"Model not found at {model_path}")
        
        self.model = xgb.Booster()
        self.model.load_model(model_path)
        self.Debug("✅ XGBoost model loaded successfully")

    def OnData(self, data: Slice):
        if not data.ContainsKey(self.symbol):
            return

        # Test avec une fausse feature
        # Remplace ici par tes vraies features issues du marché ou du CSV
        features = np.array([[1.0, 2.0, 3.0]])  # dummy features
        dmatrix = xgb.DMatrix(features)
        prediction = self.model.predict(dmatrix)

        self.Debug(f"🧠 Prediction: {prediction[0]}")