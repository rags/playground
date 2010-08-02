(define (map1 fn l)
  (if (null? l) null
      (cons (fn (car l)) (map1 fn (cdr l)))))

(define (map2 fn l)
  (define (iter fn new-list list)
      (if (null? list) new-list
      (iter fn (cons new-list (fn (car list))) (cdr list))))
  (if (null? l) `()
  (iter fn `(,(fn (car l))) (cdr l))))


(map1 (λ (x) (+ 1 x)) `())
(map1 (λ (x) (+ 1 x)) `(1))
(map1 (λ (x) (+ 1 x)) `(1 2))
(map1 (λ (x) (+ 1 x)) `(1 2 3 4))

(map2 (λ (x) (+ 1 x)) `())
(map2 (λ (x) (+ 1 x)) `(1))
(map2 (λ (x) (+ 1 x)) `(1 2))
(map2 (λ (x) (+ 1 x)) `(1 2 3 4))