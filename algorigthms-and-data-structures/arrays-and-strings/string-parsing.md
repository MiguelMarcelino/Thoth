# String Manipulation / Parsing

These problems test your ability to process structured or semi-structured text efficiently — for example:

* Normalizing or simplifying URL paths.
* Parsing logs or command strings.
* Detecting patterns or extracting key data.


## Common Patterns

### Stack-Based Parsing (e.g., Simplify Path)

Used when the input has nested or hierarchical structure, such as directories or parentheses.

Example: Simplify a URL Path

```python
def simplify_path(path):
    parts = path.split('/')
    stack = []
    for p in parts:
        if p == '' or p == '.':
            continue
        elif p == '..':
            if stack:
                stack.pop()
        else:
            stack.append(p)
    return '/' + '/'.join(stack)
```

Why: Each `..` means "go up one directory", and the stack models that hierarchy.


### Tokenization / Splitting

Used for parsing logs, commands, or key-value pairs.

Example: Parse Log Entries

```python
def parse_log(log):
    # Example log: "10.0.0.1 - - [10/Oct/2025:13:55:36] 'GET /index.html HTTP/1.1' 200"
    parts = log.split()
    ip = parts[0]
    method = parts[5].strip("'")
    path = parts[6]
    status = int(parts[-1])
    return {"ip": ip, "method": method, "path": path, "status": status}
```


### String Sliding / Pattern Matching

Used when searching or filtering within large strings (useful for packet inspection or log scanning).

Example: Find the first unique character

```python
def first_unique_char(s):
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    return -1
```

<hr>

Related to: [arrays-and-strings](arrays-and-strings)
