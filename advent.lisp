(defpackage :advent-2021
  (:use :cl)
  (:export :day-1 :day-2))
(in-package :advent-2021)

(ql:quickload "cl-ppcre")

(defun read-file (file)
  (with-open-file (stream file)
    (loop for line = (read stream nil)
	  while line
	  collect line)))

(defun count-increases (list)
  (count-if (lambda (x) (apply #'< x)) (partition 2 1 list)))

(defun day-1-part-1 (file)
  (let ((input (read-file file)))
    (count-increases input)))

(defun nth-rest (n list)
  (if (plusp n)
      (nth-rest (1- n) (rest list))
      list))

(defun partition (n step list)
  (when (<= n (length list))
    (cons (subseq list 0 n) (partition n step (nth-rest step list)))))

(defun day-1-part-2 (file)
  (let* ((input (read-file file))
	 (moving-window (mapcar (lambda (x) (apply #'+ x))
				(partition 3 1 input))))
    (count-increases moving-window)))

(defun day-1 (input)
  (values (day-1-part-1 input)
	  (day-1-part-2 input)))

(defun move (list x y)
  (if (null list)
      (list x y)
      (let* ((action (first list))
	     (dir (first action))
	     (dist (second action)))
	(cond
	  ((eq dir 'forward) (move (rest list) (+ x dist) y))
	  ((eq dir 'down) (move (rest list) x (+ y dist)))
	  ((eq dir 'up) (move (rest list) x (- y dist)))))))

(defun day-2-part-1 (file)
  (let ((input (read-file file)))
    (apply #'* (move (partition 2 2 input) 0 0))))

(defun move2 (list x y aim)
  (if (null list)
      (list x y)
      (let* ((action (first list))
	     (dir (first action))
	     (dist (second action)))
	(cond
	  ((eq dir 'forward) (move2 (rest list) (+ x dist) (+ y (* aim dist)) aim))
	  ((eq dir 'down) (move2 (rest list) x y (+ aim dist)))
	  ((eq dir 'up) (move2 (rest list) x y (- aim dist)))))))

(defun day-2-part-2 (file)
  (let ((input (read-file file)))
    (apply #'* (move2 (partition 2 2 input) 0 0 0))))

(defun day-2 (file)
  (values (day-2-part-1 file)
	  (day-2-part-2 file)))

(defparameter *day3-test-input-string* "00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
")

(setq *day3-test-input* (cl-ppcre:split "\\s+" *day3-test-input-string*))

(defun nth-is-one? (str n)
  (eql #\1 (char str n)))

(defun partition-1-0 (list n)
  (labels ((helper (list n zeros ones)
	     (cond
	       ((null list) (list (nreverse zeros) (nreverse ones)))
	       ((eql (char (first list) n) #\0)
		(helper (rest list) n (cons (first list) zeros) ones))
	       (t (helper (rest list) n zeros (cons (first list) ones))))))
    (helper list n nil nil)))

(defun gamma-rate (list)
  (let ((l (length (first list))))
    (labels ((helper (list count num)
	       (if (= count l)
		   (coerce (nreverse num) 'string)
		   (let
		       ((p (partition-1-0 list count)))
		     (if (> (length (first p)) (length (second p)))
			 (helper list (1+ count) (cons #\0 num))
			 (helper list (1+ count) (cons #\1 num)))))))
      (helper list 0 nil))))
