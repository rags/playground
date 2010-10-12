(define MIN-LENGTH 3)

(define (count-composites file min-composites)
  (count-composite-words (read-file file) min-composites))

(define (read-file file-name)
  (read-stream (open-input-file file-name)))

(define (read-stream stream)
  ((λ (contents)
     (let recur ((contents contents))
       (let ((line (read-line stream)))
         (if (eof-object? line) contents
             (let ((trim-line (substring line 0 (- (string-length line) 1))))
               (if (< (string-length trim-line) MIN-LENGTH) 
                   (recur contents)
                   (recur (cons  trim-line contents)))))))) `()))  



(define (lazy-filter list predicate) 
  (λ (fn) (let ((new-list  (fn list predicate)))
            (if (null? new-list) 
                (begin (set! list new-list) list)
                (begin (set! list (cdr new-list)) (car new-list))))))

(define (next fn)
  (fn (λ (list predicate)
        (let recur ((list list) (predicate predicate))
          (if (or (null? list) (predicate (car list))) list
              (recur (cdr list) predicate))))))


(define (count-composite-words words min-composites)
  (count-composite-words-impl (lazy-filter words 
                                           (λ (word) (>= 
                                                      (string-length word) 
                                                      (* MIN-LENGTH min-composites))))
                              words 
                              min-composites))

(define (count-composite-words-impl candidate-words all-words min-composites)
  (define (iter count)
    (let ((candidate-word (next candidate-words)))
      (if (null? candidate-word) count
          (iter (+ count (if (is-composite? candidate-word all-words min-composites) 1 0))))))
  (iter 0))

(define (is-composite? the-word all-words min-partial-words)
  
  (define (composite-count word partial-words)
    (if (null? partial-words) 0
        (let ((cur-cnt (cur-composite-count word (car partial-words))))
          (if (and (>= cur-cnt min-partial-words) (string=? word the-word)) 
              cur-cnt
              (max  cur-cnt (composite-count word (cdr partial-words)))))))
  
  (define (cur-composite-count word partial-word)
    (cond ((string-ci=? word partial-word) 1)
          ((< (- (string-length word) (string-length partial-word)) MIN-LENGTH) 0)
          (else (let ((remaining-parts (split word partial-word)))
                  (if (null? remaining-parts) 0
                      (composite-count-parts (cons partial-word remaining-parts) 0))))))
  
  (define (composite-count-parts parts count)
    (if (null? parts) count
        (let ((car-cnt (composite-count (car parts) all-words)))
          (if (= car-cnt 0) 0
              (composite-count-parts (cdr parts) (+ count car-cnt))))))
  
  (>= (composite-count the-word all-words) min-partial-words))

(define (++ int) (+ int 1))


(define (split str substr)
  (let ((str-len (string-length str)))
    (define (incr index)
      (if (= 0 index) MIN-LENGTH          
          (++ index)))
    
    (define (contains? start len)
      (string-ci=? (substring str start (+ start len)) substr))
    
    (define (split-str start len)
      (cond ((= 0 start) `(,(substring str len)))
            ((= str-len (+ start len)) `(,(substring str 0 start)))
            (else `(,(substring str 0 start) ,(substring str (+ start len))))))
    (define (valid-trailing-len? len) (or (= 0 len) (>= len MIN-LENGTH)))
    ((λ (start len)    
       (let recur ((start start) (len len))
         (cond ((or (>= len str-len)               
                    (not (valid-trailing-len? (- str-len (+ start len))))
                    (> start  (- str-len MIN-LENGTH))) 
                null)
               ((contains? start len)  (split-str start len))
               (else (recur (incr start) len)))))
     0 (string-length substr))))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;Unit tests;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(require "test.scm")
(define list `(8 5 1 6))
(define strings (read-stream (open-input-string (string-append "fooblahboobar\r\n"
                                                               "blahfoobar\r\n"
                                                               "foo\r\n"
                                                               "bar\r\n"
                                                               "blah\r\n"
                                                               "fooboobar\r\n"
                                                               "boo\r\n"
                                                               "fooblah\r\n"
                                                               "barfoo\r\n"
                                                               "foobar\r\n"
                                                               "xfooybar\r\n"
                                                               "blahfo\r\n"
                                                               "blahblah\r\n"
                                                               "foobarfo\r\n"
                                                               "nonfoobar\r\n"
                                                               "fooblahbar\r\n"
                                                               "fooblah\r\n"
                                                               "boobar\r\n"
                                                               "blabar\r\n"
                                                               "bl\r\n"
                                                               "b\r\n"
                                                               "barrr\r")))) 

;;input read tests;;
(assert-equals 20 (length strings))
(assert-equals "barrr" (car strings))
(assert-equals "blabar" (cadr strings))
(assert-equals "fooblahboobar" (list-ref strings (- (length strings) 1)))

;;lazy-filter tests;;
(define list>5 (lazy-filter  list odd?))
(assert-equals 5 (next list>5))
(assert-equals 1 (next list>5))
(assert-equals null (next list>5))


(define list>5 (lazy-filter  list (λ (x) (> x 5))))
(assert-equals 8 (next list>5))
(assert-equals 6 (next list>5))
(assert-equals null (next list>5))

;;string split tests;;
(assert-equals '("bar") (split "foobar" "foo"))
(assert-equals '("foo") (split "foobar" "bar"))
(assert-equals '() (split "fooba" "foo"))
(assert-equals null (split "foobar" "OBA"))
(assert-equals '("foo" "blah") (split "foobarblah" "BAr"))
(assert-equals '() (split "foobarblah" "foobarblah"))

;;is-composite tests;;
(assert-true (is-composite? "fooblah" strings 2))
(assert-true (is-composite? "fooblahboobar" strings 2))
(assert-true (is-composite? "fooblahboobar" strings 4))
(assert-false (is-composite? "fooblahh" strings 2))

;;count-composite-words;;
(assert-equals 10 (count-composite-words strings 2))  
(assert-equals 4 (count-composite-words strings 3))
(assert-equals 1 (count-composite-words strings 4))
(assert-equals 0 (count-composite-words strings 5))
(assert-equals 0 (count-composite-words strings 6))

;;acceptance tests - sample inputs;;
(assert-equals 106 (count-composites "sample.txt" 2))
(assert-equals 3 (count-composites "sample.txt" 3))
(assert-equals 0 (count-composites "sample.txt" 4))
