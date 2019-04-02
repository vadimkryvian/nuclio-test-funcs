class TestClass(object):
    def __init__(self, event):
        self.nums = event.body.values()

    @property
    def get_sum(self):
        return sum(self.nums)
