(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr (cdr s))))

(define (ascending? asc-lst)
  (if (null? asc-lst)
      #t
      (if (null? (cdr asc-lst))
          #t
          (if (<= (car asc-lst) (cadr asc-lst))
              (ascending? (cdr asc-lst))
              #f))))

(define (square n) (* n n))

(define (pow base exp)
  (if (= base 1)
      1
      (if 
          (= exp 2)
          (square base)
          (if 
            (even? exp)
            (square (pow base (/ exp 2)))
            (* base (pow base (- exp 1)))
              )

          )
      )
)
