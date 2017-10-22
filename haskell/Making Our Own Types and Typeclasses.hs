--自定义Shape类型类
data Shape=Circle Float Float Float |Rectangle Float Float Float Float
	deriving (Show)

area::Shape ->Float
area (Circle _ _ r)=pi*r^2
area (Rectangle x1 y1 x2 y2)=(abs $ x2-x1)*(abs $ (y2-y1))


--递归地定义一个列表
infixr 5 :-:
data List a=Empty|a :-: (List a) deriving (Show,Read,Eq,Ord)


--自定义树
data Tree a= EmptyTree | Node a (Tree a) (Tree a) deriving (Show)

singleton ::a -> Tree a
singleton x = Node x EmptyTree EmptyTree

treeInsert::(Ord a)=>a->Tree a->Tree a
treeInsert x EmptyTree = singleton x
treeInsert x (Node a left right)
	|x == a =Node x left right
	|x<a =Node a (treeInsert x left) right
	|x>a =Node a left (treeInsert x right)


treeElem:: (Ord a)=> a->Tree a->Bool
treeElem x EmptyTree=False
treeElem x (Node a left right)
	|x==a =True
	|x<a = treeElem x left
	|x>a = treeElem x right


----标准库中Eq类型类的定义，a需要为具体类型
--class Eq a where
--	(==):: a-> a-> Bool
--	(/=)::a->a->Bool
--	x==y = not (x /= y)
--	x/=y = not (x == y)


--实例化类型类
instance  (Eq m)=> Eq (Maybe m) where
	Just x == Just y = x == y
	Nothing == Nothing = True
	_ == _ = False




--Functor
--f为一个类型构造器，而非一个具体类型
--class Functor f where
--	fmap :: (a->b) -> f a -> f b
