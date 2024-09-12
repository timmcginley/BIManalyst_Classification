import ifcopenshell

def checkRule(model):
    doors = model.by_type('IfcDoor')

    #result = f"Doors: {len(doors)}"
    result = 'are you sure you are using a classification system?'
    
    return result
