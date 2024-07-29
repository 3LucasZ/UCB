; Scheme ADT trees
(define (tree label branches)
  (cons label branches)
)
(define (label t)
  (car t)
)
(define (branches t)
  (cdr t)
)
(define (is-leaf t)
  (null? (branches t))
)
(define (print t)
  (define (helper1 label depth)
    (if (= depth 0)
      (displayln label)
      (begin
        (display '___)
        (helper1 label (- depth 1))
      )
    )
  )
  (define (helper2 t depth)
    ;print self
    (helper1 (label t) depth)
    ;print children
    (if (not (is-leaf t))
      (map (lambda (b) (helper2 b (+ depth 1))) (branches t))
    )
    nil
  )
  (helper2 t 0)
)

; Double labels
(define (dub t)
  (if (is-leaf t)
    (tree (* (label t) 2) nil)
    (tree (* (label t) 2) (map dub (branches t)))
  )
)

; Tests
(define t
  (tree 3
    (list (tree 1 nil)
          (tree 2 
            (list (tree 4 nil)
                  (tree 5 nil)
            )
          )
    )
  )
)
(print t)
(print (dub t))