(define (over-or-under num1 num2) 
    (if (> num1 num2)
        1
        (if (= num1 num2)
            0
            -1
            )
        ))

(define (make-adder num) 
    (lambda (num2) (+ num num2)))

(define (composed f g) 
    (lambda (x) (f (g x)))
    )

(define lst 
    '((1) 2 (3 4) 5)
    )



(define (duplicate lst) 
    (if (null? lst)
        '()
        (if (null? (cdr lst))
            (cons (car lst) lst)
            (append 
                    (list (car lst) (car lst)) 
                    (duplicate (cdr lst)))
            )
    )
)

