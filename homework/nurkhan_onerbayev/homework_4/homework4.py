
my_dict = {
    "tuple": (1, 2, 3, 4, 5),
    "list": [1, 2, 3, 4, 5],
    "dict": {"num1": 1,
             "num2": 2,
             "num3": 3,
             "num4": 4,
             "num5": 5
    },
    "set": {1, 2, 3, 4, 5}
}


# Task1
print(my_dict["tuple"][-1])


# Task2
my_dict["list"].append(7)
my_dict["list"].pop(1)


# Task3
my_dict["dict"]["i am a tuple'"] = "yes you are"
my_dict["dict"].pop("num2")


# Task4
my_dict["set"].add(7)
my_dict["set"].remove(3)

print(my_dict)
