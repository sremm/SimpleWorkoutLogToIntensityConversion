from pathlib import Path
import pandas as pd


def load_simple_workout_log_data(path_to_file):
    return pd.read_csv(path_to_file, index_col=None)

