# Prolog List Terminology

- `[]` or `[ ]` — **Empty list**
- `[a]`, `[x]`, `[_]` — **Singleton list**
- `[a,b]`, `[x,y]` — **Two-element list** / **Doubleton list**
- `[a,b,c]` — **Three-element list** / **Tripleton list**
- `[a,b,c,d]` — **Four-element list**
- `[a,b,c,...]` — **Finite list**
- `[H|T]` — **Non-empty list**, represented using **head–tail notation**
- `[_|_]` — **Non-empty list** with unspecified head and tail
- `[_|[]]` — **Singleton list**

## Notes

- **Singleton list** is standard Prolog terminology.
- **Doubleton list** is understandable, but **two-element list** is more commonly used.
- Similarly, **three-element list** is generally clearer than **tripleton list**.
- In Prolog, `[H|T]` is the standard notation for decomposing a list into its **head** (`H`) and **tail** (`T`).
---
**Question1 - consider a list like [a,a,b] [[a,b], [a,b], c, d], such list are called double headers [e, e, [f]] as the first two elememts of the list are same. Write a predicate to find if a list is a double header or not?**
