import pytest


@pytest.mark.parametrize('people', [('male', 20), ('female', 30)])
def test1(people):
    assert isinstance(people[0], str)
    print(people[0])



# ============ with ids
people2 = [('male', 21), ('female', 31)]
people2_id = ['{},{}'.format(p[0], p[1]) for p in people2]


@pytest.mark.parametrize('people2', people2, ids=people2_id)
def test2(people2):
    assert isinstance(people2[0], str)
    print(people2)
