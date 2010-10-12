(define Y (λ (f) ((λ (fn) (f (λ (l) ((fn fn) l))))  
            (λ (fn) (f (λ (l) ((fn fn) l)))))))           
           

(define Y! (λ (f)  (letrec ((fn (f  (λ (l) (fn l))))) fn)))

(define Y1! (λ (f)  (let ((fn (λ (l) `()))) (set! fn (f (λ (l) (fn l)))) fn)))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;tests;;;;;;;;;;;;;;;;;;;;;;
(define len (Y (λ (fn) 
                    (λ (l) 
                      (cond ((null? l) 0) 
                             (else (+ 1 (fn (cdr l)))))))))

(define len! (Y! (λ (fn) 
                    (λ (l) w
                      (cond ((null? l) 0) 
                             (else (+ 1 (fn (cdr l)))))))))

(define len1 (Y1! (λ (fn) 
                    (λ (l) 
                      (cond ((null? l) 0) 
                             (else (+ 1 (fn (cdr l)))))))))




(define lst2 `(1))
;(len `(1 2 3 ))
;(len1 `(1 4 5 6 7 8 9 9))
(define lst5 `(1 35 5 5  55 5 5 5 5 5 5 5 5 5 55 5 5 5 5))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;biz;;;;;;;;;;;;;;;;;;;;;;;;;;;
(define biz
  (let ((x 0)) 
    (λ (f) 
      (set! x (+ 1 x))
      (λ (a) (if (= a x) 0 (f a))))))


;((Y biz) 5)
((Y! biz) 5)
;((Y!1 biz) 5)

