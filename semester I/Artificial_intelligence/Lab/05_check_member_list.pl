/*Question 5 - Write a program to check whether a given element is a member of a list or not.*/
member(X,[X|_]).
member(X,[_|Rest]):-
    member(X,Rest).