(define (rover x y) (lambda (fn) (fn x y)))
(define (x rover) (rover (lambda (a b) a)))
(define (y rover) (rover (lambda (a b) b)))
(define (rover-out a-rover) `(,(x a-rover) ,(y a-rover)))

(define (left fn) (fn (lambda (left-impl right-impl move-impl out-impl) (left-impl))))

(define (right fn) (fn (lambda (left-impl right-impl move-impl out-impl) (right-impl))))

(define (move fn) (fn (lambda (left-impl right-impl move-impl out-impl) (move-impl))))

(define (out fn) (fn (lambda (left-impl right-impl move-impl out-impl) (out-impl))))



(define (north a-rover)   
  (lambda (fn)
    (fn
     (lambda () (west a-rover)) ;left
     (lambda () (east a-rover)) ;right
     (lambda () (north (rover (x a-rover) (+ (y a-rover) 1)))) ;move
     (lambda () `(,(rover-out a-rover) n)) ;print
     ))
  )

(define (south a-rover)   
  (lambda (fn)
    (fn
     (lambda () (east a-rover))
     (lambda () (west a-rover))
     (lambda () (south (rover (x a-rover) (- (y a-rover) 1))))
     (lambda () `(,(rover-out a-rover) s))
     ))
  )

(define (west a-rover)   
  (lambda (fn)
    (fn
     (lambda () (south a-rover))
     (lambda () (north a-rover))
     (lambda () (west (rover (- (x a-rover) 1) (y a-rover))))
     (lambda () `(,(rover-out a-rover) w))
     ))
  )


(define (east a-rover)   
  (lambda (fn)
    (fn
     (lambda () (north a-rover))
     (lambda () (south a-rover))
     (lambda () (east (rover (+ (x a-rover) 1) (y  a-rover))))

     (lambda () `(,(rover-out a-rover) e))
     ))
  )

;;tests
;rover x y
(x (rover 2 3))
(y (rover 2 3))
;left
(out (left (north (rover 1 1))))
(out (left (west (rover 1 1))))
(out (left (south (rover 1 1))))
(out (left (east (rover 1 1))))
;;right
(out (right (north (rover 1 1))))
(out (right (east (rover 1 1))))
(out (right (south (rover 1 1))))
(out (right (west (rover 1 1))))
;;move
(out (move (north (rover 1 1))))
(out (move (south (rover 1 1))))
(out (move (east (rover 1 1))))
(out (move (west (rover 1 1))))
;;move-turn
(out (move (move (left (move (left (move (left (move (left (north (rover 1 2))))))))))))
