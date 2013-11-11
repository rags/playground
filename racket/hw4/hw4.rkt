
#lang racket

(provide (all-defined-out)) ;; so we can put tests in a second file

(define (sequence low high stride) 
    (if (> low high) null (cons low (sequence (+ low stride) high stride)))) 

(define (string-append-map xs suffix)
  (map (λ (str) (string-append str suffix)) xs))

(define (list-nth-mod xs n)
  (cond [(< n 0) (error "list-nth-mod: negative number")]
        [(null? xs) (error "list-nth-mod: empty list")]
        [#t (car (list-tail xs (remainder n (length xs))))]))

(define (stream-for-n-steps stream n) 
  (if (= 0 n) null (let [(pair (stream))] (cons (car pair) (stream-for-n-steps (cdr pair) (- n 1))))))

(define (funny-number-stream) 
  (define (stream n) (cons (if (= 0 (remainder n 5)) (- n) n) (λ () (stream (+ n 1)))))
  (stream 1))

(define (dan-then-dog)
  (define (stream cur-str) (cons cur-str (λ () (stream (if (eq? "dan.jpg" cur-str) "dog.jpg" "dan.jpg")))))
  (stream "dan.jpg"))

(define (stream-add-zero stream)
  (define (zero-stream s) 
    (let [(pair (s))]
    (cons (cons 0 (car pair))
          (λ () (zero-stream (cdr pair))))))
  (λ () (zero-stream stream)))

(define (cycle-lists xs ys)
  (define (first-non-null as bs)
    (if (null? as) bs as))
  (define (stream as bs) (cons (cons (car as) (car bs))
                               (λ () (stream (first-non-null (cdr as) xs) (first-non-null (cdr bs) ys))))) 
  (if (or (null? xs) (null? ys)) (error "cycle-lists: empty list as input")
      (λ () (stream xs ys))))

(define (vector-assoc v vec)
  (define (find i)
    (if (< i (vector-length vec))
        (let [(cur-ele (vector-ref vec i))]
          (if (and (pair? cur-ele) (equal? v (car cur-ele))) cur-ele (find (+ i 1))))
        #f))
  (find 0))

(define (cached-assoc xs n)
  (let [(cache (make-vector n #f))
        (i 0)]
    (define (lookup v)
      (let [(cached (vector-assoc v cache))]
        (if cached 
            (begin (print "from cache") cached) 
            (let [(value (assoc v xs))]
              (if value 
                  (begin (vector-set! cache i value)
                         (set! i (remainder (+ i 1) n))
                         value) 
                  #f)))))
    lookup))

(define-syntax while-less 
  (syntax-rules (do) [(_ v do body)
                      (let recur [(n v)]
                        (if (> n body) 
                            (recur n)
                            #t))]))
