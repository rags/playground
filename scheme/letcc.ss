(define (part-after list item)
  (call/cc (λ (k) 
             (let recur ((l list)) 
               (cond ((null? l) (k list))
                     ((= (car l) item) (part-after (cdr l) item))
                     (else (recur (cdr l))))))))
                     
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(require "test.scm")
(define lst `(1 4 7 3 2 9 4 2 3 6 7))

(assert-equals '(4 7 3 2 9 4 2 3 6 7) (part-after lst 1))
(assert-equals '(2 3 6 7) (part-after lst 4))
(assert-equals '(6 7) (part-after lst 3))
(assert-equals '() (part-after lst 7))
(assert-equals '(1 4 7 3 2 9 4 2 3 6 7) (part-after lst 5))






  
