import unittest


class Test(unittest.TestCase):
    def test_empty(self):
        self.assertNotEqual(mark1, [])


def avg(marks):
    assert len(marks) != 0
    return sum(marks)/len(marks)


mark1 = [1]
if __name__ == '__main__':
    unittest.main()
