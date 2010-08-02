(define (iterator list)
  (call/cc (λ (end) 
             (let iter ((l list))
               (call/cc (λ (next)
                          (end (λ (f) (f l next)))))
               (unless (null? (cdr l)) (iter (cdr l))))))) 

(define (current list next) (car list))
(define (move-next list next) (next))

(let continue ((it (iterator `(1 2 3 4))))
   (unless (void? it)
      (newline) 
      (display (it current))
      (continue (it move-next))))



(define-syntax foreach (syntax-rules (:) ((_ (i : itr) body ...) 
                                           (let iter ((it itr))
                                             (unless (void? it) 
                                             (let ((i (it current)))
                                             body ...)
                                             (iter (it move-next)))))))

(foreach (x : (iterator `(1 2 3 4))) (display (* x 3)))                                             