import unittest
import solutions


class UnitTest(unittest.TestCase):
    def test_function(self):
        func = solutions.Solution()
        self.assertEqual(func.shortestToChar("loveleetcode", 'e'),
                         [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0])


def main():
    unittest.main()


if __name__ == '__main__':
    main()
