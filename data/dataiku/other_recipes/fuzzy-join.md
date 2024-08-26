Fuzzy join: joining two datasets[¶](#fuzzy-join-joining-two-datasets "Permalink to this heading")
=================================================================================================



* [Fuzzy join prepare recipe processor](#fuzzy-join-prepare-recipe-processor)
* [Building a simple join](#building-a-simple-join)
* [Join conditions](#join-conditions)
* [Available distances](#available-distances)


	+ [Text columns](#text-columns)
	+ [Numeric columns](#numeric-columns)
	+ [Geopoint columns](#geopoint-columns)
* [Additional settings](#additional-settings)


	+ [Output matching details](#output-matching-details)
	+ [Debug mode](#debug-mode)
* [Columns in the output](#columns-in-the-output)
* [Engines](#engines)



The “fuzzy join” recipe is dedicated to joins between two datasets when join keys don’t match exactly.


It works by calculating a distance chosen by user and then comparing it to a threshold. DSS handles inner, left, right or outer joins.



See also


For more information, see the [Tutorial \| Fuzzy join recipe](https://knowledge.dataiku.com/latest/data-preparation/visual-recipes/tutorial-fuzzy-join.html) article in the Knowledge Base.




[Fuzzy join prepare recipe processor](#id1)[¶](#fuzzy-join-prepare-recipe-processor "Permalink to this heading")
----------------------------------------------------------------------------------------------------------------


DSS has another way to fuzzy join datasets, by using a [dedicated prepare recipe processor](../preparation/processors/fuzzy-join.html). However a separate fuzzy join recipe is preferred as it has less technical limitations and works with larger datasets.




[Building a simple join](#id2)[¶](#building-a-simple-join "Permalink to this heading")
--------------------------------------------------------------------------------------


When the recipe is first created it will try to automatically find matching columns based on their name and type. One to five initial conditions will be provided, but this list can be changed by user.


Adding join is a process involving several configuration steps. In the “Join” section of the recipe (in the left pane):


* Click on an existing join conditions list or on a message “No join condition” to add a new condition.
* Select the join type, between “Inner”, “Outer”, “Left” or “Right”.
* Fill in the join conditions. Conditions can be added with the “\+” button, and removed with the “Remove” button (after selecting one).


Once the join definition is ready, go to the “Selected columns” section of the recipe and select the columns of each dataset whose values you want to get.


Finally, review the execution specs in the “Output” section.




[Join conditions](#id3)[¶](#join-conditions "Permalink to this heading")
------------------------------------------------------------------------


Each join condition describes a matching rule for two columns. Depending on column types different options will be available.



Note


If all of the join conditions are set to strict equality then a fuzzy join recipe will be equivalent to a regular join recipe. In this case a regular join is preferred as it’s more performant.





[Available distances](#id4)[¶](#available-distances "Permalink to this heading")
--------------------------------------------------------------------------------



### [Text columns](#id5)[¶](#text-columns "Permalink to this heading")


* [Damerau–Levenshtein](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance) \- an edit distance between two sequences. Informally, the Damerau–Levenshtein distance between two words is the minimum number of operations (consisting of insertions, deletions or substitutions of a single character, or transposition of two adjacent characters) required to change one word into the other.
* [Hamming](https://en.wikipedia.org/wiki/Hamming_distance) \- a distance between two strings of equal length is the number of positions at which the corresponding symbols are different.
* [Jaccard](https://en.wikipedia.org/wiki/Jaccard_index) \- a distance, which measures dissimilarity between sample sets of characters from joined strings. Calculated as a size of a set containing common characters divided by a size of a set containing all characters from both strings.
* [Cosine](https://en.wikipedia.org/wiki/Cosine_similarity) \- a distance is measured by converting strings into vectors by counting characters appearing in both strings and then calculating a dot product of two vectors.


Also text values can be normalized before joining, a list of possible operations includes:




| Name | Description | Example before | Example after |
| --- | --- | --- | --- |
| Case insensitive | Ignores case when matching characters | Hello, the Mister Lefèvre | hello, the mister lefèvre |
| Remove punctuation and extra spaces | Removes punctuation and extra spaces | Hello, the Mister Lefèvre | Hello the Mister Lefèvre |
| Clear salutations | Removes English salutations, e.g. Miss, Sir, Dr | Hello, the Mister Lefèvre | Hello, the Lefèvre |
| Clear stop words | Removes common stop words depending on the language | Hello, the Mister Lefèvre | Hello Mister Lefèvre |
| Transform to stem | Transforms words to base form (Snowball stemmer) | Monkeys eat bananas | Monkey eat banana |
| Alphabetic sorting of words | Alphabetic sorting of words | Hello, the Mister Lefèvre | Hello Lefèvre Mister the |




### [Numeric columns](#id6)[¶](#numeric-columns "Permalink to this heading")


* [Euclidean](https://en.wikipedia.org/wiki/Euclidean_distance) distance




### [Geopoint columns](#id7)[¶](#geopoint-columns "Permalink to this heading")


* Geospatial distance


In case of other types or when column types don’t match the only join condition available is a strict equality.


For string and numeric columns it’s also possible to set a relative threshold.
In this case a threshold will be in percents and the calculated distance will be divided by the length of a corresponding join key (or its value in case of numbers).


For example if there are two join keys “propre” and “propeller”, the distance is set to Damerau–Levenshtein and a threshold is relative and set to 50%.


* An absolute Damerau–Levenshtein distance between these words is 4\.
* If the distance is calculated relatively to the first dataset, then a relative distance is 4/6 \= 66%, (6 is a length of “propre”) so with a 50% it’s not a match.
* If the distance is calculated relatively to the second dataset, then a relative distance is 4/9 \= 44%, ( is a length of “propeller”) and it’s a match.





[Additional settings](#id8)[¶](#additional-settings "Permalink to this heading")
--------------------------------------------------------------------------------


There are two additional options of the recipe.



### [Output matching details](#id9)[¶](#output-matching-details "Permalink to this heading")


Adds an additional “meta” column that contains a JSON object with details about joined keys that includes:


* distance type
* threshold
* calculated distance
* a result showing if two values matched
* a pair of join values




### [Debug mode](#id10)[¶](#debug-mode "Permalink to this heading")


Activates a cross join and also enabled meta column generation. Useful when trying to understand why certain rows didn’t match.



Warning


Since debug mode forces a cross join the recipe can be slow and can generate very large output. Consider filtering the inputs to only the rows that you’re interested in while debugging.






[Columns in the output](#id11)[¶](#columns-in-the-output "Permalink to this heading")
-------------------------------------------------------------------------------------


Since datasets routinely have columns with identical names, it is possible to disambiguate column names in the “Selected columns” section, either by giving an alias for a given column (using the “pencil” button next to the given column), or by assigning a prefix to apply to all columns of the table (by clicking on the “No prefix” button).




[Engines](#id12)[¶](#engines "Permalink to this heading")
---------------------------------------------------------


Only DSS engine is supported.