import unittest

from heuristic_mining import HeuristicMiner

class TestStep1(unittest.TestCase):

    def test_L1(self):
        self.x = HeuristicMiner('/Users/phuonganhngo/Downloads/datasets/L1.xes', 0.5, 0.1, 1, 0.4)
        observed = self.x.step_1()
        expected = {('a', 'e'): 0.5, ('e', 'd'): 0.5, ('a', 'c'): 0.667, ('c', 'b'): -0.167, ('b', 'd'): 0.667, ('a', 'b'): 0.75, ('b', 'c'): 0.167, ('c', 'd'): 0.75}
        self.assertEqual(observed,expected)

    def test_L2(self):
        self.x = HeuristicMiner('/Users/phuonganhngo/Downloads/datasets/L2.xes', 0.5, 0.1, 1, 0.4)
        observed = self.x.step_1()
        expected = {('a', 'c'): 0.875, ('c', 'b'): -0.095, ('b', 'd'): 0.857, ('b', 'e'): 0.75, ('e', 'f'): 0.875, ('f', 'b'): 0.833, ('b', 'c'): 0.095, ('c', 'd'): 0.875, ('a', 'b'): 0.857, ('c', 'e'): 0.8, ('f', 'c'): 0.667}
        self.assertEqual(observed,expected)
    
    def test_L3(self):
        self.x = HeuristicMiner('/Users/phuonganhngo/Downloads/datasets/L3.xes', 0.5, 0.1, 1, 0.4)
        observed = self.x.step_1()
        expected = {('a', 'b'): 0.8, ('b', 'c'): 0.75, ('c', 'd'): -0.125, ('d', 'e'): 0.75, ('e', 'f'): 0.75, ('f', 'b'): 0.75, ('b', 'd'): 0.8, ('d', 'c'): 0.125, ('c', 'e'): 0.8, ('e', 'g'): 0.8}
        self.assertEqual(observed,expected)

    def test_L4(self):
        self.x = HeuristicMiner('/Users/phuonganhngo/Downloads/datasets/L4.xes', 0.5, 0.1, 1, 0.4)
        observed = self.x.step_1()
        expected = {('a', 'c'): 0.988, ('c', 'd'): 0.989, ('b', 'c'): 0.985, ('c', 'e'): 0.984}
        self.assertEqual(observed,expected)

    def test_L5(self):
        self.x = HeuristicMiner('/Users/phuonganhngo/Downloads/datasets/L5.xes', 0.5, 0.1, 1, 0.4)
        observed = self.x.step_1()
        expected = {('a', 'b'): 0.917, ('b', 'e'): -0.154, ('e', 'c'): 0.167, ('c', 'd'): 0.909, ('d', 'b'): 0.889, ('b', 'f'): 0.923, ('a', 'e'): 0.75, ('e', 'b'): 0.154, ('b', 'c'): 0.9, ('c', 'e'): -0.167, ('e', 'd'): -0.286, ('d', 'e'): 0.286, ('e', 'f'): 0.667}
        self.assertEqual(observed,expected)

    def test_L6(self):
        self.x = HeuristicMiner('/Users/phuonganhngo/Downloads/datasets/L6.xes', 0.5, 0.1, 1, 0.4)
        observed = self.x.step_1()
        expected = {('b', 'f'): 0.8, ('f', 'd'): 0.286, ('d', 'g'): 0.8, ('b', 'd'): 0.667, ('d', 'f'): -0.286, ('f', 'g'): 0.667, ('a', 'e'): 0.75, ('e', 'c'): 0.167, ('c', 'g'): 0.75, ('a', 'c'): 0.667, ('c', 'e'): -0.167, ('e', 'g'): 0.667}
        self.assertEqual(observed,expected)

    def test_L7(self):
        self.x = HeuristicMiner('/Users/phuonganhngo/Downloads/datasets/L7.xes', 0.5, 0.1, 1, 0.4)
        observed = self.x.step_1()
        expected = {('a', 'b'): 0.857, ('b', 'c'): 0.857, ('b', 'b'): 0.833, ('a', 'c'): 0.667}
        self.assertEqual(observed,expected)

    def test_bill_instances(self):
        self.x = HeuristicMiner('/Users/phuonganhngo/Downloads/datasets/billinstances.xes', 0.5, 0.1, 1, 0.4)
        observed = self.x.step_1()
        expected = {('write bill', 'print bill'): 0.999, ('print bill', 'deliver bill'): 0.999}
        self.assertEqual(observed,expected)

    def test_flyer_instance(self):
        self.x = HeuristicMiner('/Users/phuonganhngo/Downloads/datasets/flyerinstances.xes', 0.5, 0.1, 1, 0.4)
        observed = self.x.step_1()
        expected = {('receive flyer order', 'design flyer'): 0.999, ('send draft to customer', 'print flyer'): 0.999, ('print flyer', 'deliver flyer'): 0.999, ('send draft to customer', 'design flyer'): 0.999, ('design flyer', 'send draft to customer'): 0.999}
        self.assertEqual(observed,expected)

    def test_poster_instances(self):
        self.x = HeuristicMiner('/Users/phuonganhngo/Downloads/datasets/posterinstances.xes', 0.5, 0.1, 1, 0.4)
        observed = self.x.step_1()
        expected = {('receive order and photo', 'design photo poster'): 0.999, ('design photo poster', 'print poster'): 0.999, ('print poster', 'deliver poster'): 0.999}
        self.assertEqual(observed,expected)
    
    def test_running_example(self):
        self.x = HeuristicMiner('/Users/phuonganhngo/Downloads/datasets/running-example.xes', 0.5, 0.1, 1, 0.4)
        observed = self.x.step_1()
        expected = {('register request', 'examine casually'): 0.75, ('examine casually', 'check ticket'): 0.286, ('check ticket', 'decide'): 0.857, ('decide', 'reinitiate request'): 0.75, ('reinitiate request', 'examine thoroughly'): 0.5, ('examine thoroughly', 'check ticket'): 0.25, ('decide', 'pay compensation'): 0.75, ('register request', 'check ticket'): 0.667, ('check ticket', 'examine casually'): -0.286, ('examine casually', 'decide'): 0.667, ('register request', 'examine thoroughly'): 0.5, ('decide', 'reject request'): 0.75, ('reinitiate request', 'check ticket'): 0.5, ('reinitiate request', 'examine casually'): 0.5, ('check ticket', 'examine thoroughly'): -0.25, ('examine thoroughly', 'decide'): 0.5}
        self.assertEqual(observed,expected)

if __name__ == '__main__':
    unittest.main()
