import ifcopenshell

#from rules import windowRule
#from rules import doorRule
from rules import classificationRule

model = ifcopenshell.open("C:/models/24_06/CES_BLD_24_06_ARC.ifc")

#windowResult = windowRule.checkRule(model)
#doorResult = doorRule.checkRule(model)
classificationResult = classificationRule.checkRule(model)

#print("Window result:", windowResult)
#print("Door result:", doorResult)
print("Classification result:", classificationResult)
