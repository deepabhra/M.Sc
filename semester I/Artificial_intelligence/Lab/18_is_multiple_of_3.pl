/*Question 18 - Write a predicate to check whether a given Peano number is a multiple of 3.*/
is_multiple_of_3(s(s(s(0)))).
is_multiple_of_3(s(s(s(X)))) :- is_multiple_of_3(X).
