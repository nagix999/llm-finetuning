Discretize (bin) numerical values[¶](#discretize-bin-numerical-values "Permalink to this heading")
==================================================================================================


Group numbers into bins (intervals).



Options[¶](#options "Permalink to this heading")
------------------------------------------------


**Input columns**


Number column to transform into bin.


**Binning mode**


Choose from two binning modes:


* **Fixed size intervals:** Define **bin width** to create bins of equal width. For example, `2` generates `...,-2:0, 0:2, 2:4, ....`



> + In each bin, the lower bound is included and the upper bound is excluded.
> 	+ **Minimum value:** Set a minimum value *N* below which the corresponding bin will be *\< N*. This also creates an offset for the bins: with `width=2` and `minimum=0.5`, the generated bins will be `0.5:2.5, 2.5:4.5, 4.5:6.5, ...`
> 	+ **Maximum value:** Set a maximum value *N* above which the corresponding bin will be *\>\= N.*
* **Custom, use raw values:** specify non\-overlapping intervals to create bins.



> + In each bin, the lower bound is included and the upper bound is excluded.
> 	+ If a bound isn’t specified, \+/\- infinity will be used.
> 	+ The output bin for a value that is out of the ranges will be an empty cell.


**Output column**


Perform the binning in an additional output column or leave it empty to perform the binning in place.