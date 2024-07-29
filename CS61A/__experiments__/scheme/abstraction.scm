; Object class
(define (attKey att)
  (car att)
)
(define (attVal att)
  (car (cdr att))
)
(define (keys obj)
  (if (null? obj)
    nil
    (cons (attKey (car obj)) (keys (cdr obj)))
  )
)
(define (val obj key)
  (if (null? obj)
    nil
    (if (eq? (car (car obj)) key)
      (car (cdr (car obj)))
      (val (cdr obj) key)
    )
  )
)
(define (setVal obj key val)
  (if (null? obj)
    nil
    (begin 
      (define newVal 
        (if (eq? (attKey (car obj)) key)
          val
          (attVal (car obj))
        )
      )
      (cons (list (attKey (car obj)) newVal) 
            (setVal (cdr obj) key val)
      )
    )
  )
)

; Inherited soldier class
(define (soldier hp dmg)
  (list (list 'hp hp) (list 'dmg dmg))
)

; Testcases
(define p1 (soldier 50 10))
(keys p1)
(val p1 'hp)
(val p1 'dmg)
(define p1 (setVal p1 'dmg 20))
(val p1 'dmg)

