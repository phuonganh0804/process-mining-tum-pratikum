from backend.alpha_miner.alpha_algorithm import AlphaAlgorithm
from backend.heuristic_miner.heuristic_mining import HeuristicMiner

#miner = HeuristicMiner("/Users/phuonganhngo/Downloads/datasets/L1.xes", 0.8, 0.1)
alpha = AlphaAlgorithm("/Users/phuonganhngo/Downloads/datasets/L2.xes")
alpha.get_petri_net()
alpha.frequency()
print("frequency: ", alpha.event)
#print("pL: ", alpha.pL)
#miner.heuristic_net()
#print("frequency: ", miner.frequency)
#print("activity: ", miner.activities)
# print("input: ", miner.input)
# print("output: ", miner.output)
# print("dependency: ", miner.dependency) 

