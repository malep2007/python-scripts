def some_function(*args, **kwargs):
    if len(args)!=0:
        print(args[0])
    name = kwargs.get("name")
    if name is not None:
        print("we have a keyword variable called " + name + " Keys:" + kwargs.keys())
    else:
        print("no keyword variable called name")
    if name not in kwargs.keys():
        print("No name in list")
    else:
        print("We got name")



some_function("Ephraim", name="Malinga", age=31)

