import asyncio

import pytest


class TestAsyncio(object):
    @pytest.mark.asyncio
    def test_1(self, event_loop):
        res = event_loop.run_until_complete(asyncio.wait([self.demo_func() for _ in range(10)]))
        print(res)

    async def demo_func(self):
        print("haha")
        await asyncio.sleep(1)
