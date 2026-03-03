# Method 1 : Using forloop, if-else condition
def merge_dicts(dict1, dict2): # Fnctin ដែរ accepts 2 parameters (dict1, ditc2)
    merged = dict1 # Can be use dict1.copy() to avoid modifying the original dict1 but teacher said same reference is fine, so we can directly assign dict1 to merged7
    for key, value in dict2.items():
        if key in merged: # dak condition to check tha mean key ot ber mean merge
            merged[key] += value #
        else:
            merged[key] = value
    return merged
"""
# Method 2 : Applying .get()
def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    for key, value in dict2.items():
        merged[key] = merged.get(key, 0) + value
    return merged
"""

# Create a function that merges two dictionarie, If a key exists in both, sum the values.
d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 3, "c": 4, "d": 5}
# user input those 2 parameters
print(merge_dicts(d1, d2)) # Expected output: {'a': 1, 'b': 5, 'c': 7, 'd': 5}
