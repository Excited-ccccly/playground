from typing import List

class Entry:
  """一个文件系统中的项，可能是文件或者文件夹
  """
  def __init__(self, name: str, is_dir: bool, children, size: int):
    self.name = name
    self.is_dir = is_dir
    self.children: List[Entry] = children
    self.size = size

  def __repr__(self):
    """格式化一下 print 的输出
    """
    output = f"[name={self.name}, is_dir={self.is_dir}, size={self.size}]"
    for c in self.children:
      output += f"\n ----{c.__repr__()}"
    return output