(define (min list) (reduce (λ (x y) (if (< x y) x y)) list))
(define (max list) (reduce (λ (x y) (if (> x y) x y)) list))


(define (max-2 x y) (max `(,x ,y)))
(define (min-2 x y) (min `(,x ,y)))

(define (minmax-reducor cur-match condition f1 f2)
  (λ (x y)
    (if (condition (f1 x y) cur-match) 
        (f2 x y) 
        (f1 x y)
        )
    ))

(define (nth-max list n)
  (nth-minmax list n (λ (cur-max) (minmax-reducor cur-max >= max-2 min-2)) (max list)))

(define (nth-min list n)
  (nth-minmax list n (λ (cur-min) (minmax-reducor cur-min <= min-2 max-2)) (min list)))

(define (nth-minmax list n reducor first-match) 
  (define (iter list cur-match n)
    (if (= n 0) cur-match
        (iter list (reduce (reducor cur-match) list) (- n 1))
        ))
  (iter list first-match (- n 1)))


(define (reduce fn list)
  (define (accumilate accumilator a-list)
    (if (null? a-list) accumilator
        (accumilate (fn accumilator (car a-list)) (cdr a-list))))
  (accumilate (car list) (cdr list)))

(define (2nd-largest list) (nth-max list 2))
(define (2nd-smallest list) (nth-min list 2))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(= 1 (nth-min `(1 4 3 2 6) 1) )
(= 2 (2nd-smallest `(1 4 3 2 6)))
(= 1 (2nd-smallest `(-2 4 4 2 1 )))
(= 4 (nth-min `(-2 4 4 2 1) 6))
(= 6 (nth-max `(1 4 3 2 6) 1) )
(= 4 (2nd-largest `(1 4 3 2 6)) )
(= 3 (nth-max `(1 4 3 2 6) 3) )
(= 3 (nth-max `(1 4 3 6 6) 3) )
(= 1 (nth-max `(1 4 3 6 6) 4) )
(= 0 (2nd-largest `(0 0 6 6)) )
(= 2 (2nd-largest `(-2 4 4 2 1 )) )
(= 2 (nth-max `(2 2 2 -2 -2) 1) )
(= 2 (nth-max `(2 2 2 -2 -2) 1) )
(= 1 (min `(1 2 3)) )
(= -1 (min `(1 2 3 -1)))
(= -3 (min `(-3 2 3 4 5)))
(= 1 (min `(2 4 5 1)) )
(= -2 (min `(2 2 2 -2 -2)) )
(= 3 (max `(1 2 3)) )
(= 3 (max `(1 2 3 -1)))
(= 5 (max `(-3 2 3 4 5)))
(= 5 (max `(2 4 5 1)) )
(= 2 (max `(2 2 2 -2 -2)))
