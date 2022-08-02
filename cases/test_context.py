# 测试上下文
# pip install pytest-contexts
class TestWhenAddingTwoNumbers:
    def given_the_two_numbers(self):
        self.x = 4
        self.y = 2

    def when_i_add_them(self):
        self.result = self.x + self.y

    def test_it_should_produce_the_correct_sum(self):
        print(self.result)
        assert self.result == 6
