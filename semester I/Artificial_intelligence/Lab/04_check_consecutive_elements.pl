/*Question 4 - Write a program to check whether two given elements occur consecutively in a list or not.*/
next_to(X,Y,[X|[Y|Rest]]).
next_to(X,Y,[_|Z]):-
    next_to(X,Y,Rest).