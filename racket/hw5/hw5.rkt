;; Programming Languages, Homework 5

#lang racket
(provide (all-defined-out)) ;; so we can put tests in a second file

;; definition of structures for MUPL programs - Do NOT change
(struct var  (string) #:transparent)  ;; a variable, e.g., (var "foo")
(struct int  (num)    #:transparent)  ;; a constant number, e.g., (int 17)
(struct add  (e1 e2)  #:transparent)  ;; add two expressions
(struct ifgreater (e1 e2 e3 e4)    #:transparent) ;; if e1 > e2 then e3 else e4
(struct fun  (nameopt formal body) #:transparent) ;; a recursive(?) 1-argument function
(struct call (funexp actual)       #:transparent) ;; function call
(struct mlet (var e body) #:transparent) ;; a local binding (let var = e in body) 
(struct apair (e1 e2)     #:transparent) ;; make a new pair
(struct fst  (e)    #:transparent) ;; get first part of a pair
(struct snd  (e)    #:transparent) ;; get second part of a pair
(struct aunit ()    #:transparent) ;; unit value -- good for ending a list
(struct isaunit (e) #:transparent) ;; evaluate to 1 if e is unit else 0

;; a closure is not in "source" programs; it is what functions evaluate to
(struct closure (env fun) #:transparent) 


;; Problem 1


(define (racketlist->mupllist lst)
  (if (null? lst) 
      (aunit)
      (apair (car lst) (racketlist->mupllist (cdr lst)))))


(define (mupllist->racketlist lst)
  (if (aunit? lst) 
      null
      (cons (apair-e1 lst) (mupllist->racketlist (apair-e2 lst)))))

;; Problem 2

;; lookup a variable in an environment
;; Do NOT change this function
(define (envlookup env str)
  (cond [(null? env) (error "unbound variable during evaluation" str)]
        [(equal? (car (car env)) str) (cdr (car env))]
        [#t (envlookup (cdr env) str)]))

;; Do NOT change the two cases given to you.  
;; DO add more cases for other kinds of MUPL expressions.
;; We will test eval-under-env by calling it directly even though
;; "in real life" it would be a helper function of eval-exp.

(define (value? e) (or (int? e) (aunit? e) (closure? e)))

(define (pair-accesor e env fn)
  (let ([pr (eval-under-env e env)]) (if (apair? pr) (fn pr) (error "MUPL fst/snd requires apair"))))

(define (eval-under-env e env)
  (cond [(var? e) 
         (envlookup env (var-string e))]
        [(value? e) e]
        [(fun? e) (if (and (string? (fun-formal e)) 
                           (or (string? (fun-nameopt e)) (not (fun-nameopt e)))) 
                      (closure env e)
                      ("MUPL fun needs namepopt to be string or #f and a parameter name"))]
        [(call? e)(let* ([c (eval-under-env (call-funexp e) env)]
                         [arg (eval-under-env (call-actual e) env)]
                         [f (closure-fun c)]
                         [fenv (closure-env c)]
                         [arg-name (fun-formal f)]
                         [fbody (fun-body f)]
                         [fname (fun-nameopt f)])
                    (eval-under-env fbody (cons (cons fname c) (cons (cons arg-name arg) fenv))))]
        [(add? e) 
         (let ([v1 (eval-under-env (add-e1 e) env)]
               [v2 (eval-under-env (add-e2 e) env)])
           (ensure-all-ints "MUPL addition applied to non-number" v1 v2)
           (int (+ (int-num v1) 
                   (int-num v2))))]
        
        [(ifgreater? e)
         (let ([v1 (eval-under-env (ifgreater-e1 e) env)]
               [v2 (eval-under-env (ifgreater-e2 e) env)])
           (ensure-all-ints "MUPL ifgreater expected int? for e1 and e2" v1 v2)
           (if (> (int-num v1) (int-num v2)) 
               (eval-under-env (ifgreater-e3 e) env) 
               (eval-under-env (ifgreater-e4 e) env)))]
        [(mlet? e) (eval-under-env (mlet-body e) (cons (cons (mlet-var e) (eval-under-env (mlet-e e) env)) env))]
        [(apair? e) (apair (eval-under-env (apair-e1 e) env) (eval-under-env (apair-e2 e) env))]
        [(fst? e) (pair-accesor (fst-e e) env apair-e1)]
        [(snd? e) (pair-accesor (snd-e e) env apair-e2)]
        [(isaunit? e) (int (if (aunit? (eval-under-env (isaunit-e e) env)) 1 0))]
        
        ;; CHANGE add more cases here
        [#t (error (format "bad MUPL expression: ~v" e))]))

(define (ensure-all-ints err-msg . es)
  (cond [(null? es) #t]
        [(not (int? (car es))) (error err-msg)]
        [#t (apply ensure-all-ints err-msg (cdr es))]))


;; Do NOT change
(define (eval-exp e)
  (eval-under-env e null))
        
;; Problem 3

(define (ifaunit e1 e2 e3) 
  (ifgreater (isaunit e1) (int 0) e2 e3))

(define (mlet* lstlst e2) 
  (if (null? lstlst) e2
      (mlet (caar lstlst) (cdar lstlst) (mlet* (cdr lstlst) e2))))

(define (ifeq e1 e2 e3 e4) 
  (mlet* (list (cons "_x" e1) (cons "_y" e2))
         (ifgreater (var "_x") (var "_y") e4 (ifgreater (var "_y") (var "_x") e4 e3))))

;; Problem 4

  
(define mupl-map
  (fun #f "_f"
       (fun "_map" "_lst"
            (ifaunit (var "_lst") (aunit)
                     (apair (call (var "_f") (fst (var "_lst")))
                            (call (var "_map") (snd (var "_lst"))))))))

(define mupl-mapAddN 
  (mlet "map" mupl-map
        (fun #f "i"
          (call (var "map") (fun #f "x" (add (var "i") (var "x")))))))

;; Challenge Problem

(struct fun-challenge (nameopt formal body freevars) #:transparent) ;; a recursive(?) 1-argument function

(define (free-vars e env)
    (cond [(var? e)
           (if (not (set-member? env (var-string e))) 
               (set (var-string e)) (set))]
           [(add? e) (set-union 
                        (free-vars (add-e1 e) env)
                        (free-vars (add-e2 e) env))]
           [(ifgreater? e) (set-union 
                              (free-vars (ifgreater-e1 e) env)
                              (free-vars (ifgreater-e2 e) env)
                              (free-vars (ifgreater-e3 e) env)
                              (free-vars (ifgreater-e4 e) env))]
           [(fun? e) (free-vars (fun-body e) (set-add (set-add env (fun-formal e)) (fun-nameopt e)))]
           [(call? e) (set-union (free-vars (call-funexp e) env) (free-vars (call-actual e) env))]
           [(mlet? e) (set-union (free-vars (mlet-e e) env) (free-vars (mlet-body e) (set-add env (mlet-var e))))]
           [(apair? e) (set-union (free-vars (apair-e1 e) env) (free-vars (apair-e2 e) env))]
           [(fst? e) (free-vars (fst-e e) env)]
           [(snd? e) (free-vars (snd-e e) env)]
           [(isaunit? e) (free-vars (isaunit-e e) env)]
           [(closure? e) (free-vars (closure-fun e) (append env (closure-env e)))]
           [#t (set)]))
  
;; We will test this function directly, so it must do
;; as described in the assignment
(define (compute-free-vars e) 
  (cond [(add? e) (add 
                   (compute-free-vars (add-e1 e))
                   (compute-free-vars (add-e2 e)))]
        [(ifgreater? e) (ifgreater 
                         (compute-free-vars (ifgreater-e1 e))
                         (compute-free-vars (ifgreater-e2 e))
                         (compute-free-vars (ifgreater-e3 e))
                         (compute-free-vars (ifgreater-e4 e)))]
        [(fun? e) (fun-challenge (fun-nameopt e) 
                                 (fun-formal e) 
                                 (compute-free-vars (fun-body e))
                                 (free-vars e (set)))]
        [(call? e) (call 
                    (compute-free-vars (call-funexp e)) 
                    (compute-free-vars (call-actual e)))]
        [(mlet? e) (mlet (mlet-var e) 
                         (compute-free-vars (mlet-e e))  
                         (compute-free-vars (mlet-body e)))]
        [(apair? e) (apair (compute-free-vars (apair-e1 e)) (compute-free-vars (apair-e2 e)))]
        [(fst? e) (fst (compute-free-vars (fst-e e)))]
        [(snd? e) (snd (compute-free-vars (snd-e e)))]
        [(isaunit? e) (isaunit (compute-free-vars (isaunit-e e)))]
        [(closure? e) (closure (closure-env e) (compute-free-vars (closure-fun e)))]
        [#t e]))


;; Do NOT share code with eval-under-env because that will make
;; auto-grading and peer assessment more difficult, so
;; copy most of your interpreter here and make minor changes
(define (eval-under-env-c e env) 
  (define (filter-free-vars en free-vars)
    (if (null? en) en
        (let ([cur (caar en)]
              [rest (filter-free-vars (cdr en) free-vars)])
          (if (set-member? free-vars cur)
              (cons (car en) rest)
              rest))))
  (cond [(var? e) 
         (envlookup env (var-string e))]
        [(value? e) e]
        [(fun? e) (error "MUPL fun not an allowed construct for challenge-eval")]
        [(fun-challenge? e) (if (and (string? (fun-challenge-formal e)) 
                                     (or (string? (fun-challenge-nameopt e)) 
                                         (not (fun-challenge-nameopt e)))) 
                                (closure (filter-free-vars env (fun-challenge-freevars e)) e)
                                ("MUPL fun needs namepopt to be string or #f and a parameter name"))]
        [(call? e)(let* ([c (eval-under-env-c (call-funexp e) env)]
                         [arg (eval-under-env-c (call-actual e) env)]
                         [f (closure-fun c)]
                         [fenv (closure-env c)]
                         [arg-name (fun-challenge-formal f)]
                         [fbody (fun-challenge-body f)]
                         [fname (fun-challenge-nameopt f)])
                    (eval-under-env-c fbody (cons (cons fname c) (cons (cons arg-name arg) fenv))))]
        [(add? e) 
         (let ([v1 (eval-under-env-c (add-e1 e) env)]
               [v2 (eval-under-env-c (add-e2 e) env)])
           (ensure-all-ints "MUPL addition applied to non-number" v1 v2)
           (int (+ (int-num v1) 
                   (int-num v2))))]
        
        [(ifgreater? e)
         (let ([v1 (eval-under-env-c (ifgreater-e1 e) env)]
               [v2 (eval-under-env-c (ifgreater-e2 e) env)])
           (ensure-all-ints "MUPL ifgreater expected int? for e1 and e2" v1 v2)
           (if (> (int-num v1) (int-num v2)) 
               (eval-under-env-c (ifgreater-e3 e) env) 
               (eval-under-env-c (ifgreater-e4 e) env)))]
        [(mlet? e) (eval-under-env-c (mlet-body e) (cons (cons (mlet-var e) (eval-under-env-c (mlet-e e) env)) env))]
        [(apair? e) (apair (eval-under-env-c (apair-e1 e) env) (eval-under-env-c (apair-e2 e) env))]
        [(fst? e) (pair-accesor-c (fst-e e) env apair-e1)]
        [(snd? e) (pair-accesor-c (snd-e e) env apair-e2)]
        [(isaunit? e) (int (if (aunit? (eval-under-env-c (isaunit-e e) env)) 1 0))]
        
        ;; CHANGE add more cases here
        [#t (error (format "bad MUPL expression: ~v" e))]))

(define (pair-accesor-c e env fn)
  (let ([pr (eval-under-env-c e env)]) (if (apair? pr) (fn pr) (error "MUPL fst/snd requires apair"))))

;; Do NOT change this
(define (eval-exp-c e)
  (eval-under-env-c (compute-free-vars e) null))
