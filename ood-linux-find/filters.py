from abc import abstractmethod
from entry import Entry

class Filter:
  """filter 抽象类
  """
  @abstractmethod
  def test(self, entry: Entry):
    pass

class FileExtensionFilter(Filter):
  """扩展名 filter
  """

  def __init__(self, extension: str):
    self.required_extension = extension

  def test(self, entry: Entry):
    if entry.is_dir:
      return False
    splited_filename = entry.name.split(".")
    if len(splited_filename) < 2:
      return False
    entry_extension = splited_filename[-1]
    return self.required_extension == entry_extension

class SizeFilter(Filter):
  """ size filter 抽象类. 因为 size 的比较可以有 >, >=, =, <, <=
  但其实可以通过 > 和 = 就可以构造出所有的比较。例如
  >= -> > or =
  <= -> not >
  <  -> not (> or =)
  这种由基本的元素来组合的思想值得学习
  """

  def __init__(self, size: int):
    self.required_size = size

  @abstractmethod
  def test(self, entry: Entry):
    pass

class SizeGreaterFilter(SizeFilter):
  """ 大于 size 的 filter
  """

  def __init__(self, size):
    super().__init__(size)

  def test(self, entry: Entry):
    return entry.size > self.required_size

class SizeEqualFilter(SizeFilter):
  """ 等于 size 的 filter
  """

  def __init__(self, size):
    super().__init__(size)

  def test(self, entry: Entry):
    return entry.size == self.required_size

class SizeGreaterOrEqualFilter(SizeFilter):
  """ SizeGreaterOrEqualFilter 是 SizeGreaterFilter 和 SizeEqualFilter 的组合
  """

  def __init__(self, size):
    super().__init__(size)
    self.greater_filter = SizeGreaterFilter(size)
    self.equal_filter = SizeEqualFilter(size)

  def test(self, entry: Entry):
    return self.greater_filter.test(entry) or self.equal_filter.test(entry)

class SizeLessOrEqualFilter(SizeFilter):
  """ SizeLessOrEqualFilter 是 SizeGreaterFilter 取反
  """

  def __init__(self, size):
    super().__init__(size)
    self.greater_filter = SizeGreaterFilter(size)

  def test(self, entry: Entry):
    return not self.greater_filter.test(entry)

class SizeLessFilter(SizeFilter):
  """ SizeLessOrEqualFilter 是 SizeGreaterOrEqualFilter 取反
  """

  def __init__(self, size):
    super().__init__(size)
    self.greater_or_equal_filter = SizeGreaterOrEqualFilter(size)

  def test(self, entry: Entry):
    return not self.greater_or_equal_filter.test(size)