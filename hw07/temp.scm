(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
    (car (cdr s))
)

(cadr '(1 2 3 4))