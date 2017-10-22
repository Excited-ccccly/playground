doubleMe x=x+x
doubleUs x y=x*2+y*2
doubleSmallNumber x= if x>100
						then x
						else x*2
						
						
lostNumbers=[4,8,15,16,23,42]
a=[1,2,3,4]
b=[4,6,7,8]
c=a++b
helloWorld="hello"++" "++"world"
d=[9.4,33.2,96.2]


factorial::Integer->Integer
factorial 0=1
factorial n=n*factorial(n-1)


lucky::Int->String
lucky 7 = "Lucky"
lucky x = "Sorry"


addVectors::(Double,Double)->(Double,Double)->(Double,Double)
addVectors (x1,y1) (x2,y2)=(x1+x2,y1+y2)


third::(a,b,c)->c
third (_,_,z)=z


head'::[a]->a
head' []=error "Can't call head on an empty list,dummy!"
head' (x:_)=x


bmiTell::Double->String
bmiTell bmi
	|bmi <= 18.5 ="You are underweight,you emo,you!"
	|bmi <= 25.0 ="You are supposed normal.Pffft,I bet you are ugly!"
	|bmi <= 30.0 ="You are fat!"
	|otherwise ="You are a whale,congratulations!"
	
	
myCompare::(Ord a)=>a->a->Ordering
a `myCompare` b
	|a==b =EQ
	|a<=b =LT
	|otherwise =GT

--where可以保存中间计算结果
bmiTell'::Double->Double->String	
bmiTell' weight height
	|bmi <= 18.5 ="You are underweight,you emo,you!"
	|bmi <= 25.0 ="You are supposed normal.Pffft,I bet you are ugly!"
	|bmi <= 30.0 ="You are fat!"
	|otherwise ="You are a whale,congratulations!"
	where bmi=weight/height^2


--let测试，《haskell趣学指南》中有错误，let绑定多个变量时,let后面不能跟变量，应另起一行，被坑了好久
cylinder::Double->Double->Double
cylinder r h =
	let 
		sideArea = 2*pi*r*h  
		topArea = r^2*pi
	in sideArea+2*topArea

	
--改写上面的let函数为where,同样多个变量需要换行
cylinder'::Double->Double->Double
cylinder' r h =sideArea+2*topArea
	where 
		sideArea = 2*pi*r*h  
		topArea = r^2*pi

--case学习,和let有同样的问题，多个变量需要换行
head'' ::[a]->a
head'' xs=case xs of 
			[] -> error"No head for empty list"
			(x:_)->x
--函数参数的模式匹配只能在定义函数时使用，而case表达式的模式匹配可以用在任何地方			
describeList ::[a]->String
describeList ls="The list is "++ case ls of
									[]->"empty"
									[x]->"a singleton list"
									xs->"a longer list"
