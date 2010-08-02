(module test mzscheme
  (define (assert-= x y)
    (assert-equality x y =))
  
  (define (assert-equal? x y)
    (assert-equality x y equal?))
  
  (define (assert-string=? x y)
    (assert-equality x y string=?))
  
  
  (define (assert-equals x y)
    (cond ((or (list? x) (pair? x)) (assert-equal? x y))
          ((number? x) (assert-= x y))
          ((string? x) (assert-string=? x y))
          (else (assert-equality x y (λ (x y) #f)))))
  (define (fail) (error "Test failed"))
  
  (define (assert-true x)
    (if (not x) (fail)))

  (define (assert-false x) (assert-true (not x)))
                       
  
  (define (assert-equality x y eq-checker)
    (if (eq-checker x y) 'PASS
        (begin (display "expected: [")
               (display x)
               (display "], but was: [")
               (display y)
               (display "]")
               (newline)
               (fail))))
  (provide assert-equals assert-true assert-false))

