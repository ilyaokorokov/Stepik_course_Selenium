def test_input_text(expected_result, actual_result):
    assert (
        expected_result == actual_result
    ), f"expected {expected_result}, got {actual_result}"


def test_substring(full_string, substring):
    if substring not in full_string:
        print(f"expected '{substring}' to be substring of '{full_string}'")
