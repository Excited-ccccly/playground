--统计单词数
import Data.List
import Data.Char
import qualified Data.Map as Map

wordNums::String->[(String,Int)]
wordNums =map (\ws ->(head ws,length ws)).group.sort.words
 
--凯撒加密解密

--encode
encode::Int->String->String
encode offset msg = map (\c-> chr $ ord c + offset) msg

--decode
decode::Int->String->String
decode shift msg=encode (negate shift) msg

--寻找酷数

digitSum::Int ->Int
digitSum = sum.map digitToInt.show

firstTo::Int -> Maybe Int
firstTo n =find (\x ->digitSum x==n) [1..]


--映射键与值
findKey::(Eq k) =>k->[(k,v)]->v
findKey key xs=snd.head.filter (\(k,v)-> key==k)$ xs

--防止空列表的运行时错误
findKey'::(Eq k) =>k->[(k,v)]->Maybe v
findKey' key []=Nothing
findKey' key ((k,v):xs)
			| key==k =Just v
			|otherwise =findKey' key xs


--折叠实现
findKey''::(Eq k) =>k->[(k,v)]->Maybe v
findKey'' key xs=foldr (\(k,v) acc-> if key==k then Just v else acc) Nothing xs

--Map
phoneBook::Map.Map String String
phoneBook =Map.fromList $
				[("a","1")
				,("b","2")
				,("c","3")
				,("d","4")
				]



