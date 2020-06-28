import unittest
import mouse_follower_funcs as mff


class MyTestCase(unittest.TestCase):

    def test_calculate_error(self):
        error_vector = mff.calculate_error([0,0])
        self.assertLess(error_vector[0], 2000)
        self.assertLess(error_vector[1], 2000)

    def test_plot(self):
        mff.plot([0,0], [0, 0])

if __name__ == '__main__':
    unittest.main()
