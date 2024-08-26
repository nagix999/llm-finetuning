Round numbers[¶](#round-numbers "Permalink to this heading")
============================================================


Round decimal numbers in one or several columns using round, floor, or ceil.



Options[¶](#options "Permalink to this heading")
------------------------------------------------


**Column**


Apply rounding to numbers in the following:


* A single column
* An explicit list of columns
* All columns matching a regex pattern
* All columns


**Rounding mode**


Select how to round numbers:


* Round: Round the number to the specified significant digit.
* Floor: Round the number down, or toward zero.
* Ceil: Round the number up, or away from zero.


**Significant digits**


Control the *precision* of the number. `1234.5` with 2 significant digits is `1200`. Using 0 means the number is unbounded and keeps all significant digits.


**Decimal places**


How many numbers to show after the decimal point. `1.234` with 1 decimal place is `1.2`. Using 0 rounds to the integer; \-2 rounds to the hundreds.