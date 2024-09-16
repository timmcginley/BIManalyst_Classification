import ifcopenshell
# Import time module
import time

#from rules import windowRule
#from rules import doorRule
from rules import classificationRule

# remember this is a local link on my machine as we cannnot upload the files to github.
model = ifcopenshell.open("C:/models/24_06/CES_BLD_24_06_MEP.ifc")

#windowResult = windowRule.checkRule(model)
#doorResult = doorRule.checkRule(model)

 
# record start time
start = time.time()
 

classificationResult = classificationRule.checkRule(model)

# record end time
end = time.time()

# print the difference between start 
# and end time in milli. secs
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")

#print("Window result:", windowResult)
#print("Door result:", doorResult)
print('')
print("Your model is classified in:", classificationResult)
print('')