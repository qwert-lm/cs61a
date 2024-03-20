(define (my-filter pred s) 
    (if (null? s)
    s
    (let (
             (first (car s))
             (rest (my-filter pred (cdr s)))
        )
    (if (pred first)
        (cons first rest)
        rest
        )
    )
)
)

(define (interleave lst1 lst2) 
    (if (null? lst1)
        lst2
        (if (null? lst2)
            lst1
            (cons (car lst1) (interleave lst2 (cdr lst1)))
            )
        )
    )

(define (accumulate joiner start n term)
  (if (= n 0)
      start
      (joiner (term n) (accumulate joiner start (- n 1) term))
      )
  )

(define (no-repeats lst) 
    (define (in-list? element lst)
          (if (null? lst)
              #f
              (if (= element (car lst))
                  #t
                  (in-list? element (cdr lst)))))
    (define (helper input encountered)
        (if (null? input)
            '()
            (if (in-list? (car input) encountered)
                (helper (cdr input) encountered)
                (cons (car input) 
                      (helper (cdr input) 
                              (cons (car input) encountered)
                              )
                          ) 
                )
            )
        )
    (helper lst '())
)
