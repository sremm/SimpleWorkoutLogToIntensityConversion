from conversion import convert_swl_format_to_intensity_format
from loaders import load_simple_workout_log_data

from pathlib import Path
import pandas as pd

import argparse

argparser = argparse.ArgumentParser()

argparser.add_argument(
    "--path_to_export",
    "-p",
    required=True,
    help="Path to strength.csv, export from Simple Workout Log",
)
argparser.add_argument(
    "--save_path",
    default="intensity_formatted_data.csv",
    help="Optional save path for insensity formatted file",
)
args = argparser.parse_args()

path_to_swl_file = Path(args.path_to_export)
save_path = Path(args.save_path)


swl_data = load_simple_workout_log_data(path_to_swl_file)
intensity_formatted_data = convert_swl_format_to_intensity_format(swl_data)

intensity_formatted_data.to_csv(save_path, index=False)
