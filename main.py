import ifcopenshell

#from rules import windowRule
#from rules import doorRule
from rules import classificationRule

# remember this is a local link on my machine as we cannnot upload the files to github.
model = ifcopenshell.open("C:/models/24_06/CES_BLD_24_06_MEP.ifc")

#windowResult = windowRule.checkRule(model)
#doorResult = doorRule.checkRule(model)
classificationResult = classificationRule.checkRule(model)

#print("Window result:", windowResult)
#print("Door result:", doorResult)
print('')
print("Classification result:", classificationResult)
print('')