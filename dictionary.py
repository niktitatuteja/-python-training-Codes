dict = {"name": "Nikita Rani", "age": 20, "gender": "female"}
print(dict)

print(dict["name"])

print(dict.values())

dict["age"] = 31
print(dict)

dict["role"] = "student"
print(dict)

for key in dict:
    print(key)

l1 = ['apple', 'banana', 'cherry']
l2 = [10, 20, 30]
dict1 = {l1[i]: l2[i] for i in range(len(l1))}
print(dict1)


dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = {**dict1, **dict2}
print(f"Dictionary 1: {dict1}")
print(f"Dictionary 2: {dict2}")
print(f"Merged Dictionary: {merged_dict}")


dict = {'C': 92, 'Java': 66, 'Python': 85}
lowest_value_key = min(dict, key=dict.get)
print(f"The dictionary is: {dict}")
print(f"The key with the lowest value is: {lowest_value_key}")
min_value = dict[lowest_value_key]
print(f"The lowest value is: {min_value}")