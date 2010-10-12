(define (quick-sort list)
  (if (null? list) list
      (append(append (quick-sort (filter (λ (x) (< x (car list))) (cdr list))) 
                     `(,(car list)))
             (quick-sort (filter (λ (x) (> x (car list))) (cdr list))))))

(define (filter fn list)
  (define (is-append list cur)
    (if (fn cur) (append list `(,cur)) list))
  (define (iter filter-list cur list)
    (if (null? list) (is-append filter-list cur)
        
        (iter (is-append filter-list cur) (car list) (cdr list))))
  (if (null? list) list
      
      (iter `() (car list) (cdr list))))



(filter (λ (x) (> x 2)) `(1 2 3 4) )
(filter (λ (x) (> x 2)) `() )
(filter (λ (x) (> x 2)) `(3) )
(filter (λ (x) (> x 2)) `(1) )
(filter (λ (x) (> x 2)) `(1 4) )

(quick-sort `(2 1))
(quick-sort `(2 1 3 4))
(quick-sort `(1 2 1 2 -3 -2 0 4 5))