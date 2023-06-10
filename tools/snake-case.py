import ast
import sys
import re
import keyword

# https://stackoverflow.com/a/1176023
def camel_to_snake(name):
  name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
  name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()
  
  if is_reserved(name):
    name = 'x_' + name
  
  return name

def is_reserved(name):
  return (name in __builtins__.__dict__ or keyword.iskeyword(name))

def main():
  cpp = ast.CLangAST(sys.argv[1])
  
  for struct in cpp.structs():
    if struct.spelling != sys.argv[2]:
      continue
    
    fields = struct.get_declaration().get_children()
    for field in fields:
      print(camel_to_snake(field.spelling))

main()