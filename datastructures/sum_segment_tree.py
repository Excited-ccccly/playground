import math

class SumSegmentTree:

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
    # 内部节点的数量 I = L-1
    max_size = 2*2**pow_factor-1
    self.st = [-1 for _ in range(0, max_size)]
    self.build_segment_tree()
    # build 完之后， st 长这样
    # self.st = [36, 9, 27, 4, 5, 16, 11, 1, 3, -1, -1, 7, 9, -1, -1]
    # 画成树状图长这样， 内部节点是两个子节点的和
    """
                                        +-----+
                                        |  36 |
                                        |     |
                                        XX-----XX
                                    XXXX         XXX
                                  XXX               XXX
                          +-----XX                   XXX------+
                          |  9   |                     |  27  |
                          |      |                     |      |
                          X+X-----X                     XX-----X
                      XXX          X                   XX       XXX
                  XXXX            XX                XXX           XX
                  XX                XX               X              XXX
            +----X-+             +--X---+        +-XX----+        +--XX---+
            |  4   |             |  5   |        |  16   |        |   11  |
            |      |             |      |        |       |        |       |
            +XX--X-+             +------+        +---XX--+        +-------+
          XX X   XX                                XX  XX
        XXX         XX                            XX     XXX
      XXX            XX                         XXX        XXX
    +-X----+      +---XX--+                 +---X--+     +---X---+
    |  1   |      |   3   |                 |  7   |     |   9   |
    |      |      |       |                 |      |     |       |
    +------+      +-------+                 +------+     +-------+
    """

  def get_mid(self, ss, se):
    """
    :param ss: arr start index
    :param se: arr end index
    """
    return (ss+se)//2

  def build_segment_tree(self):

    def _build_segment_tree(ss, se, i):
      """
      :param ss: Starting indexe of the segment represented by current node
      :param se: Ending indexe of the segment represented by current node
      """
      if ss == se:
        self.st[i] = self.arr[ss]
        return self.st[i]
      mid = self.get_mid(ss, se)
      self.st[i] = _build_segment_tree(ss, mid, i*2+1)+_build_segment_tree(mid+1, se, i*2+2)
      return self.st[i]

    return _build_segment_tree(0, self.length-1, 0)

  def get_sum(self, qs, qe):
    """求 arr[qs:qe] 的和
    :param qs: query start 求和开始的地方
    :param qe: query end 求和结束的地方
    """

    def _get_sum(ss, se, i):
      # 如果 [ss:se] 在 [qs:qe] 内， 那么直接返回已经求好的 [ss:se] 的和 self.st[i]
      if ss>=qs and se<=qe:
        return self.st[i]
      # 如果 [ss:se] 在 [qs:qe] 完全没有交集，那么返回 0
      if se<qs or ss>qe:
        return 0
      # 二分递归求和
      mid = self.get_mid(ss, se)
      return _get_sum(ss, mid, i*2+1)+_get_sum(mid+1, se, i*2+2)
    return _get_sum(0, self.length-1, 0)

  def update(self, index, val):
    """ arr[index] = val
    同时更新 st，如果 index 在 [ss:se] 之间，说明 [ss:se] 的和需要更新，加上一个 diff
    """
    origin = self.arr[index]
    diff = val - origin

    def _update(ss, se, i):
      if ss<=index<=se:
        self.st[i] += diff
        mid = self.get_mid(ss, se)
        # 防止当 ss = se 时的无限递归调用
        if mid != ss or mid != se:
          _update(ss, mid, i*2+1)
          _update(mid+1, se, i*2+2)

    _update(0, self.length-1, 0)


arr = [1,3,5,7,9,11]
st = SumSegmentTree(arr)
print(st.get_sum(1,3))
st.update(1, 10)
print(st.get_sum(1,3))