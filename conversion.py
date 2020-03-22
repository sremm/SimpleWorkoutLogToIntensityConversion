import pandas as pd

from typing import List

intensity_required_columns = [
    "Date",
    "Exercise",
    "Reps",
    "Set",
    "Weight",
    "Rpe",
    "Percentage",
    "Completed",
    "Notes",
]

swl_to_intensity_column_map = {
    "Date": "Date",
    "Exercise": "Exercise",
    "# of Reps": "Reps",
    # "Set",
    "Weight": "Weight",
    # "Rpe",
    # "Percentage",
    # "Completed",
    "Notes": "Notes",
}

completed_yes = 1
completed_no = 0


def get_set_numbers_from_swl_data(data) -> List:
    columns_to_group_by = ["Date", "Time", "Exercise"]
    # group all same day, same excercise with the same time
    grouped = data.groupby(columns_to_group_by)
    # create column for set number for each group
    set_numbers_by_group = grouped.size()
    group_keys = grouped.groups.keys()

    data_with_group_columns_as_index = data.set_index(columns_to_group_by)
    for current_group_keys in group_keys:
        range_end = set_numbers_by_group[current_group_keys] + 1
        data_with_group_columns_as_index.loc[current_group_keys, "Set"] = list(
            range(1, range_end)
        )
    set_numbers = list(data_with_group_columns_as_index["Set"].astype(int))
    return set_numbers


def convert_swl_format_to_intensity_format(
    data_in_swl_format: pd.DataFrame
) -> pd.DataFrame:
    data_in_intensity_format = pd.DataFrame(columns=intensity_required_columns)
    for swl_key, intensity_key in swl_to_intensity_column_map.items():
        data_in_intensity_format[intensity_key] = data_in_swl_format[swl_key]
    # all data in swl are of completed sets
    data_in_intensity_format["Completed"] = completed_yes
    # find set number based on
    data_in_intensity_format["Set"] = get_set_numbers_from_swl_data(data_in_swl_format)
    return data_in_intensity_format
