/*Question 16 - Write a predicate to check whether a given Peano number is even.*/
is_even(0).
is_even(s(s(X))) :- is_even(X).
