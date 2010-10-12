(define save-me 0)
(define (foo c)
  (call/cc (λ (k) 
  (display "here")
  (set! save-me k)           
  (c)
  (display "here again")))
  )

;(call/cc (λ (k) (foo k) ))
;(save-me)

;;;;;;;;;


; generate 1 2 3 as a sequence using special iterators
;  broken: only works from repl because returning to the previous
(define (gen3a)
  (call/cc (lambda (exit)
             (let loop ((x 1))
               (call/cc (lambda (resume)
                          (exit (lambda (msg)
                                  (cond
                                    ((eqv? msg 'get) x)
                                    ((eqv? msg 'next)
                                     (resume '()))
                                    (#t (raise-error)))))))
               (unless (= x 3) (loop (+ x 1))))
             (exit #f))))

; and try out this generator
(let continue ((it (gen3a)))
   (when it
      (display (it 'get))
      (continue (it 'next))))
