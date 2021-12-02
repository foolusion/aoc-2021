(defpackage :advent-2021
  (:use :cl)
  (:export :day-1 :day-2))
(in-package :advent-2021)

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
