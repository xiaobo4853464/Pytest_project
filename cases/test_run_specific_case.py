import pytest


# terminal exec "pytest -m 'case' -k '2' -W=ignore"


class TestRunSpecificCase(object):
    @pytest.mark.case(id=1)
    def test_1(self):
        print("haha1")

    @pytest.mark.case(id=2)
    def test_2(self):
        print("haha2")

    @pytest.mark.case(id=3)
    def test_3(self):
        print("haha3")
