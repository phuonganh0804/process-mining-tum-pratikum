import unittest

from heuristic_mining import HeuristicMiner

class TestStep1(unittest.TestCase):

    def test_L1(self):
        self.x = HeuristicMiner('/Users/phuonganhngo/Downloads/datasets/L1.xes', 0.4, 0.1, 0.5, 0.4)
        self.x.step_1()
        self.x.step_2()
        observed_input = self.x.input
        expected_input = {'a': ['0'], 'b': ['a'], 'c': ['a'], 'd': [('e', 'b'), ('e', 'c')], 'e': ['a']}
        self.assertEqual(observed_input,expected_input)
        observed_output = self.x.output
        expected_output = {'a': [('e', 'c'), ('e', 'b')], 'b': ['d'], 'c': ['d'], 'd': ['0'], 'e': ['d']}
        self.assertEqual(observed_output,expected_output)

    def test_L2(self):
        self.x = HeuristicMiner('/Users/phuonganhngo/Downloads/datasets/L2.xes', 0.5, 0.1, 1, 0.4)
        self.x.step_1()
        self.x.step_2()
        observed_input = self.x.input
        expected_input = {'a': ['0'], 'b': [('f', 'a')], 'c': [('a', 'f')], 'd': ['b', 'c'], 'e': ['b', 'c'], 'f': ['e']}
        self.assertEqual(observed_input,expected_input)
        observed_output = self.x.output
        expected_output = {'a': ['c', 'b'], 'b': [('d', 'e')], 'c': [('d', 'e')], 'd': ['0'], 'e': ['f'], 'f': ['b', 'c']}
        self.assertEqual(observed_output,expected_output)

    def test_L3(self):
        self.x = HeuristicMiner('/Users/phuonganhngo/Downloads/datasets/L3.xes', 0.5, 0.1, 0.5, 0.4)
        self.x.step_1()
        self.x.step_2()
        observed_input = self.x.input
        expected_input = {'a': ['0'], 'b': [('a', 'f')], 'c': ['b'], 'd': ['b'], 'e': ['d', 'c'], 'f': ['e'], 'g': ['e']}
        self.assertEqual(observed_input,expected_input)
        observed_output = self.x.output
        expected_output = {'a': ['b'], 'b': ['c', 'd'], 'c': ['e'], 'd': ['e'], 'e': [('f', 'g')], 'f': ['b'], 'g': ['0']}
        self.assertEqual(observed_output,expected_output)
    
    def test_L4(self):
        self.x = HeuristicMiner('/Users/phuonganhngo/Downloads/datasets/L4.xes', 0.6, 0.1, 1, 0.4)
        self.x.step_1()
        self.x.step_2()
        observed_input = self.x.input
        expected_input = {'a': ['0'], 'b': ['0'], 'c': [('a', 'b')], 'd': ['c'], 'e': ['c']}
        self.assertEqual(observed_input,expected_input)
        observed_output = self.x.output
        expected_output = {'a': ['c'], 'b': ['c'], 'c': [('d', 'e')], 'd': ['0'], 'e': ['0']}
        self.assertEqual(observed_output,expected_output)

    def test_L5(self):
        self.x = HeuristicMiner('/Users/phuonganhngo/Downloads/datasets/L5.xes', 0.6, 0.1, 1, 0.4)
        self.x.step_1()
        self.x.step_2()
        observed_input = self.x.input
        expected_input = {'a': ['0'], 'b': [('a', 'd')], 'c': ['b'], 'd': ['c'], 'e': ['a'], 'f': ['b', 'e']}
        self.assertEqual(observed_input,expected_input)
        observed_output = self.x.output
        expected_output = {'a': ['b', 'e'], 'b': [('f', 'c')], 'c': ['d'], 'd': ['b'], 'e': ['f'], 'f': ['0']}
        self.assertEqual(observed_output,expected_output)

    def test_L6(self):
        self.x = HeuristicMiner('/Users/phuonganhngo/Downloads/datasets/L6.xes', 0.5, 0.1, 1, 0.4)
        self.x.step_1()
        self.x.step_2()
        observed_input = self.x.input
        expected_input = {'a': ['0'], 'b': ['0'], 'c': ['a'], 'd': ['b'], 'e': ['a'], 'f': ['b'], 'g': [('d', 'c'), ('d', 'e'), ('f', 'c'), ('f', 'e')]}
        self.assertEqual(observed_input,expected_input)
        observed_output = self.x.output
        expected_output = {'a': ['e', 'c'], 'b': ['f', 'd'], 'c': ['g'], 'd': ['g'], 'e': ['g'], 'f': ['g'], 'g': ['0']}
        self.assertEqual(observed_output,expected_output)

    # loop one
    def test_L7(self):
        self.x = HeuristicMiner('/Users/phuonganhngo/Downloads/datasets/L7.xes', 0.5, 0.1, 1, 0.4)
        self.x.step_1()
        self.x.step_2()
        observed_input = self.x.input
        expected_input = {'a': ['0'], 'b': ['a', 'b'], 'c': ['b', 'a']}
        self.assertEqual(observed_input,expected_input)
        observed_output = self.x.output
        expected_output = {'a': ['b', 'c'], 'b': ['b', 'c'], 'c': ['0']}
        self.assertEqual(observed_output,expected_output)

    def test_bill_instances(self):
        self.x = HeuristicMiner('/Users/phuonganhngo/Downloads/datasets/billinstances.xes', 0.7, 0.1, 1, 0.4)
        self.x.step_1()
        self.x.step_2()
        observed_input = self.x.input
        expected_input = {'deliver bill': ['print bill'], 'print bill': ['write bill'], 'write bill': ['0']}
        self.assertEqual(observed_input,expected_input)
        observed_output = self.x.output
        expected_output = {'deliver bill': ['0'], 'print bill': ['deliver bill'], 'write bill': ['print bill']}
        self.assertEqual(observed_output,expected_output)
    
    #loop two
    def test_flyer_instance(self):
        self.x = HeuristicMiner('/Users/phuonganhngo/Downloads/datasets/flyerinstances.xes', 0.7, 0.1, 0.5, 0.4)
        self.x.step_1()
        self.x.step_2()
        observed_input = self.x.input
        expected_input = {'deliver flyer': ['print flyer'], 'design flyer': [('receive flyer order', 'send draft to customer')], 'print flyer': ['send draft to customer'], 'receive flyer order': ['0'], 'send draft to customer': ['design flyer']}
        self.assertEqual(observed_input,expected_input)
        observed_output = self.x.output
        expected_output = {'deliver flyer': ['0'], 'design flyer': ['send draft to customer'], 'print flyer': ['deliver flyer'], 'receive flyer order': ['design flyer'], 'send draft to customer': [('design flyer', 'print flyer')]}
        self.assertEqual(observed_output,expected_output)

    def test_poster_instances(self):
        self.x = HeuristicMiner('/Users/phuonganhngo/Downloads/datasets/posterinstances.xes', 0.7, 0.1, 1, 0.4)
        self.x.step_1()
        self.x.step_2()
        observed_input = self.x.input
        expected_input = {'deliver poster': ['print poster'], 'design photo poster': ['receive order and photo'], 'print poster': ['design photo poster'], 'receive order and photo': ['0']}
        self.assertEqual(observed_input,expected_input)
        observed_output = self.x.output
        expected_output = {'deliver poster': ['0'], 'design photo poster': ['print poster'], 'print poster': ['deliver poster'], 'receive order and photo': ['design photo poster']}
        self.assertEqual(observed_output,expected_output)

    
    def test_running_example(self):
        self.x = HeuristicMiner('/Users/phuonganhngo/Downloads/datasets/running-example.xes', 0.3, 0.1, 0.5, 2)
        self.x.step_1()
        self.x.step_2()
        observed_input = self.x.input
        expected_input = {'check ticket': [('register request', 'reinitiate request')], 'decide': ['check ticket', ('examine casually', 'examine thoroughly')], 'examine casually': [('register request', 'reinitiate request')], 'examine thoroughly': [('reinitiate request', 'register request')], 'pay compensation': ['decide'], 'register request': ['0'], 'reinitiate request': ['decide'], 'reject request': ['decide']}
        self.assertEqual(observed_input,expected_input)
        observed_output = self.x.output
        expected_output = {'check ticket': ['decide'], 'decide': [('reinitiate request', 'pay compensation'), ('reinitiate request', 'reject request'), ('pay compensation', 'reject request')], 'examine casually': ['decide'], 'examine thoroughly': ['decide'], 'pay compensation': ['0'], 'register request': ['check ticket', ('examine casually', 'examine thoroughly')], 'reinitiate request': ['check ticket', ('examine thoroughly', 'examine casually')], 'reject request': ['0']}
        self.assertEqual(observed_output,expected_output)


if __name__ == '__main__':
    unittest.main()