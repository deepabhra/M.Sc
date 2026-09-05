/*Question 25 - Write a predicate to compute the modulo (remainder) of dividing one Peano number by another.
  (plus/3, is_natural/1 and is_less_equal/2 are repeated here as helpers so this file runs standalone.)*/
is_natural(0).
is_natural(s(X)) :- is_natural(X).

is_less_equal(0,Y) :- is_natural(Y).
is_less_equal(s(X),s(Y)) :- is_less_equal(X,Y).

plus(0,Y,Y).
plus(s(X), Y, s(Z)) :- plus(X,Y,Z).

modu(X,X,0).
modu(X,Y,X) :- is_less_equal(X,Y).
modu(X,Y,Z) :- plus(U,Y,X), is_less_equal(Y,U), modu(U,Y,Z).
