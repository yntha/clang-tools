import json
import clang.cindex as clang
clang.Config.set_library_file('/data/data/com.termux/files/usr/lib/libclang.so')

imaginary_file = 'input_src.cpp'
class CLangAST:
  incl_headers = ['stdint.h']
  
  def __init__(self, source_path):
    source = None
    with open(source_path, 'r') as source_fobj:
      source = source_fobj.read()
    
    if source is None:
      print('Failed to read source.')
      
      return
    
    source = self._prefix_includes() + source
    self.ast = cpp = clang.TranslationUnit.from_source(imaginary_file,
      unsaved_files = [(imaginary_file, source)])
    
  
  @property
  def tokens(self):
    return self.ast.get_tokens(extent = self.ast.cursor.extent)
  
  def _prefix_includes(self):
    headers = []
    
    for header in CLangAST.incl_headers:
      headers.append('#include <%s>' % header)
    
    return '\n'.join(headers)
  
  def structs(self):
    advance_to = None
    
    for token in self.tokens:
      cursor = token.cursor
      
      if advance_to is not None:
        if cursor.location.line <= advance_to.line:
          continue
        
        advance_to = None
      
      if cursor.kind != clang.CursorKind.STRUCT_DECL:
        continue
      
      advance_to = cursor.type.get_declaration().extent.end
      
      yield cursor.type