import json
import struct
import os
from pprint import pprint


class Rule(object):
    def __init__(self, inputs, outputs):
        self.inputs = inputs
        self.outputs = outputs

    def applies(self, knowledge):
        return set(self.inputs).issubset(set(knowledge))


rule1 = Rule(["a"], ["b"])
rule2 = Rule(["a", "b"], ["c"])
rule3 = Rule(["a", "b", "c"], ["d"])
rule4 = Rule(["d", "a", "c"], ["e"])
rule5 = Rule(["e"], ["f"])
rule6 = Rule(["z"], ["x"])
rule7 = Rule(["a", "z"], ["w"])
rules = [
    rule1,
    rule2,
    rule3,
    rule4,
    rule5,
    rule6,
    rule7
]

knowledge = ["a"]

someRuleApplies = True
while ((len(rules) > 0) and (someRuleApplies == True)):
    someRuleApplies = False
    for rule in rules:
        if rule.applies(knowledge):
            rules.remove(rule)
            knowledge.extend(rule.outputs)
            knowledge = list(set(knowledge))
            someRuleApplies = True
            break
    

print (knowledge)