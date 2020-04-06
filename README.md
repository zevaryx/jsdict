# jsdict

Javascript-style Dictionaries for Python


## Usage

```py
from jsdict import JsDict

d = JsDict({"key1": 2, "key2": 3})

print(d.key1)
# 2
print(d)
# {'key1': 2, 'key2': 3}

d.key3 = {"key4": 5}
print(d)
# {'key1': 2, 'key2': 3, 'key3': {'key4': 5}}

d.key3.key5 = 6
print(d)
# {'key1': 2, 'key2': 3, 'key3': {'key4': 5, 'key5': 6}}
```
