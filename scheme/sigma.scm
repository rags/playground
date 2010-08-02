(define (sigma-recurse low high incrementor current-value) 
  (if (> low high) 0
      (+ (current-value low) (sigma-recurse (incrementor low) high incrementor current-value)))
  )

(define (sigma-iterate low 
                         high 
                         incrementor 
                         current-value 
                         accumilator) 
  (if (> low high) accumilator
      (sigma-iterate (incrementor low) 
                       high 
                       incrementor 
                       current-value
                       (+ (current-value low) accumilator)))
  )

(define (sigma low high incrementor current-value) 
  ;(sigma-recurse low high incrementor current-value)
  (sigma-iterate low high incrementor current-value 0)
  )

(define (++ x) (+ 1 x))

(define (sum a b)
  (sigma a b ++ (λ (i) i)))

(define (sum-of-square a b)
  (sigma a b ++ (λ (i) (* i i))))

