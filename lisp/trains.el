(defun new-node (name &rest neighbours) (cons name neighbours))
(defalias 'new-neighbour 'cons)
(defalias 'name-of 'car)
(defalias 'neighbours-of 'cdr)
(defalias 'neighbour 'car)
(defalias 'distance 'cdr)
(defalias 'set-neighbours 'setcdr)
(defalias 'same-node? 'equalp)
(defvar NO-ROUTE -1)
  
(defun add-neighbours (node &rest neighbours) 
  (set-neighbours node
	      (nconc (neighbours-of node) neighbours)))

(defun empty? (list) (equalp list nil))

(defun distance-between (node othernode)
  (defun find-node (neighbour-list)
    (cond ((empty? neighbour-list) NO-ROUTE)
	  ((same-node? othernode (neighbour (car neighbour-list)))
	   (distance (car neighbour-list)))
	  (t (find-node (cdr neighbour-list)))))
  (find-node (neighbours-of node)))

(defun distance-route (&rest args)
  (defun distance-impl (nodes distance)
    (if (< (length nodes) 2) distance
      (let ((dist (distance-between (car nodes) (cadr nodes))))
	(message "here")
	(if (= NO-ROUTE dist) NO-ROUTE
	  (distance-impl (cdr nodes) (+ dist distance))))))
  (distance-impl args 0))

;(defun routes (source destination constraint)
;  (defun routes constraint

;;;;;;;;;;;;;;;;;;;;Setup the digraph;;;;;;;;;;;;;;;;;;;;
(defvar A (new-node "A"))
(defvar B (new-node "B"))
(defvar C (new-node "C"))
(defvar D (new-node "D"))
(defvar E (new-node "E"))

(add-neighbours A
		(new-neighbour B 5)
		(new-neighbour D 5)
		(new-neighbour E 7))
(add-neighbours B
		(new-neighbour C 4))
(add-neighbours C
		(new-neighbour D 8)
		(new-neighbour E 2))
(add-neighbours D
		(new-neighbour C 8)
		(new-neighbour E 6))
(add-neighbours E (new-neighbour B 3))


;;;;;;;;;;;;;;;;;;;;Tests;;;;;;;;;;;;;;;;;;;;
(load-file "test.el")
(assert-equals 5 (distance-between A B))
(assert-equals 3 (distance-between E B))
(assert-equals -1 (distance-between A C))

(assert-equals 0 (distance-route A))
(assert-equals 5 (distance-route A B))
(assert-equals NO-ROUTE (distance-route A C))
(assert-equals 9 (distance-route A B C))
(assert-equals 5 (distance-route A D))
(assert-equals 13 (distance-route A D C))
(assert-equals 22 (distance-route A E B C D))
(assert-equals NO-ROUTE (distance-route A E D))
