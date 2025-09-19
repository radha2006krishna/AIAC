from lab_8_3.task1 import is_valid_email

def test_is_valid_email():
    # Valid emails
    assert is_valid_email("user@example.com")
    assert is_valid_email("john.doe@mail.co")
    assert is_valid_email("a_b-c@domain.org")
    assert is_valid_email("user123@domain456.com")
    # Invalid: no @
    assert not is_valid_email("userexample.com")
    # Invalid: no .
    assert not is_valid_email("user@examplecom")
    # Invalid: multiple @
    assert not is_valid_email("user@@example.com")
    # Invalid: starts with special char
    assert not is_valid_email(".user@example.com")
    assert not is_valid_email("@user@example.com")
    # Invalid: ends with special char
    assert not is_valid_email("user@example.com.")
    assert not is_valid_email("user@example.com@")
    # Invalid: only special chars
    assert not is_valid_email("@.")

if __name__ == "__main__":
    test_is_valid_email()
    print("All test cases passed.")