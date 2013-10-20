(define VARAIANCE-THRESHHOLD .000000000000001)
(define dx VARAIANCE-THRESHHOLD)

(define (sqrt x)
(newton (λ (y) (- x (square y))) 1))

(define (square x) (* x x))

; In each iteration of newton's method Xn 
; is determined by the value of X in previous iteration Xn-1 as follows

;Xn = Xn-1  - y/(dy/dx)
;
;where y = f(Xn-1)
;      dy/dx = f'(Xn-1) = [f(Xn-1 + dx) - f(Xn-1)]/dx
;      is the derivative of the function f(Xn-1)
 
(define (newton f guess)
  (define deriv (λ (f) (λ (x) (/ (- (f (+ x dx)) (f x)) dx))))
  (define df (deriv f))
  (fixed-point (λ (x) (- x (/ (f x) (df x)))) guess))

(define (average a b) (/ (+ a b) 2))

(define (close-enough? prev-result cur-result) (< (abs (- cur-result prev-result)) VARAIANCE-THRESHHOLD))
(define (fixed-point fn x)
  (define (is-fixed prev-result cur-result)
    (if (close-enough? prev-result cur-result)
        cur-result
        (is-fixed cur-result (fn cur-result))))
  (is-fixed x (fn x)))


(sqrt 25)
(sqrt 2)
(sqrt 9)
(newton (λ (x) (+ (- (square x) (* 5 x)) 4)) 0)
(newton (λ (x) (+ (- (square x) (* 6 x)) 4)) 0)