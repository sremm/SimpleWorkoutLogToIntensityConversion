from pathlib import Path
from loaders import load_simple_workout_log_data


def test_load_simple_workout_log_data():
    path_to_export = Path("test_data") / "strength.csv"
    data = load_simple_workout_log_data(path_to_export)
    assert len(data) == 4, "Data length is wrong"
