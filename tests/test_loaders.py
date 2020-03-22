def test_example_simple_workout_log_data_has_correct_length(data_in_swl_format):
    assert len(data_in_swl_format) == 4, "Data length is wrong"
