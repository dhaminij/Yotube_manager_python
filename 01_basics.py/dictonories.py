chai_types = {"masala":"spicy",
              "ginger":"zesty",
              "green":"mild"}
chai_types["earl"] = "citrus"
for key,value in chai_types.items():
    print(key,value)

chai_types.popitem()
print(chai_types)

del chai_types["green"]
print(chai_types)

chai_types_copy = chai_types.copy()
print(chai_types_copy)

tea_shop = {
    "chai":{
        "masala":"spicy",
        "ginger":"zesty",
    },
    "tea":{
        "green":"mild",
        "black":"strong"
    }
}
print(tea_shop)
tea_shop["chai"]

squared_nums = [x**2 for x in range(10)]
print(squared_nums)

squared_nums = {x:x**2 for x in range(10)}
print(squared_nums)
squared_nums.clear()
print(squared_nums)

keys = ["masala","ginger","lemon"]
print(keys)
default_value = "Delicious"
new_dict = dict.fromkeys(keys,default_value)
print(new_dict)
new_dict = dict.fromkeys(keys,keys)
print(new_dict)
