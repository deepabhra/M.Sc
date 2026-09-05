/*Question 15 - Using Peano (successor) notation, where 0 represents zero and s(X) represents the successor of X, write a predicate to check whether a given term is a natural number.*/
is_natural(0).
is_natural(s(X)) :- is_natural(X).
