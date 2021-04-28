# Git data model

## Snapshots

Top-level tree that is being tracked.

```shell
<root> (tree)
|
+- foo (tree)
|  |
|  + bar.txt (blob, contents = "hello world")
|
+- baz.txt (blob, contents = "git is wonderful")
```

## Data model

```shell
// file is a bunch of bytes
type blob = array<byte>

// directory is files and directories
type tree = map<string, tree|blob>

type commit = struct{
    parent: array<commit> // Directed acyclic graph. can have multiple parents, e.g. merge branch.
    author: string
    message: string
    snapshot: tree
}
```

## Objects and hashing

```python
type object = blob | tree | commit

objects = map<string, object> # SHA-1 hash to object

def store(object):
    id = sha1(object)
    objects[id] = object

def load(id):
    return objects[id]
```

## References

Human-readable references instead of SHA-1 hash code. e.g. `master`, `HEAD`.

```python
references = map<string, string>

def update_reference(name, id):
    reference[name] = id

def read_reference(name):
    return reference[name]

def load_reference(name_or_id):
    if name_or_id in references:
        return references[name_or_id]
    else:
        return load(name_or_id)
```


