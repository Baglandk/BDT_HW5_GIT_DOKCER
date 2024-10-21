from src.myproject.the_project import add_num


def test_add_num():
    assert add_num(1, 3) == 4


if __name__ == "__main__":
    test_add_num()
