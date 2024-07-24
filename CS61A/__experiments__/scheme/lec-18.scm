(define (sum-of-squares n)
  (if (= n 0) 
    0
    (+ (* n n) (sum-of-squares (- n 1)))
  )
)
(sum-of-squares 4)

(define (add-to-all lst)
	(if (null? lst)
    nil
		(cons (+ (car lst) 1) (add-to-all (cdr lst)))
  )
)
(add-to-all '(1 2 3 4))