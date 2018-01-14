(define (square a) (* a a))
(define (sum-of-square-of-two a b) (+ (square a) (square b)))
(define (soqotln a b c)
  (cond ((and (> a c) (> b c)) (sum-of-square-of-two a b))
         ((and (> a b) (> c b)) (sum-of-square-of-two a c))
         ((and (> b a) (> c a)) (sum-of-square-of-two b c)) 
   )
  )


(soqotln -5 -4 7)