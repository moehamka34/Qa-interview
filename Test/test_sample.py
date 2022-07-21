# content of test_sample.py
# just to see if pytest is working 
def func(x):
    return x + 1


def test_answer():
    assert func(4) == 5


