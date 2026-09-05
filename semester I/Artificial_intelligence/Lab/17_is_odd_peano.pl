/*Question 17 - Write a predicate to check whether a given Peano number is odd.*/
is_odd(s(0)).
is_odd(s(s(X))) :- is_odd(X).
