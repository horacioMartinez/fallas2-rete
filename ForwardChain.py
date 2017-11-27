import json
import struct
import os
from rule import Rule
from pprint import pprint
import sys
# from problog.tasks.dtproblog import dtproblog

def query_yes_no(question):
    valid = {"si": True, "s": True, "se": True,
             "no": False, "n": False}

    while True:
        sys.stdout.write(question + " [si/no] ")
        choice = input().lower()
        if choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Por favor responde con 'si' o 'no'.\n")

LARGA_DISTANCIA = "Larga distancia"
GRAVE_SINTOMA = "Sintoma grave"
MAL_CLIMA = "Mal clima"
NOCHE = "Noche"

PERSONAL_ADICIONAL = "Personal adicional"
DOBLE_AMBULANCIA = "Doble ambulancia"
RAPIDA_AMBULANCIA = "Ambulancia rapida"
EQUIPAMIENTO_EXTRA = "Equipamiento extra"

rule1 = Rule([LARGA_DISTANCIA], [RAPIDA_AMBULANCIA])
rule2 = Rule([LARGA_DISTANCIA,GRAVE_SINTOMA], [EQUIPAMIENTO_EXTRA])
rule3 = Rule([EQUIPAMIENTO_EXTRA, NOCHE], [DOBLE_AMBULANCIA])
rule4 = Rule([GRAVE_SINTOMA,NOCHE], [EQUIPAMIENTO_EXTRA])
rule5 = Rule([MAL_CLIMA,NOCHE], [DOBLE_AMBULANCIA])
rules = [
    rule1,
    rule2,
    rule3,
    rule4,
    rule5
]

initialKnowledge = []
if query_yes_no("El destino se encuentra a una distancia mayor a 5KM?"):
    initialKnowledge.append(LARGA_DISTANCIA)
if query_yes_no("El sintoma del paciente es grave?"):
    initialKnowledge.append(GRAVE_SINTOMA)
if query_yes_no("Hay mal clima?"):
    initialKnowledge.append(MAL_CLIMA)
if query_yes_no("Es de noche?"):
    initialKnowledge.append(NOCHE)

knowledge = list(initialKnowledge)

someRuleApplies = True
while ((len(rules) > 0) and (someRuleApplies == True)):
    someRuleApplies = False
    for rule in rules:
        if rule.applies(knowledge):
            rules.remove(rule)
            rule.apply(knowledge)
            knowledge = list(set(knowledge))
            someRuleApplies = True
            break
    

print ("Dada el siguiente conocimiento inicial: " + ', '.join(initialKnowledge))
newKnowledge = list(set(knowledge) - set(initialKnowledge))
print("Deducimos el conocimiento: " + ', '.join(newKnowledge))


# from problog.tasks.dtproblog import dtproblog
# from problog.program import PrologString
# 
# model = """
#     0.3::rain.
#     0.5::wind.
#     ?::umbrella.
#     ?::raincoat.
# 
#     broken_umbrella :- umbrella, rain, wind.
#     dry :- rain, raincoat.
#     dry :- rain, umbrella, not broken_umbrella.
#     dry :- not(rain).
# 
#     utility(broken_umbrella, -40).
#     utility(raincoat, -20).
#     utility(umbrella, -2).
#     utility(dry, 60).
# """
# 
# program = PrologString(model)
# decisions, score, statistics = dtproblog(program)
# 
# for name, value in decisions.items():
#     print ('%s: %s' % (name, value))
# 
# 
# '''
# instalar:
# sudo apt install python-pip
# pip install setuptools
# pip install problog
# 
# ejecutar:
# python3 ForwarChain.py
# '''