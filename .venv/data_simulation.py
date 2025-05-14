import pandas as pd
import numpy as np

n_samples = 200
proportion_sick = 0.5
n_sick = int(n_samples * proportion_sick)
n_healthy = n_samples - n_sick

sick_data = pd.DataFrame({
    "wiek": np.random.normal(45, 10, n_sick).astype(int),
    "płeć": np.random.choice(["M", "K"], size=n_sick),
    "temperatura": np.random.normal(38.5, 0.5, n_sick),
    "ciśnienie": np.random.normal(110, 10, n_sick),
    "chory": 1
})

healthy_data = pd.DataFrame({
    "wiek": np.random.normal(45, 10, n_healthy).astype(int),
    "płeć": np.random.choice(["M", "K"], size=n_healthy),
    "temperatura": np.random.normal(36.6, 0.3, n_healthy),
    "ciśnienie": np.random.normal(120, 10, n_healthy),
    "chory": 0
})

data = pd.concat([sick_data, healthy_data], ignore_index=True)
data = data.sample(frac=1).reset_index(drop=True)

print(data.head())
