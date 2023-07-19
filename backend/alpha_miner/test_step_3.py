import unittest

from alpha_algorithm import AlphaAlgorithm

class TestStep3(unittest.TestCase):

    def test_L1(self):
        self.x = AlphaAlgorithm('/Users/phuonganhngo/Downloads/datasets/L1.xes')
        self.x.step_1()
        self.x.step_2()
        observed = self.x.step_3()
        expected = ['d']
        self.assertEqual(observed,expected)

    def test_L2(self):
        self.x = AlphaAlgorithm('/Users/phuonganhngo/Downloads/datasets/L2.xes')
        self.x.step_1()
        self.x.step_2()
        observed = self.x.step_3()
        expected = ['d']
        self.assertEqual(observed,expected)

    def test_L3(self):
        self.x = AlphaAlgorithm('/Users/phuonganhngo/Downloads/datasets/L3.xes')
        self.x.step_1()
        self.x.step_2()
        observed = self.x.step_3()
        expected = ['g']
        self.assertEqual(observed,expected)

    def test_L4(self):
        self.x = AlphaAlgorithm('/Users/phuonganhngo/Downloads/datasets/L4.xes')
        self.x.step_1()
        self.x.step_2()
        observed = self.x.step_3()
        expected = ['d', 'e']
        self.assertEqual(observed,expected)

    def test_L5(self):
        self.x = AlphaAlgorithm('/Users/phuonganhngo/Downloads/datasets/L5.xes')
        self.x.step_1()
        self.x.step_2()
        observed = self.x.step_3()
        expected = ['f']
        self.assertEqual(observed,expected)

    def test_L6(self):
        self.x = AlphaAlgorithm('/Users/phuonganhngo/Downloads/datasets/L6.xes')
        self.x.step_1()
        self.x.step_2()
        observed = self.x.step_3()
        expected = ['g']
        self.assertEqual(observed,expected)

    def test_L7(self):
        self.x = AlphaAlgorithm('/Users/phuonganhngo/Downloads/datasets/L7.xes')
        self.x.step_1()
        self.x.step_2()
        observed = self.x.step_3()
        expected = ['c']
        self.assertEqual(observed,expected)

    def test_bill_instances(self):
        self.x = AlphaAlgorithm('/Users/phuonganhngo/Downloads/datasets/billinstances.xes')
        self.x.step_1()
        self.x.step_2()
        observed = self.x.step_3()
        expected = ['deliver bill']
        self.assertEqual(observed,expected)

    def test_flyer_instances(self):
        self.x = AlphaAlgorithm('/Users/phuonganhngo/Downloads/datasets/flyerinstances.xes')
        self.x.step_1()
        self.x.step_2()
        observed = self.x.step_3()
        expected = ['deliver flyer']
        self.assertEqual(observed,expected)

    def test_poster_instances(self):
        self.x = AlphaAlgorithm('/Users/phuonganhngo/Downloads/datasets/posterinstances.xes')
        self.x.step_1()
        self.x.step_2()
        observed = self.x.step_3()
        expected = ['deliver poster']
        self.assertEqual(observed,expected)

    def test_running_example(self):
        self.x = AlphaAlgorithm('/Users/phuonganhngo/Downloads/datasets/running-example.xes')
        self.x.step_1()
        self.x.step_2()
        observed = self.x.step_3()
        expected = ['pay compensation', 'reject request']
        self.assertEqual(observed,expected)

if __name__ == '__main__':
    unittest.main()