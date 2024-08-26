Column Pseudonymization[¶](#column-pseudonymization "Permalink to this heading")
================================================================================


This processor implements pseudonymization by replacing values of columns (containing sensitive data) with hashes. The processor works on any data type by hashing the string representation of the data.



What is pseudonymization ?[¶](#what-is-pseudonymization "Permalink to this heading")
------------------------------------------------------------------------------------


Pseudonymization is a process of replacing a unique attribute in your data by a pseudonym or alias. This reduces the likelihood that the data will be linked to the original identity of the data subject. Pseudonymization is a means of ensuring data privacy but differs from anonymization because the latter irreversibly destroys any way of identifying the data subject.




Input[¶](#input "Permalink to this heading")
--------------------------------------------


* Column selection:



> + A single column
> 	+ A list of multiple columns
> 	+ All columns matching a given pattern
> 	+ All columns
* A hashing algorithm:



> + SHA\-256
> 	+ SHA\-512
> 	+ MD5
* (Optional) A static **pepper** value \- To protect against dictionary attacks, the *pepper* value is added to all input values before hashing. If you intend to use the hash as join or lookup keys, then the *pepper* should be the same for all pseudonymized datasets.
* (Optional) A **salt** column \- To protect against dictionary attacks, the value in each row of this column will be added to the corresponding row of the input values before hashing. If you intend to use the hash as join or lookup keys, then the *salt* column should be present and identical for all pseudonymized datasets.




Output[¶](#output "Permalink to this heading")
----------------------------------------------


The values in each processed column are replaced with the pseudonymized values.
For a cell, the preparation processor calculates a hash of the concatenation of the cell value, the *pepper* value, and the *salt* value. For the i\-th row of a pseudonymized column the output is:



\\\[HASH(row\_i \+ pepper \+ salt\_i)\\]


Pseudonymization Steps[¶](#pseudonymization-steps "Permalink to this heading")
------------------------------------------------------------------------------


Using the Visual analysis tool of the Lab, in the Script tab:


* Add a new step of type **Pseudonymize text**
* Select an option for *Column*, and type the column name(s) or pattern, as applicable
* Select a value for *Hashing algorithm*
* Specify a column for *Salt* (optional)
* Specify a value for *Pepper* (optional)




Spark Execution[¶](#spark-execution "Permalink to this heading")
----------------------------------------------------------------


When Spark is installed, this preparation processor can run on Spark.




In\-Database Execution[¶](#in-database-execution "Permalink to this heading")
-----------------------------------------------------------------------------


This processor can be run using SQL Engine. But some databases have a limited support for hashing functions. Here are the details of this support:




| Databases | MD5 | SHA256 | SHA512 |
| --- | --- | --- | --- |
| MySQL | Y | Y | Y |
| PostgreSQL | Y | N | N |
| SQLServer | Y | Y | Y |
| Vertica | Y | Y | Y |
| Oracle | \>\=12c | \>\=12c | \>\=12c |
| Redshift | Y | N | N |
| GreenPlum | Y | N | N |
| BigQuery | Y | Y | Y |
| Hive | \>\=1\.3 | N | N |
| Impala | N | N | N |
| DB2 | Y | Y | Y |
| Snowflake | Y | Y | Y |
| Teradata | N | N | N |