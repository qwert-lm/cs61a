(define (even-subsets s)
    (if (null? s) nil
        (append (even-subsets (cdr s))
                (map (lambda (t) (cons (car s) t))
                     (if (even? (car s))
                         (even-subsets (cdr s))
                         (odd-subsets (cdr s))
                         ))
                (if (even? (car s)) 
                    (list (list (car s)))
                    nil
                    )
                     )
                )
        )


(define (odd-subsets s)
    (if (null? s) nil
        (append (odd-subsets (cdr s))
                (map (lambda (t) (cons (car s) t))
                     (if (odd? (car s))
                         (even-subsets (cdr s))
                         (odd-subsets (cdr s))
                         ))
                (if (odd? (car s)) 
                    (list (list (car s)))
                    nil
                    )
                     )
                )
        )
    
(define (all-subsets s)
    (if (null? s) 
        nil
        (let ((rest-subsets (all-subsets (cdr s))))
        (append rest-subsets
                (map (lambda (sub) (cons (car s) sub)) rest-subsets)
                (list (list (car s)))
                )
        )
    ))

; (define (all-subsets s)
;   (if (null? s) 
;       '()
;       (let ((rest-subsets (all-subsets (cdr s))))
;         (append rest-subsets
;                 (map (lambda (subset) (cons (car s) subset)) rest-subsets)
;                 (list (list (car s)))
;                 )
;         )
;       )
;   )
