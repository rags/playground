(define (min list) (reduce (λ (x y) (if (< x y) x y)) list))
(define (max list) (reduce (λ (x y) (if (> x y) x y)) list))

(define (reduce fn list)
  (define (accumilate accumilator a-list)
    (if (null? a-list) accumilator
        (accumilate (fn accumilator (car a-list)) (cdr a-list))))
  (accumilate (car list) (cdr list)))

(define (filter fn list)
  (define (accumilate accumilator a-list)
    (if (null? a-list) accumilator
        (if (not (fn (car a-list))) 
            (accumilate (append accumilator `(,(car a-list))) (cdr a-list))
            (accumilate accumilator (cdr a-list))            
            ))        
        )
  (accumilate `() list))

(define (nth-minmax list n minmax-fn) 
  (define (iter a-list n cur-match)
    (if (or (= n 0) (null? a-list)) cur-match (do-iter a-list n cur-match))
    )
  (define (do-iter a-list n cur-match)
    (define filtered-list (filter (λ (x) (= x cur-match)) a-list))
    (if (null? filtered-list) cur-match
    (iter filtered-list (- n 1) (minmax-fn filtered-list)))
    )
  (iter list (- n 1) (minmax-fn list))
  )
  


(define (nth-max list n)
  (nth-minmax list n max))

(define (nth-min list n)
  (nth-minmax list n min))

(define (2nd-largest list) (nth-max list 2))
(define (2nd-smallest list) (nth-min list 2))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(equal? `(1 2 4 5  ) (filter (λ (x) (= x 3)) `(1 2 3 4 5 3)))
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
