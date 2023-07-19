import unittest

from alpha_algorithm import AlphaAlgorithm

class TestStep4(unittest.TestCase):

    def test_L1(self):
        self.x = AlphaAlgorithm('/Users/phuonganhngo/Downloads/datasets/L1.xes')
        self.x.step_1()
        self.x.step_2()
        self.x.step_3()
        observed = self.x.step_4()
        expected = [(['a'], ['b']),(['a'], ['c']), (['a'], ['e']), (['b'], ['d']), (['c'], ['d']), (['e'], ['d']), (['a'], ['b', 'e']), (['a'], ['c', 'e']), (['b', 'e'], ['d']), (['c', 'e'], ['d'])]
        self.assertEqual(observed,expected)

    def test_L2(self):
        self.x = AlphaAlgorithm('/Users/phuonganhngo/Downloads/datasets/L2.xes')
        self.x.step_1()
        self.x.step_2()
        self.x.step_3()
        observed = self.x.step_4()
        expected = [(['a'], ['b']),(['a'], ['c']), (['b'], ['d']), (['b'], ['e']), (['c'], ['d']), (['c'], ['e']),(['e'], ['f']),(['f'], ['b']), (['f'], ['c']), (['a', 'f'], ['b']), (['a', 'f'], ['c']), (['b'], ['d', 'e']), (['c'], ['d', 'e'])]
        self.assertEqual(observed,expected)

    def test_L3(self):
        self.x = AlphaAlgorithm('/Users/phuonganhngo/Downloads/datasets/L3.xes')
        self.x.step_1()
        self.x.step_2()
        self.x.step_3()
        observed = self.x.step_4()
        expected = [(['a'], ['b']),(['b'], ['c']), (['b'], ['d']), (['c'], ['e']), (['d'], ['e']), (['e'], ['f']),(['e'], ['g']),(['f'], ['b']), (['a', 'f'], ['b']), (['e'], ['f','g'])]
        self.assertEqual(observed,expected)

    def test_L4(self):
        self.x = AlphaAlgorithm('/Users/phuonganhngo/Downloads/datasets/L4.xes')
        self.x.step_1()
        self.x.step_2()
        self.x.step_3()
        observed = self.x.step_4()
        expected = [(['a'], ['c']),(['b'], ['c']), (['c'], ['d']), (['c'], ['e']), (['a', 'b'], ['c']), (['c'], ['d','e'])]
        self.assertEqual(observed,expected)

    def test_L5(self):
        self.x = AlphaAlgorithm('/Users/phuonganhngo/Downloads/datasets/L5.xes')
        self.x.step_1()
        self.x.step_2()
        self.x.step_3()
        observed = self.x.step_4()
        expected = [(['a'], ['b']),(['a'], ['e']), (['b'], ['c']), (['b'], ['f']), (['c'], ['d']), (['d'], ['b']),(['e'], ['f']),(['a', 'd'], ['b']), (['b'], ['c','f'])]
        self.assertEqual(observed,expected)

    def test_L6(self):
        self.x = AlphaAlgorithm('/Users/phuonganhngo/Downloads/datasets/L6.xes')
        self.x.step_1()
        self.x.step_2()
        self.x.step_3()
        observed = self.x.step_4()
        expected = [(['a'], ['c']),(['a'], ['e']), (['b'], ['d']), (['b'], ['f']), (['c'], ['g']), (['d'], ['g']),(['e'], ['g']),(['f'], ['g']),(['c', 'd'], ['g']), (['c', 'f'], ['g']), (['d', 'e'], ['g']),(['e', 'f'], ['g'])]
        self.assertEqual(observed,expected)

    def test_L7(self):
        self.x = AlphaAlgorithm('/Users/phuonganhngo/Downloads/datasets/L7.xes')
        self.x.step_1()
        self.x.step_2()
        self.x.step_3()
        observed = self.x.step_4()
        expected = [(['a'], ['c'])]
        self.assertEqual(observed,expected)

    def test_bill_instances(self):
        self.x = AlphaAlgorithm('/Users/phuonganhngo/Downloads/datasets/billinstances.xes')
        self.x.step_1()
        self.x.step_2()
        self.x.step_3()
        observed = self.x.step_4()
        expected = [(['print bill'], ['deliver bill']), (['write bill'], ['print bill'])]
        self.assertEqual(observed,expected)

    def test_flyer_instances(self):
        self.x = AlphaAlgorithm('/Users/phuonganhngo/Downloads/datasets/flyerinstances.xes')
        self.x.step_1()
        self.x.step_2()
        self.x.step_3()
        observed = self.x.step_4()
        expected = [(['print flyer'], ['deliver flyer']), (['receive flyer order'], ['design flyer']), (['send draft to customer'], ['print flyer'])]
        self.assertEqual(observed,expected)

    def test_poster_instances(self):
        self.x = AlphaAlgorithm('/Users/phuonganhngo/Downloads/datasets/posterinstances.xes')
        self.x.step_1()
        self.x.step_2()
        self.x.step_3()
        observed = self.x.step_4()
        expected = [(['design photo poster'], ['print poster']), (['print poster'], ['deliver poster']), (['receive order and photo'], ['design photo poster'])]
        self.assertEqual(observed,expected)

    def test_running_example(self):
        self.x = AlphaAlgorithm('/Users/phuonganhngo/Downloads/datasets/running-example.xes')
        self.x.step_1()
        self.x.step_2()
        self.x.step_3()
        observed = self.x.step_4()
        expected = [(['check ticket'], ['decide']), (['decide'], ['pay compensation']), (['decide'], ['reinitiate request']), (['decide'], ['reject request']), (['examine casually'], ['decide']), (['examine thoroughly'], ['decide']), (['register request'], ['check ticket']), (['register request'], ['examine casually']), (['register request'], ['examine thoroughly']), (['reinitiate request'], ['check ticket']), (['reinitiate request'], ['examine casually']), (['reinitiate request'], ['examine thoroughly']), (['decide'], ['pay compensation', 'reinitiate request', 'reject request']), (['examine casually', 'examine thoroughly'], ['decide']), (['register request', 'reinitiate request'], ['check ticket']), (['register request', 'reinitiate request'], ['examine casually', 'examine thoroughly'])]
        self.assertEqual(observed,expected)

if __name__ == '__main__':
    unittest.main()