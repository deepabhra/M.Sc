/*Question 20 - Write a predicate to check whether one Peano number is greater than or equal to another.
  (is_natural/1 is repeated here as a helper so this file runs standalone.)*/
is_natural(0).
is_natural(s(X)) :- is_natural(X).

is_greater_equal(Y,0) :- is_natural(Y).
is_greater_equal(s(X),s(Y)) :- is_greater_equal(X,Y).
