/*Question 1 - Consider a list like [a,a,b], [[a,b],[a,b],c,d],such lists are called double headers [e,e,[f]] as the first two elements of the list are the same. Write a predicate to find if a list is a double header or not.*/

double_header([X|[X|_]]).