--compare类型为(Ord a)=>a->(a->Ordering),用100调用它之后，即可得到一个取一个数值为参数，返回Ordering值得函数
compareWithHundred ::Int->Ordering
compareWithHundred =compare 100


--截断,对中缀函数进行部分应用。将一个参数放在中缀函数的一侧，并在外面用括号括起，即可截断这个中缀函数
divideByTen::(Floating a) =>a->a
divideByTen =(/10)

--函数作为参数
applyTwice::(a->a)->a->a
applyTwice f x = f(f x)


--zipWith实现
zipWith'::(a->b->c)->[a]->[b]->[c]
zipWith' _ [] _ =[]
zipWith' _ _ [] =[]
zipWith' f (x:xs) (y:ys)=f x y: zipWith' f xs ys

--map实现
map'::(a->b)->[a]->[b]
map' _ [] =[]
map' f (x:xs)=f x: map f xs

--filter函数
filter'::(a->Bool)->[a]->[a]
filter' _ []=[]
filter' f (x:xs)
		|f x =x: filter' f xs
		|otherwise =filter' f xs


--100000内能整除3829的最大整数		
largestDivisible ::Integer
largestDivisible=head (filter p [100000,99999..])
	where p x=x `mod` 3829==0


--chain
chain::Integer->[Integer]
chain 1=[1]
chain n
	|even n=n:chain (n `div` 2)
	|odd n=n:chain (n*3+1)
	
--map,filter,chain综合运用
numLongChains::Int
numLongChains =length(filter isLong (map chain [1..100]))
						where isLong xs=length xs>15

--lambda函数,xs为lambda的参数
numLongChains'::Int
numLongChains' =length(filter (\xs->length xs>15) (map chain [1..100]))


--折叠foldl,初始值0和列表中的xs从左到右累加
sum'::(Num a)=>[a]->a
sum' xs=foldl(\acc x-> acc+x) 0 xs


--上面一个函数的柯里化
sum''::(Num a)=>[a]->a	
sum'' = foldl (+) 0		

--使用右折叠实现map
map''::(a->b)->[a]->[b]
map'' f xs = foldr (\x acc -> f x:acc) [] xs


--PointFree风格

--原函数
oddSquareSum::Integer
oddSquareSum =sum(takeWhile (<10000) (filter odd (map (^2) [1..])))

--PointFree化后
oddSquareSum'::Integer
oddSquareSum' =sum.takeWhile (<10000) .filter odd $ map (^2) $ [1..]

