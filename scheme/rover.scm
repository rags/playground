(define (rover x y) (¦Ë (fn) (fn x y)))
(define (x rover) (rover (¦Ë (a b) a)))
(define (y rover) (rover (¦Ë (a b) b)))
(define (rover-out a-rover) `(,(x a-rover) ,(y a-rover)))

(define (left fn) (fn (¦Ë (left-impl right-impl move-impl out-impl) (left-impl))))

(define (right fn) (fn (¦Ë (left-impl right-impl move-impl out-impl) (right-impl))))

(define (move fn) (fn (¦Ë (left-impl right-impl move-impl out-impl) (move-impl))))

(define (out fn) (fn (¦Ë (left-impl right-impl move-impl out-impl) (out-impl))))



(define (north a-rover)   
  (¦Ë (fn)
    (fn
     (¦Ë () (west a-rover))
     (¦Ë () (east a-rover))
     (¦Ë () (north (rover (x a-rover) (+ (y a-rover) 1))))     
     (¦Ë () `(,(rover-out a-rover) n))
     ))
  )

(define (south a-rover)   
  (¦Ë (fn)
    (fn
     (¦Ë () (east a-rover))
     (¦Ë () (west a-rover))
     (¦Ë () (south (rover (x a-rover) (- (y a-rover) 1))))
     (¦Ë () `(,(rover-out a-rover) s))
     ))
  )

(define (west a-rover)   
  (¦Ë (fn)
    (fn
     (¦Ë () (south a-rover))
     (¦Ë () (north a-rover))
     (¦Ë () (west (rover (- (x a-rover) 1) (y a-rover))))
     (¦Ë () `(,(rover-out a-rover) w))
     ))
  )


(define (east a-rover)   
  (¦Ë (fn)
    (fn
     (¦Ë () (north a-rover))
     (¦Ë () (south a-rover))
     (¦Ë () (east (rover (+ (x a-rover) 1) (y  a-rover))))

     (¦Ë () `(,(rover-out a-rover) e))
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
;right
(out (right (north (rover 1 1))))
(out (right (east (rover 1 1))))
(out (right (south (rover 1 1))))
(out (right (west (rover 1 1))))
;move
(out (move (north (rover 1 1))))
(out (move (south (rover 1 1))))
(out (move (east (rover 1 1))))
(out (move (west (rover 1 1))))
;move-turn
(out (move (move (left (move (left (move (left (move (left (north (rover 1 2))))))))))))
