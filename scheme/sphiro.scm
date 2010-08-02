;x = (R+r)*cos(t) - (r+O)*cos(((R+r)/r)*t)
;y = (R+r)*sin(t) - (r+O)*sin(((R+r)/r)*t) 

(define PI (/ 22 7))  
(define DEGREE (/ PI 180))
(define (paint canvas dc) 
  (let (  (R -20)
          (r -75)
          (O 2)
          (inc .1)
          (T 5000)
          )       
    (define (iter t)
      (spiro-point dc R r t O)
      (if (> t T) 'done
          (iter (+ inc t))))
    
    (iter 1)
    )  
  )

(define (spiro-point dc R r t O)
  (send dc draw-point (x R r t O) (y r R t O)))

(define (x R r t O)
  (coord R r t O (trignom-func-deg cos)))

(define (y R r t O)
  (coord R r t O (trignom-func-deg sin)))

 (define (trignom-func-deg fn)
   (λ (int)
   (fn (* DEGREE int))))

(define (coord R r t O trignom-func)
  (let ((R+r (+ R r)))
  (- (* R+r (trignom-func t)) (* (+ R O) (trignom-func (* (/ R+r r) t))))))
  

(define frame (instantiate frame% ("Drawing Example") (width 800) (height 600)))
(define canvas (instantiate canvas% (frame) (paint-callback paint)))
(define dc (send canvas get-dc))
(send dc set-pen (instantiate pen% ("RED" 3 'solid)))
;(define msg (instantiate message% ("example" frame)))
;(instantiate button% () (label "click me")(parent frame)
;(callback (lambda (button event)(send msg set-label "button_click"))))


(send frame show #t) 
(sleep/yield 1) 

(define (range start end . step)
  (let ((i start)
        (_step (if (null? step) 1 (car step))))        
  (λ () 
         (if (> i end) 'done
         (let ((cur i))
           (set! i (+ i _step))
           cur))
         
         )))


;tests
(define range1 (range 0 2))
(equal? `(0 1 2 done) `(,(range1) ,(range1) ,(range1) ,(range1)))

(define range2 (range 0 10 3))
(equal? `(0 3 6 9 done) `(,(range2) ,(range2) ,(range2) ,(range2) ,(range2)))

