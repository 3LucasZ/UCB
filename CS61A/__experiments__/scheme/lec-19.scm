; Simple
; f(n) = n!
(define (f n)
  (if (= n 0) 
    1
    (* n (f (- n 1)))
  )
)

(f 5)

; Weird efficient (tail call)
; f(n, k) = n! * k
(define (f n k)
  (if (= n 0) k
    (f (- n 1) (* n k))
  )
)

(f 5 1)

; Simple
; len(lst) = |lst|
(define (len lst)
  (if (null? lst)
    0
    (+ 1 (len (cdr lst)))
  )
)

; Tail recursive
; len(lst, k) = |lst| + k
; len(lst, k) = len(cdr(lst), k+1)
(define (len lst k)
  (if (null? lst)
    k
    (len (cdr lst) (+ k 1))
  )
)

(len '(1 2 3 4 5 6 7 8 9 10) 0)

; Tail recursive
; reduce(f s start) = reduce(f cdr(s) f(car(s) start))
(define (reduce f s start)
  (if (null? s)
    start
    (reduce f (cdr s) (f (car s) start))
  )
)

(reduce * '(1 2 3 4 5) 1)

; Map solution #1
; Simple, not tail recursive, inefficient :(
(define (map-rec procedure s)
  (if (null? s) nil
    (cons (procedure (car s))
      (map-rec procedure (cdr s))
    )
  )
)

(map-rec (lambda (x) (+ x 1)) (list 3 4 5))

; Tail recursive
; map(f s) = (f(s[0]), f(s[1]), ...)
; helper(s cur) = helper(cdr(s) '(f(car(s)) cur))
(define (map f s)
  (define (helper s cur)
    (if (null? s)
      cur
      (helper (cdr s) 
        (list
          cur
          (f (car s))
        )
      )
    )
  )
  (helper (cdr s) (list (f (car s))))
)

(map (lambda (x) (+ x 1)) (list 3 4 5))

