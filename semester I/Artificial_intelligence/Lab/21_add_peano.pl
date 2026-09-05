/*Question 21 - Write a predicate to add two Peano numbers.
  Note: plus/3 shadows SWI-Prolog's built-in plus/3; rename to add/3 if loading alongside library arithmetic.*/
plus(0,Y,Y).
plus(s(X), Y, s(Z)) :- plus(X,Y,Z).
