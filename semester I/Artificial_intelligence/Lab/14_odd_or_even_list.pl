/*Question 14 - Homework: Check whether the number of elements in a list is odd or even.*/
even([]).
even([_,_|L]) :-
    even(L).

odd([_]).
odd([_,_|L]) :-
    odd(L).