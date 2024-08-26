Parquet[¶](#parquet "Permalink to this heading")
================================================


Parquet is an efficient file format of the Hadoop ecosystem. Its main points are:


* Column\-oriented, even for nested complex types
* Block\-based compression
* Ability to “push down” filtering predicates to avoid useless reads


Using Parquet or another efficient file format is strongly recommended when working with Hadoop data (rather than CSV data). Speedups can reach up to x100 on select queries.



Requirements[¶](#requirements "Permalink to this heading")
----------------------------------------------------------


Using Parquet format requires [Setting up DSS Hadoop integration](../../hadoop/installation.html#hadoop-integration). If you don’t have a Hadoop cluster, you must run the [Standalone Hadoop integration](../../hadoop/installation.html#hadoop-installation-standalone) in order to use Parquet format.




Applicability[¶](#applicability "Permalink to this heading")
------------------------------------------------------------


* Parquet datasets can be stored on the following cloud storage and hadoop connections: HDFS, S3, GCS, Azure Blob storage. For more details see [Hadoop filesystems connections (HDFS, S3, EMRFS, WASB, ADLS, GS)](../../hadoop/hadoop-fs-connections.html).
* Parquet datasets can be used as inputs and outputs of all recipes
* Parquet datasets can be used in the Hive and Impala notebooks




Limitations and issues[¶](#limitations-and-issues "Permalink to this heading")
------------------------------------------------------------------------------



### Case\-sensitivity[¶](#case-sensitivity "Permalink to this heading")


Due to differences in how Hive and Parquet treat identifiers, it is strongly recommended that you only use **lowercase identifiers** when dealing with Parquet files.




### Related to Hive[¶](#related-to-hive "Permalink to this heading")


* “Array” columns containing NULL values are corrupted when read or written by Hive. See [https://issues.apache.org/jira/browse/HIVE\-6994](https://issues.apache.org/jira/browse/HIVE-6994)
* NULL values in “Object” columns wrongly get converted to empty objects. See [https://issues.apache.org/jira/browse/HIVE\-8419](https://issues.apache.org/jira/browse/HIVE-8419)
* “Map” columns containing NULL values are corrupted when read or written by Hive. See [https://issues.apache.org/jira/browse/HIVE\-8359](https://issues.apache.org/jira/browse/HIVE-8359)
* DECIMAL(…) columns in Hive tables are stored as fixed\-length byte arrays, which DSS doesn’t parse.
* CHAR(…) and VARCHAR(…) columns in Hive tables are stored as utf\-8 strings. DSS doesn’t apply the padding (on CHAR(…) columns) nor the trimming (on VARCHAR(…) columns).




### Related to Impala[¶](#related-to-impala "Permalink to this heading")


* Impala needs to load in memory each Parquet block. You might need to increase the max memory allocated to the impala queries in the Impala configuration screens.




### Misc[¶](#misc "Permalink to this heading")


* While reading Parquet files, DSS uses the schema from the dataset settings and not the integrated schema in the files. To use the schema from the Parquet files, set `spark.dku.allow.native.parquet.reader.infer` to `true` in the Spark settings.
* on recent EMR clusters, the `EmrOptimizedSparkSqlParquetOutputCommitter` conflicts with the `fs.s3.impl.disable.cache=true` that DSS sets, which causes failures to create the staging directory. Disabling the optimized EMRFS committer or adding a property `dku.no.disable.hdfs.cache -> true` to the S3 connection in DSS is then needed.