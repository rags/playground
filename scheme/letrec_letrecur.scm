(define (find lst a)
  (let recur ((l lst))
    (cond 
      ((null? l) `())
      ((= (car l) a) a)
      (else (recur (cdr l))))))


(define (find1 l a)
  (letrec ((f (λ (l) (cond 
      ((null? l) `())
      ((= (car l) a) a)
      (else (f (cdr l))))))) (f l))) 

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(require "test.scm")
(define list `(8 5 1 6))


(assert-equals 8 (find list 8))
(assert-equals 8 (find1 list 8))


(assert-equals 1 (find list 1))
(assert-equals 1 (find1 list 1))


(assert-equals `() (find list 9))
(assert-equals `() (find1 list 9))

