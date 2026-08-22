/*Question 3 - Write a program to find the last element of a list.*/
last_element(X,[X]).
last_element(X,[_|Rest]):-
    last(X,Rest).