from src.myproject.the_project import is_prime


def test_is_prime():
    assert is_prime(0) == 0
    assert is_prime(1) == 0
    assert is_prime(2) == 1
    assert is_prime(17) == 1


if __name__ == "__main__":
    test_is_prime()
