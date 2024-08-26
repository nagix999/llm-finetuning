SparkSQL recipes[¶](#sparksql-recipes "Permalink to this heading")
==================================================================


DSS lets you write recipes using SparkSQL. You simply need to write a SparkSQL query, which will be used to populate an output dataset.


As with all Spark integrations in DSS, SparkSQL recipes can read and write datasets,
whatever their storage backends.



* [Creating a SparkSQL recipe](#creating-a-sparksql-recipe)
* [Using the global metastore](#using-the-global-metastore)




[Creating a SparkSQL recipe](#id1)[¶](#creating-a-sparksql-recipe "Permalink to this heading")
----------------------------------------------------------------------------------------------


* First make sure that [Spark is enabled](../spark/installation.html)
* Create a SparkSQL recipe by clicking the corresponding icon
* Add the input Datasets that will be used as source data in your recipes.
* Select or create the output dataset
* Click Create recipe.
* You can now write your SparkSQL code



Note


If the SparkSQL icon is not enabled (greyed out), it can be because:


* Spark is not installed. See [Setting up Spark integration](../spark/installation.html) for more information
* You don’t have [write access](../security/permissions.html) on the project



A SparkSQL recipe is simply a SELECT query based on the input datasets. Each input dataset is available as a SparkSQL table with the same name as the dataset (no database).


When you Validate your SparkSQL recipe, DSS verifies the syntax and computes the output schema of the output dataset. You get a prompt to update the schema.



Note


The first time you validate a SparkSQL recipe after DSS startup, validation can take up to one minute. Subsequent validations are faster.





[Using the global metastore](#id2)[¶](#using-the-global-metastore "Permalink to this heading")
----------------------------------------------------------------------------------------------


Alternatively to the default mode, where each input dataset is exposed as a table with the same name in the default database, you can choose to use the global Hive metastore as source of definitions for your tables.


Using the global metastore can be configured in the Advanced tab of the recipe.


In global metastore mode, your SparkSQL recipe does not need to declare its input datasets. It can actually run with no input dataset.


In global metastore mode, validation is disabled: it is not possible to validate your code anymore. The schema of your output dataset cannot be inferred prior to running, and cannot be propagated across the Flow without running the recipe. However, output schema will still be automatically inferred after running the recipe. This behavior can be disabled in the Advanced tab.