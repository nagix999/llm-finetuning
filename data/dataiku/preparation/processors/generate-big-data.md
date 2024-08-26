Generate Big Data[¶](#generate-big-data "Permalink to this heading")
====================================================================


This processor generates Big Data out of small data.


The number of output rows will be exactly the number of input rows times the specified Expansion Factor.


The processor does not simply copy rows; instead, for numeric columns, it generates new values in the same range as the input values. For alphanumeric columns, it splits the column into words, and replaces each input word by a randomly selected one from the observed values.