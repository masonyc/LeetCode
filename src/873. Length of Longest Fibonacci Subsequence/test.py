import unittest
import solutions


class UnitTest(unittest.TestCase):
    def test_Function(self):
        func = solutions.Solution()
        self.assertEqual(func.lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8]), 5)
        self.assertEqual(func.lenLongestFibSubseq([1, 3, 7, 11, 12, 14, 18]),
                         3)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
