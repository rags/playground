(define (is-prime n)
 
  (define (test i)
    (if (> i (sqrt n)) #t
    (if (=(/ n i) 0) #f (test (+ i 1)))))
  (if (< n 2) 
    #f
    (test 2)
    )
  )
