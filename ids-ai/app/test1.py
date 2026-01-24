import pandas as pd
from app.core.preprocess import Preprocessor
from app.core.features import FeatureEngineer

df = pd.read_csv("data/raw/sample.csv")

pre = Preprocessor()
fe = FeatureEngineer()

df = pre.process(df, fit=True)
df = fe.build(df)

print(df.head())
