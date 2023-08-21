# print(
#     "Let's count together: {}, then goes {}, and then {}".format("one", "two", "three")
# )


# str1 = "one"
# str2 = "two"
# str3 = "three"
# print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")


# actual_result = "abrakadabra"
# print(f"Wrong text, got {actual_result}, something wrong")

expected_result = 8
actual_result = 11


def test_input_text(expected_result, actual_result):
    assert f"expected {expected_result}, got {actual_result}"
