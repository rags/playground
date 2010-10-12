(define (read-file file-name)
  (define (iter file contents)
  (let ((line (read-line file)))
    (if (eof-object? line) contents
        (iter file (cons line contents)))))
  (iter (open-input-file file-name) `()))

(read-file "C:\\Users\\rramakri\\Desktop\\pbms\\sample.txt")

