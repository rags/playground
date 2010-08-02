;<point>
(define new-point cons)
(define x car)
(define y cdr)
;</point>

;<line>
(define (new-line x1 y1 x2 y2) 
  (cons (new-point x1 y1) (new-point x2 y2)))

(define point1 car)
(define point2 cdr)

(define (axis-diff line axis)
  (abs- (axis (point2 line)) (axis (point1 line))))
;</line>

;<traingle>
(define (new-triangle line)
  (λ () line))

(define (hypotenuse triangle) (triangle))
(define (height triangle) (dimension triangle y))
(define (width triangle) (dimension triangle x))

(define (dimension triangle axis) (axis-diff (hypotenuse triangle) axis))
(define (ratio triangle) (/ (height triangle) (width triangle)))

(define (triangle-axis-point triangle axis-point)
  (axis-point (hypotenuse triangle)))

(define (xy1 triangle) (point1 (triangle)))
(define (xy2 triangle) (point2 (triangle)))
;</traingle>

(define (intersections triangle)
  (let ((x-ratio (/ 1 (ratio triangle)))
        (y-ratio (ratio triangle))
        (triangle-pt1 (xy1 triangle))         
        (triangle-pt2 (xy2 triangle)))
    (make-unique-list
     (intersects-along-a-axis triangle-pt1 triangle-pt2 1 y-ratio)
     (intersects-along-a-axis triangle-pt1 triangle-pt2 x-ratio 1))))

(define (delta-fn pt1 pt2 axis)
  (if (< (axis pt1) (axis pt2)) + -))

(define (intersects-along-a-axis pt1 pt2 x-delta y-delta)
  (let ((x-delta-fn (delta-fn pt1 pt2 x))
        (y-delta-fn (delta-fn pt1 pt2 y)))    
    (calc-intersects pt1 pt2 (λ (x) (x-delta-fn x x-delta)) (λ (y) (y-delta-fn y y-delta)) `())))

(define (calc-intersects pt1 pt2 next-x next-y intersections)
  (define (iter point intersections)
    (let ((next-point (new-point (next-x (x point)) (next-y (y point)))))
      (if (equal? pt2 next-point) intersections
          (iter next-point (cons  next-point intersections)))))
  (iter pt1 intersections))


(define (make-unique-list horizontal-intersections vertical-intersections)
  (if (null? vertical-intersections) horizontal-intersections
      (let ((vertical-intersection (car vertical-intersections)))
        (if (is-duplicate? vertical-intersection) 
            (make-unique-list horizontal-intersections (cdr vertical-intersections))
            (make-unique-list (cons vertical-intersection horizontal-intersections) (cdr vertical-intersections))))))

(define (is-duplicate? point) (and (integer? (x point)) (integer? (y point))))

(define (unit-difference? num1 num2)
  (= 1 (abs- num1 num2)))

(define (abs- num1 num2) (abs (- num1 num2)))  

(define (count-squares-in-triangle triangle)
  (+ (length (intersections triangle)) 1))

(define (count-squares x1 y1 x2 y2)
  (cond ((or (= x1 x2) (= y1 y2)) 0)
        ((unit-difference? x1 x2) (abs- y1 y2))
        ((unit-difference? y1 y2) (abs- x1 x2))
        ((= (abs- y1 y2) (abs- x1 x2)) (abs- x1 x2))
        (else (count-squares-in-triangle (new-triangle (new-line x1 y1 x2 y2))))))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;Unit tests;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(require "test.scm")
(define triangle0306 (new-triangle (new-line 0 3 0 6)))
(define triangle53103 (new-triangle (new-line 5 3 10 3)))
(define triangle1154 (new-triangle (new-line 1 1 5 4)))
(define triangle1175 (new-triangle (new-line 1 1 7 5)))
(define triangle1176 (new-triangle (new-line 1 1 7 6)))
(define triangle1166 (new-triangle (new-line 1 1 6 6)))
(define triangle1671 (new-triangle (new-line 1 6 7 1)))

;;width test;;
(assert-equals 0 (width triangle0306)) 
(assert-equals 5 (width triangle53103)) 
(assert-equals 4 (width triangle1154)) 
(assert-equals 6 (width triangle1175))
(assert-equals 6 (width triangle1176))

;;height test;;
(assert-equals 3 (height triangle0306)) 
(assert-equals 0 (height triangle53103)) 
(assert-equals 3 (height triangle1154)) 
(assert-equals 4 (height triangle1175))
(assert-equals 5 (height triangle1176))

;;ratio test;;
(assert-equals 5/6 (ratio triangle1176))
(assert-equals 5/6 (ratio triangle1176))
;;intersections tests;;
(define triangle1175-intersects    
  `(,(new-point 5/2 2) 
    ,(new-point 11/2 4)
    ,(new-point 6 13/3)
    ,(new-point 5 11/3)
    ,(new-point 4 3)
    ,(new-point 3 7/3)
    ,(new-point 2 5/3)))
(assert-equals triangle1175-intersects (intersections triangle1175))

(assert-equals 8 (count-squares-in-triangle triangle1175))
(assert-equals 10 (count-squares-in-triangle triangle1176))
(assert-equals 5 (count-squares-in-triangle triangle1166))
(assert-equals 10 (count-squares-in-triangle triangle1671))

;;;;;;;;;;;;;;;;;;;;;;;;;;;Acceptance tests - SAMPLE INPUTS::::::::::::::::::::::::::::::::::::::::
(assert-equals 5 (count-squares 1 1 6 6))
(assert-equals 10 (count-squares 1 1 7 6 ))
(assert-equals 8 (count-squares 1 1 7 5))

(assert-equals 0 (count-squares 5 6 500 6))
(assert-equals 376 (count-squares 1 200 180 2 ))
(assert-equals 19824  (count-squares 1 10000 9999 173))