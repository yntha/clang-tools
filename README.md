# clang-tools
A growing list of my personal publicly shared tools for working with c/c++ through clang's AST API.

### snake-case.py
Dumps the member names of the named struct, converting them from camel case to
snake case in the process. Also renames them if the resulting name conflicts
with a python keyword or builtin.
```
python3 snake-case.py <source file> <struct name>
```
