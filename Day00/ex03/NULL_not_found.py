def NULL_not_found(object: any) -> int:
    try:
        if object is None:  
            print(f"Nothing: {object} {type(object)}")
        elif object == 0: 
            print(f"Zero: {object} {type(object)}")
        elif object == "": 
            print(f"Empty: {object} {type(object)}")
        elif object is False:  
            print(f"Fake: {object} {type(object)}")
        elif object != object:
            print(f"Cheese: {object} {type(object)}")
        else:
            raise Exception
        return 0 
    except Exception as e:
        print("Type not Found")
        return 1  
