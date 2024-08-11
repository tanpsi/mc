                              Macho calculator
              (If you have used bc on some *nix system, this is mc)


This uses python's AST implemetation to parse user input.  It also uses python's
decimal module to store all numbers which avoids floating point representation
error within its precision (try `>>> 0.2 + 0.1` in a python prompt to see).
Normal assignments to variables are permitted and they can be used once assigned
some value, some common value (pi and e) are already present at startup.
Augmented assignments (+=, *=, ...) are not implemented. Available functions are
sin, cos, tan, cosec, sec, cot, ln, log, sqrt, fact, abs. I've tried to catch
most internal errors but some might still remain. Multiple statements can be
given on a single prompt by separating them with semicolons, their outputs will
also be separated with semicolons. The quadratic solver is implemented as a
separate command. You can use,
	> quad a b c
to get the solution(s) for the quadratic equation `ax**2 + bx + c`.

NOTE: This calculator uses the same syntax for exponentiation as python (**).

NOTE2: See mymath.py for implementations for functions.

NOTE3: Use `python main.py` to run.

NOTE4: For implementing sqrt and log functions I've used Newton's method. For
log this means I'm raising e to arbitrary powers which python's exponentiation
operator allows. I could use the the same (x**0.5) for sqrt but I haven't.

Improvements that can be made:
- Use multiprocessing in function implementations and choose better
  series/alogrithms for them.
- Allow symbolic representation for equations, polynomials, expressions, ...
- Allow things like `5x` to work just like `5*x`. It raises an error right now.
- Give descriptive errors telling what really went wrong, right now only a
  single error message is provided for all errors.
