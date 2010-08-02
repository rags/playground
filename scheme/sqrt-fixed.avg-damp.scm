(define VARAIANCE-THRESHHOLD .000000000000001)

(define (sqrt-fixed-point x)
(fixed-point (λ (y) (average y (/ x y)) ) 1)
  )

(define (sqrt-fixed-point-avg-damp x)
(fixed-point (average-damp (λ (y) (/ x y)) ) 1)
  )

(define (average-damp fn) (λ (y) (average (fn y) y)))


(define (average a b) (/ (+ a b) 2))
;(define (average-damp fn x) (average x (fn x)))
(define (close-enough? prev-result cur-result) (< (abs (- cur-result prev-result)) VARAIANCE-THRESHHOLD))
(define (fixed-point fn x)
  (define (is-fixed prev-result cur-result)
    (if (close-enough? prev-result cur-result)
        cur-result
        (is-fixed cur-result (fn cur-result))))
  (is-fixed x (fn x)))