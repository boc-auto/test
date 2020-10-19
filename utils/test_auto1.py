import pytest

def func(x):
    return x + 1

@pytest.mark.parametrize('a,b',[
    (1,2),
    (5,7),
    (6,10),
    (9,10)
])
def test_answer1(a,b):
    assert func(a) == b

def test_answer2():
    assert func(4) == 5

@pytest.fixture()
def login():
    print('需要登录的model')
    username = 'jerry'
    return username


class TestDemo:
    def test_one(self,login):
        print(f"a,{login}")
    def test_two(self):
        print("b，不需要登录的model")
    def test_three(self,login):
        print(f"c,{login}")

if __name__ == '__main__':
    pytest.main(['test_auto1.py::TestDemo','-v'])































