--求列表最大值的自我实现版本
maximum'::(Ord a)=>[a]->a
maximum'[]=error "maximum of empty list"
maximum'[x]=x
maximum'(x:xs)=max x (maximum' xs)


--replicate函数的重新实现
replicate'::Int->a->[a]
replicate' n x
	|n<=0 =[]
	|otherwise = x:replicate' (n-1) x
	

--take重新实现
take'::Int->[a]->[a]
take' n _
	|n<=0 =[]
take' _ [] =[]
take' n (x:xs)=x:take'(n-1) xs


--reverse重新实现
reverse'::[a]->[a]
reverse' []=[]
reverse' (x:xs)=reverse' xs++[x]

--zip重新实现
zip'::[a]->[b]->[(a,b)]
zip' _ []=[]
zip' [] _=[]
zip' (x:xs) (y:ys)=(x,y):zip' xs ys


--elem'重新实现
elem'::(Eq a)=>a->[a]->Bool
elem' a []=False
elem' a (x:xs)
	|a==x =True
	|otherwise = a `elem'` xs
	

--快排重新实现
quickSort:: (Ord a)=>[a]->[a]
quickSort [] =[]
quickSort(x:xs)=
		let
			smallerOrEqual=[a|a<-xs,a<=x]
			larger=[a|a<-xs,a>x]
		in
			quickSort smallerOrEqual++[x]++quickSort larger
