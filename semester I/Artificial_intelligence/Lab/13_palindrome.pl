/*Question 13 - Homework: Check whether a list is a palindrome.*/
rev([],[]).
rev([X],[X]).
rev([X|L],L1) :-
    rev(L,L2),
    append(L2,[X],L1).

palindrome(L) :-
    rev(L,R),
    L = R.