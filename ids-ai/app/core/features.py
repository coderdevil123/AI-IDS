# app/core/features.py

import pandas as pd
import numpy as np
from app.core.logger import get_logger

logger = get_logger("Features")

class FeatureEngineer:
    def add_entropy(self, df: pd.DataFrame, col: str) -> pd.Series:
        logger.info(f"Calculating entropy for {col}")
        probabilities = df[col].value_counts(normalize=True)
        entropy = -np.sum(probabilities * np.log2(probabilities + 1e-9))
        return pd.Series(entropy, index=df.index)

    def burst_ratio(self, df: pd.DataFrame) -> pd.Series:
        if "Flow_Packets/s" not in df.columns:
            return pd.Series(0, index=df.index)
        mean_rate = df["Flow_Packets/s"].mean()
        return (df["Flow_Packets/s"] > mean_rate * 2).astype(int)

    def port_switching_rate(self, df: pd.DataFrame) -> pd.Series:
        if "Dst_Port" not in df.columns:
            return pd.Series(0, index=df.index)
        return df["Dst_Port"].diff().fillna(0).ne(0).astype(int)

    def build(self, df: pd.DataFrame) -> pd.DataFrame:
        logger.info("Building advanced features")

        if "Packet_Length" in df.columns:
            df["packet_entropy"] = self.add_entropy(df, "Packet_Length")

        df["burst_traffic"] = self.burst_ratio(df)
        df["port_switching"] = self.port_switching_rate(df)

        return df
