Tokenize text[¶](#tokenize-text "Permalink to this heading")
============================================================


This processor tokenizes (splits in words) a text column.



Example use case[¶](#example-use-case "Permalink to this heading")
------------------------------------------------------------------


You want to perform statistics on the words used in a product catalog or
query log. Tokenization allows you to handle words separately.




Output[¶](#output "Permalink to this heading")
----------------------------------------------


The tokenizer offers several output modes:


* Convert to array: An array (JSON\-formatted) containing the words is
generated, either in the input column or in another column. This mode
is most useful if you intend to perform some custom processing and
need to retain the structure of the original text.
* One token per row: in this mode, for each token, a new row is
generated. The row contains a copy of all other columns in the
original row. This mode is most useful if you intend to group by word
afterwards.
* One token per column: in this mode, a new column is generated for
each token. For example, if a column contains 4 words, and you use
‘out\_’ as prefix, columns ‘out\_0’, ‘out\_1’, ‘out\_2’ and ‘out\_3’
will be generated.




Simplification[¶](#simplification "Permalink to this heading")
--------------------------------------------------------------


Very often, you’ll want to simplify the text to remove some variance in
your text corpus. This processor offers several possible simplifications
on the text to tokenize.


* Normalize text: transforms to lowercase, removes accents and performs
Unicode normalization (Café \-\> cafe)
* Clear stop words: remove so\-called ‘stop words’ (the, I, a, of, …).
This transformation is language\-specific and requires you to enter
the language of your column.
* Stem words: transforms each word into its ‘stem’, ie its grammatical
root. For example, ‘grammatical’ is transformed to ‘grammat’. This
transformation is language\-specific and requires you to enter the
language of your column.
* Sort words alphabetically: sorts all words of the text. For example,
‘the small dog’ is transformed to ‘dog small the’. This allows you to
match together strings that are written with the same words in a
different order.