(defun assert-equals (expected actual)
  (let ((eq-checker
	 (cond ((stringp expected) #'string=)
	       ((numberp expected) #'=)
	       ((listp expected)   #'equalp))))
    (assert-equality eq-checker expected actual)))

(defun assert-equality (eq-checker expected actual)
  (if (not (funcall eq-checker expected actual))      
      (error "expected %s but was %s" expected actual)))

(defun assert-true (exp) (if (not exp) (error "assertion failure")))

(defun assert-false (exp) (assert-true (not exp)))