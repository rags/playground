(define (combination denominations amount)
  (define (subcomb combs amt mult denoms) 
    (if (null? denoms) combs
        (append combs 
                (map (λ (x) (cons mult x)) 
                     (combination (cdr denoms) (- amt (* mult (car denoms))))))))
  (define (iter mult denoms amt combs)
    (cond
      ((<= (length denoms) 1) (cons `(,mult) combs))  
      ((= mult 0) (subcomb combs amt mult denoms))      
      (else (iter (- mult 1) denoms amt (subcomb combs amt mult denoms)))))
  (if (null? denominations) `(())
      (iter (quotient amount (car denominations)) denominations amount `())))

(= 242 (length (combination  `(25 10 5 1) 100)))
(= 40 (length (combination `(50 25 10 5) 100)))
(equal? `((1)) (combination  `(25) 25))
(equal? `((0 1 1 1) (0 1 0 6) (0 0 3 1) (0 0 2 6) (0 0 1 11) (0 0 0 16)) (combination  `(25 10 5 1) 16))
(equal? (combination  `(50 25 10 5 1) 10) `((0 0 1 0 0) (0 0 0 2 0) (0 0 0 1 5) (0 0 0 0 10)))