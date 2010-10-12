(define VARAIANCE-THRESHHOLD .000000000000001)

(define (sqrt-simple x)
(define (try guess)
    (if (good-enough? guess)
        guess
        (try (improve guess))))

(define (good-enough? guess)
  (< (abs (- (square guess) x))  VARAIANCE-THRESHHOLD))
 
(define (improve guess)
  (/ (+ guess (/ x guess)) 2))
  
  (define (square n) (* n n))
  
  (define (abs n) (if (< n 0) (- n) n))
  
(try 1)
  )
