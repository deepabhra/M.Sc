/*Question 19 - Write a predicate to check whether one Peano number is less than or equal to another.
  (is_natural/1 is repeated here as a helper so this file runs standalone.)*/
is_natural(0).
is_natural(s(X)) :- is_natural(X).

is_less_equal(0,Y) :- is_natural(Y).
is_less_equal(s(X),s(Y)) :- is_less_equal(X,Y).
