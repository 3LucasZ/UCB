; even-subsets
; --Desc
; find all subsets of given set w/ an even sum
; include an element or not?
; --Parameters
; set of elements left (set), set of elements taken (cur)
; --Return
; LIST of subsets w/ even sum(cur) + all combinations in set
; --Base
; if(null?(set)) => if(even(reduce(+ cur))) => [cur]
; --Transition
; even-subsets(set, sum) => append(
; even-subsets(cdr(set), sum+car(set))
; even-subsets(cdr(set), sum)
; )

(define (even-subsets set cur)
  (begin 
    (displayln (list set cur))
    (if (null? set)
      (if (and (not (null? cur)) (even? (reduce + cur)))
        (list cur)
        nil
      )
      (append 
        (even-subsets (cdr set) (append cur (list (car set))))
        (even-subsets (cdr set) cur)
      )
    )
  )
)

(even-subsets '(1 3 2 5) '())