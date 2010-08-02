(define (mycons x y) (lambda (f) (f x y))) 
(define (mycar x) (x (lambda (a b) a)))
(define (mycdr x) (x (lambda (a b) b)))
