
# Special characters

https://tldp.org/LDP/abs/html/special-chars.html

# Command substitution

First call `ls` and then iterate over those values

```shell
for file in $(ls)
```

# Process substitution

`<(CMD)` will execute `CMD` and place the output in a temporary file and substitute `<()` with file name.

```shell
diff <(ls foo) <(ls bar)
```

difference between files in `foo` and `bar` dir.


