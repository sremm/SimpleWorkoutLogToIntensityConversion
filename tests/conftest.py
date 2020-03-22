from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
from loaders import load_simple_workout_log_data
import pytest


@pytest.fixture
def path_to_swl_strength_export():
    return Path("test_data") / "strength.csv"


@pytest.fixture
def data_in_swl_format(path_to_swl_strength_export):
    return load_simple_workout_log_data(path_to_swl_strength_export)
