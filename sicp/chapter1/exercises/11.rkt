#lang racket

; recursive process.
(define (f-rec n)
  (cond ((< n 3) n)
        (else (+ (f-rec (- n 1)) (* 2 (f-rec (- n 2))) (* 3 (f-rec (- n 3))))) 
        )
  )

; iterative process
(define (f n)
  (define (f-iter a b c n)
    (cond ((= n 2) a)
          ((= n 1) b)
          ((= n 0) c)
          (else (f-iter (+ a (* 2 b) (* 3 c)) a b (- n 1)))
    )
    )
  (f-iter 2 1 0 n)
  )

(f-rec 3)
(f 3)

(= (f 20) (f-rec 20))