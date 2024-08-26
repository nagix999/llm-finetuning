Hive ORCFile[¶](#hive-orcfile "Permalink to this heading")
==========================================================


The Optimized Row Columnar (ORC) file format provides a highly efficient way to store Hive data.
It was added in Hive 0\.11 to overcome limitations of the other Hive file formats.


For more information, see [the official ORCFile documentation](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+ORC).



Compatibility[¶](#compatibility "Permalink to this heading")
------------------------------------------------------------


Data Science Studio can read \& write ORCFiles. Most Hive data types are supported, including complex types (object, map \& array).


The following Hive types are not supported:


* DATE
* UNION




Limitations[¶](#limitations "Permalink to this heading")
--------------------------------------------------------


* The ORCFile format can only be used on Hadoop filesystems. If the data is on S3 or Azure Blob Storage, then access needs to be setup through Hadoop with [HDFS connections](../../hadoop/hadoop-fs-connections.html)
* Impala doesn’t support ORCFile. Consequently, you won’t be able to use the “Live processing” chart engine on ORCFile datasets.