from conversion import convert_swl_format_to_intensity_format
from conversion import intensity_required_columns

import pytest


@pytest.fixture
def data_converted_from_swl_to_intensity(data_in_swl_format):
    return convert_swl_format_to_intensity_format(data_in_swl_format)


class TestSwlToIntensityConversion:
    def test_columns_are_correct(self, data_converted_from_swl_to_intensity):
        assert (
            list(data_converted_from_swl_to_intensity.columns)
            == intensity_required_columns
        ), "Converted data columns are wrong"

    def test_length_is_correct(self, data_converted_from_swl_to_intensity):
        assert (
            len(data_converted_from_swl_to_intensity) == 4
        ), "Length of converted data is wrong"

    def test_no_value_in_set_column_is_NaN(self, data_converted_from_swl_to_intensity):
        assert (
            data_converted_from_swl_to_intensity["Set"].notna().any()
        ), "No value in Set column should be NaN"

    def test_set_numbers_are_correct(self, data_converted_from_swl_to_intensity):
        excpected_set_values = [1, 2, 1, 2]
        set_values = data_converted_from_swl_to_intensity["Set"].values
        assert all(
            set_values == excpected_set_values
        ), f"Set values are wrong: {set_values} != {excpected_set_values}"
