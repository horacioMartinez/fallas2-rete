import json
import struct
import os
from pprint import pprint


class Rule(object):
    def __init__(self, inputs, outputs):
        self.inputs = inputs
        self.outputs = outputs

    def applies(self, data):
        return set(self.inputs).issubset(set(data))

    def implies(self, target):
        return target in self.outputs


#rule1 = Rule(["a"], ["b"])
#rule2 = Rule(["a", "b"], ["c"])
#rule3 = Rule(["a", "b", "c"], ["d"])
#rule4 = Rule(["d", "a", "c"], ["e"])
#rule5 = Rule(["e"], ["f"])
#rule6 = Rule(["z"], ["x"])
#rule7 = Rule(["a", "z"], ["w"])
#rules = [
#    rule1,
#    rule2,
#    rule3,
#    rule4,
#    rule5,
#    rule6,
#    rule7
#]

rule1 = Rule(["p","q"],["s"])
rule2 = Rule(["r"],["t"])
rule3 = Rule(["s","t"],["u"])
rule4 = Rule(["s","r"],["v"])

rules = [
    rule1,
    rule2,
    rule3,
    rule4
]

def backwardsChain(knowledge, targetValue):
    if targetValue in knowledge:
        return True
    for rule in rules:
        if rule.implies(targetValue):
            premises = rule.inputs
            for value in premises:
                if value not in knowledge:
                    backwardsChain(knowledge, value)

            if rule.applies(knowledge):
                knowledge.extend(rule.outputs)
                knowledge = list(set(knowledge))

targetValue = "v"
knowledge = ["p","q","r"]

backwardsChain(knowledge,targetValue)
print (knowledge)