#lang racket
(define (mycons x y) (λ (f) (f x y))) 
(define (mycar x) (x (λ (a b) a)))
(define (mycdr x) (x (λ (a b) b)))
