# app/core/preprocess.py

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from app.core.logger import get_logger

logger = get_logger("Preprocess")

class Preprocessor:
    def __init__(self):
        self.scaler = StandardScaler()

    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        logger.info("Cleaning data")
        df = df.replace([np.inf, -np.inf], np.nan)
        df = df.dropna()
        return df

    def encode_protocol(self, df: pd.DataFrame) -> pd.DataFrame:
        if "Protocol" in df.columns:
            logger.info("Encoding protocol column")
            df = pd.get_dummies(df, columns=["Protocol"], drop_first=True)
        return df

    def normalize(self, df: pd.DataFrame, fit: bool = False) -> pd.DataFrame:
        numeric_cols = df.select_dtypes(include=[np.number]).columns

        if fit:
            logger.info("Fitting scaler")
            df[numeric_cols] = self.scaler.fit_transform(df[numeric_cols])
        else:
            df[numeric_cols] = self.scaler.transform(df[numeric_cols])

        return df

    def process(self, df: pd.DataFrame, fit: bool = False) -> pd.DataFrame:
        df = self.clean(df)
        df = self.encode_protocol(df)
        df = self.normalize(df, fit)
        return df
