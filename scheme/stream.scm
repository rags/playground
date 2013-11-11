#lang racket
(define (cons-stream x y)
;  (cons x y))
    (cons x (delay1 y)))

(define (delay1 x) (λ () x))

(define (head cons-stream) (car cons-stream))

(define (tail cons-stream) (force (cdr cons-stream)))

(define (force x) (x))

(define EMPTY-STREAM `())

(define (range low high)
  (if (> low high)
      EMPTY-STREAM
      (cons-stream
       low
       ;(λ () (range (+ low 1) high)))))
       (range (+ low 1) high))))

(define (n-th stream n)
  (define (find-nth i the-stream) (if (= n i) (head the-stream)
                         (find-nth (+ i 1) (tail the-stream))))
  (find-nth 1 stream))

;(define million-nums (range 1 1000000))

;(n-th million-nums 2)

(define (x y) (λ () y))

(define (ones) (cons-stream 1 ones))

(define all-ones (ones))