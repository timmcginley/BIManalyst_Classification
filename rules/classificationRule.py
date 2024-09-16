import ifcopenshell


def checkRule(model):

    #Add a popular classification from a library
    # find them here - 
    classify = model.by_type('IfcClassification')[0]

    #library = ifcopenshell.open("C:/classification/uniclass2.ifc")
    #classification = library.by_type("IfcClassification")[0]
    #ifcopenshell.api.classification.add_classification(model,
    #classification=classification)

    # doors = model.by_type('IfcDoor')
    #result = f"Doors: {len(doors)}"

    result = classify.Name
    
    return result
