import json
import struct
import os
from rule import Rule

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
                rule.apply(knowledge)
                knowledge = list(set(knowledge))

targetValue = "v"
knowledge = ["p","q","r"]

backwardsChain(knowledge,targetValue)
print (knowledge)