#lang racket
(define (deep-map fn lst)
  (if (null? lst)
      lst
      (if (list? (car lst))
          (cons (deep-map fn (car lst)) (deep-map fn (cdr lst)))
          (cons (fn (car lst)) (deep-map fn (cdr lst))))))
