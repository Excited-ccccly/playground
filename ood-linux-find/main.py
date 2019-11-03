from typing import List
from entry import Entry
from filters import Filter, FileExtensionFilter, SizeGreaterOrEqualFilter

class Context:
  """本次搜索执行的上下文
  :param entrypoint: 搜索的起始 entry
  :param filters: 搜索的过滤条件
  """

  def __init__(self, entrypoint: Entry, filters: List[Filter] = []):
    self.entrypoint = entrypoint
    self.filters = filters

  def add_filter(self, filter: Filter):
    self.filters.append(filter)

  def execute(self) -> List[Entry]:
    """bfs 搜索所有可能满足条件的 entry
    """
    results = []
    source = [self.entrypoint]
    while source:
      entry = source.pop()
      if all([f.test(entry) for f in self.filters]):
        results.append(entry)
      if entry.is_dir:
        source.extend(entry.children)
    return results

# 这里直接手工构造目录和过滤条件了。 因为这不是 ood 的重点
# 过滤条件在实际使用中，一般是通过命令行传入的参数构造的，可以用 argparse 来解析命令行参数
"""
手动构造的目录结构大概长这样

├── code
│   └── main.py
│   └── cmd.go
│   └── data.json
"""
pyE = Entry("main.py", False, [], 20)
goE = Entry("cmd.go", False, [], 30)
jsonE = Entry("data.json", False, [], 256)
codeE = Entry("code", True, [pyE, goE, jsonE], 0)

context = Context(entrypoint=codeE)

# size 大于等于30的 filter
greater_or_equal_filter = SizeGreaterOrEqualFilter(30)
context.add_filter(greater_or_equal_filter)
print(context.execute())

# 以 .go 结尾的文件
file_extension_filter = FileExtensionFilter("go")
context.add_filter(file_extension_filter)
# context 里有两个 filter，所以只打印 size >= 30 并且扩展名为 go 的文件
print(context.execute())