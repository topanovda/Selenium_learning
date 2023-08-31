import pytest


@pytest.fixture(scope="class")
# область покрытия class означает, что фикстура будет вызываться один раз для класса
def prepare_faces():
    print("^_^", "\n")
    yield
    print(":3", "\n")  # эта часть выполниться только после прогона всех тестов


@pytest.fixture()
def very_important_fixture():
    print(":)", "\n")


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print(":-Р", "\n")


# параметр autouse=True указывает на то, что данная фикстура будет
# запускаться для каждого теста , даже без явного вызова


class TestPrintSmilingFaces:
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        pass
        # какие-то проверки

    def test_second_smiling_faces(self, prepare_faces):
        pass
        # какие-то проверки
