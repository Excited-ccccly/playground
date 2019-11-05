import math

class MinSegmentTree:

  def __init__(self, arr):
    """将一个数组转换成 segment_tree 的表示形式
    segment_tree 是一个 full binary tree，即内部节点有2个 children，叶子节点没有 children 的二叉树
    full binary tree 有一个性质，叶子节点的数量=内部节点的数量+1

    segment_tree 内部也是使用数组来表示，比如当前 node 的 index 为 i, 那么
    左节点的 index 就是 2*i+1, 右节点的 index 就是 2*i+2
    segment_tree 叶子节点的个数，是一个恰好大于 len(arr) 的2的次方数
    比如长度为6的数组在 segment_tree 里叶子节点的数量就是8
    arr 中所有的元素都在叶子节点，sum segment tree 里内部节点是两个子节点的和
    """
    self.length = len(arr)
    self.arr = arr
    # 假设 arr 里有 1，3，5，7，9，11。那么 pow_factor 就是 3，因为 2^3 > 6
    pow_factor = math.ceil(math.log(self.length, 2))
    # segment tree 叶子节点的数量 L 设置为 2^pow_facotr = 8
    # 内部节点的数量 I = (L-1)/(k-1)
    max_size = 2*2**pow_factor-1
    self.st = [-1 for _ in range(0, max_size)]
    self.build_segment_tree()

  def get_mid(self, ss, se):
    return (ss+se)//2

  def build_segment_tree(self):

    def _build_segment_tree(ss, se, i):
      if ss == se:
        self.st[i] = self.arr[ss]
        return self.st[i]
      mid = self.get_mid(ss, se)
      self.st[i] = min(_build_segment_tree(ss, mid, i*2+1), _build_segment_tree(mid+1, se, i*2+2))
      return self.st[i]

    return _build_segment_tree(0, self.length-1, 0)

  def min(self, qs, qe):

    def _min(ss, se, i):
      if ss>=qs and se<=qe:
        return self.st[i]
      if se<qs or ss>qe:
        return math.inf
      mid = self.get_mid(ss, se)
      return min(_min(ss, mid, i*2+1),_min(mid+1, se, i*2+2))
    return _min(0, self.length-1, 0)

  def update(self, index, val):
    self.arr[index] = val
    def _update(ss, se, i):
      if ss<=index<=se:
        if ss == index and se == index:
          self.st[i] = val
          return self.st[i]
        mid = self.get_mid(ss, se)
        self.st[i] = min(_update(ss, mid, i*2+1), _update(mid+1, se, i*2+2))
      return self.st[i]

    _update(0, self.length-1, 0)


arr = [1, 3, 2, 7, 9, 11]
st = MinSegmentTree(arr)
print(st.min(1,5))
st.update(2, 10)
print(st.min(1,5))