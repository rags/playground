(define (seperate-nums list col)
  (cond
    ((null? list) (col () () 1 0))
    ((list? (car list)) (seperate-nums (cdr list) (λ (evens odds even-prod odd-sum) 
                                                    (seperate-nums (car list) (λ (car-evens car-odds car-even-prod car-odd-sum) 
                                                                                (col (cons car-evens evens) 
                                                                                     (cons car-odds odds) 
                                                                                     (* car-even-prod even-prod) 
                                                                                     (+ car-odd-sum odd-sum)))))))
    (else (cond
            ((even? (car list)) (seperate-nums (cdr list) (λ (evens odds even-prod odd-sum) 
                                                            (col (cons (car list) evens) 
                                                                 odds 
                                                                 (* even-prod (car list)) 
                                                                 odd-sum))))
            (else (seperate-nums (cdr list) (λ (evens odds even-prod odd-sum) 
                                              (col evens 
                                                   (cons (car list) odds) 
                                                   even-prod 
                                                   (+ odd-sum (car list))))))))))


(define (collector evens odds even-prod odd-sum)
  (cons evens (cons odds (cons even-prod (cons odd-sum `())))))

(equal? `((2 (4 (4)) 4) (1 3 (3 (5)) 3 5) 128 20) (seperate-nums `(1 2 3 (3 4 (4 5)) 3 4 5) collector))

(equal? `((() () () ()) ((1) (3 5) 7 9 11 (13) (5 7)) 1 61) (seperate-nums `((1) (3 5) 7 9 11 (13) (5 7)) collector))

(equal? `((2 4 6 8 10) () 3840 0) (seperate-nums `(2 4 6 8 10) collector))