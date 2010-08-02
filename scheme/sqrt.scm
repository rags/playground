(define VARAIANCE-THRESHHOLD .000000000000001)
(define dx VARAIANCE-THRESHHOLD)

(define (sqrt x)
(newton (λ (y) (- x (square y))) 1))

(define (square x) (* x x))


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