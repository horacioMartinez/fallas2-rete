class Rule(object):
    def __init__(self, inputs, outputs):
        self.inputs = inputs
        self.outputs = outputs

    def applies(self, data):
        return set(self.inputs).issubset(set(data))

    def implies(self, target):
        return target in self.outputs

    def apply(self, knowledge):
        knowledge.extend(self.outputs)