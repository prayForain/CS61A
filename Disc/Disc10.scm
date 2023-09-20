#lang racket
;Disc 10 Scheme, Scheme Lists
;pass-test

;3.1
(define a (+ 1 2))
a
; 3

(define b (- (+ (* 3 3 ) 2) 1))
(= (modulo b a) (quotient 5 3))
; #t

;4.1 WWSD
(if (or #t (/ 1 0)) 1 (/ 1 0))
; 1

((if (< 4 3) + -) 4 100)
; -96

;4.1
(define (factorial x)
  (if (= x 0)
      1
      (* x (factorial (- x 1)))))

;4.2
(define (fib n)
  (if (= n 0)
      0
      (if (= n 1)
          1
          (+ (fib (- n 1)) (fib (- n 2))))))

;5.1
(define nil '())
(define (my-append a b)
  (if (equal? (cdr a) nil)
      (cons (car a) b)
      (cons (car a) (my-append (cdr a) b))))

;5.2
(define s '(5 4 (1 2) 3 7))
; (car (cdr (cdr (cdr s))))

;5.3
(define (duplicate lst)
  (if (equal? lst nil)
      nil
      (cons (car lst) (cons (car lst) (duplicate (cdr lst))))))

;5.4
(define (insert element lst index)
  (if (= index 0)
      (cons element lst)
      (cons (car lst) (insert element (cdr lst) (- index 1)))))





