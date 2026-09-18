 # 1 Dictionary in Python

A dictionary is a built-in data type in Python used to store data in key-value
pairs.

Each key is unique and maps to a value.

Dictionaries are unordered, mutable (changeable), and don't allow duplicate
keys.

Example
-          student = {
                "name": "Saumya Singh",
                "age": 25,
                "city": "Sultanpur"
                   }
 
Here:

"name", "age", "city" -> keys
"Saumya Singh", 21, "Delhi" -> values

- Accessing Values
You can access a value using its key:

            print(student [ "name"])  # Saumya Singh
            print(student["city"])    # Delhi

# Methods
- .keys()
Returns all keys in the dictionary
Example: student.keys()
- .values()
Returns all values in the dictionary
Example: student.values()
- .items()
Returns all key-value pairs as tuples
Example: student.items()
- .get(key)
Safely returns the value of a key (avoids error if key is missing)
Example: student.get("name")
- .update(new_dict)
Updates the dictionary with new key-value pairs
Example: student.update({"city": "Lucknow"})

Would you like this converted into a printable format, a flowchart, or a quiz for practice?

- .keys()
Returns all keys in the dictionary
Example: student.keys()
- .values()
Returns all values in the dictionary
Example: student.values()
- .items()
Returns all key-value pairs as tuples
Example: student.items()
- .get(key)
Safely returns the value of a key (avoids error if key is missing)
Example: student.get("name")
- .update(new_dict)
Updates the dictionary with new key-value pairs
Example: student.update({"city": "Lucknow"})

# Nested Dictionary
You can store another dictionary inside a dictionary.
-
Example:-
- 
         profile = {
        "username" : "saumyalsingh",
           "details": {
           "followers": 1200,
           "verified": True
           1

# 2 Sets in Python

A set is a collection of unordered and unique items. Sets automatically
duplicate elements and are written using curly braces { }.
Example:
languages = {"Python", "Java", "C++", "Python"}
print(languages)  # Output: {'C++', 'Java', 'Python'}

- Properties of sets 
· Unordered
no fixed index positions
· Unique -+ no duplicates
. Mutable - elements can be added or removed
· Cannot contain mutable elements like lists or dictionaries
# mathod 
- .add(el)
Adds an element to the set.
Example: nums.add(5)
- .remove(el)
Removes a specific element from the set. Raises an error if the element is not found.
Example: nums.remove(1)
- .clear()
Empties the entire set, leaving it as an empty set.
Example: nums.clear()
- .pop()
Removes and returns a random element from the set.
Example: nums.pop()
- .union(set2)
Returns a new set containing all elements from both sets (no duplicates).
Example: {1, 2}.union({2, 3}) → {1, 2, 3}
- .intersection(set2)
Returns a new set with elements common to both sets.
Example: {1, 2, 3}.intersection({2, 3}) → {2, 3}



### 🔍 Difference Between Dictionary and Set

| Feature      | Dictionary                            | Set                          |
|--------------|----------------------------------------|------------------------------|
| **Structure** | Stores data as key-value pairs         | Stores unique values only    |
| **Syntax**    | `{ "key" : value }`                    | `{value1, value2, ...}`      |
| **Mutable**   | Yes                                    | Yes                          |
| **Duplicates**| Keys are unique                        | All elements are unique      |
| **Indexing**  | Not supported                          | Not supported                |



