(define (over-or-under num1 num2) 
  (cond
    ((> num1 num2) 1)
    ((> num2 num1) -1)
    (else 0)
  )
)

(define (make-adder num) 
  (define (adder inc)
    (+ num inc)
  )
  adder
)

(define (composed f g) 
  (define (combo x)
    (f (g x))
  )
  combo
)

(define (repeat f n) 
  (define (f-pow-n x)
    (if (= n 0)
      x
      (f ((repeat f (- n 1)) x))
    )
  )
  f-pow-n
)

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b) 
  (define aa (max a b))
  (define bb (min a b))
  (if (zero? b)
    aa
    (gcd bb (modulo aa bb))
  )
)

(define (duplicate lst) 
  (if (null? lst)
    nil
    (append (list (car lst) (car lst)) (duplicate (cdr lst)))
  )
)

(expect (duplicate '(1 2 3)) (1 1 2 2 3 3))

(expect (duplicate '(1 1)) (1 1 1 1))

(define (deep-map fn s) 
  (if  (null? s) 
    nil
    (cons 
      (if (list? (car s))
        (deep-map fn (car s))
        (fn (car s))
      ) (deep-map fn (cdr s))
    )
  )
)
