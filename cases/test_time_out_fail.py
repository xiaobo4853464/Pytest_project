"""
测试超时>=5s,强制fail
"""
import time


class Test1(object):
    @classmethod
    def setup_class(cls):
        time.sleep(6)
        print("setup_class")

    def test1(self):
        # pass
        time.sleep(1)
        print("test...")

    @classmethod
    def teardown_class(cls):
        time.sleep(1)
        print("teardown")
