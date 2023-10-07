; pass-test
#lang racket
(define nil '())
(define (split-at lst n)
  'YOUR-CODE-HERE
  (if (equal? (cdr lst) nil)
      (cons (list (car lst)) (cdr lst))
      (if (= n 0)
          (cons nil lst)
          (cons (cons (car lst) (car (split-at (cdr lst) (- n 1))))
                (cdr (split-at (cdr lst) (- n 1))))))
)


(define (compose-all funcs)
  'YOUR-CODE-HERE
  (if (equal? funcs nil)
      (lambda (x) x)
      (lambda (x) ((compose-all (cdr funcs)) ((car funcs) x))))
)

