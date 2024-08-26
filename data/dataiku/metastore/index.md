Metastore catalog[¶](#metastore-catalog "Permalink to this heading")
====================================================================


The metastore catalog is a concept that originated from the Hive project. The metastore stores an association between paths (initially on HDFS) and virtual tables.


A “table” in the metastore is made of:


* A location of the files making up the data
* A schema (column names and types)
* A storage format indicating the file format of the data files
* Other various metadata


Originally, a metastore catalog is an external service.


DSS features multiple integration points with the metastore catalog:


* Datasets can be automatically and massively imported from definitions in a metastore catalog.
* HadoopFS, S3, Azure Blob and Google Cloud Storage datasets can have an “associated metastore table”
* When a managed dataset has an associated metastore table, the definition of the table in the metastore can be updated from the dataset settings each time the dataset is built. This allows you to then query the data of the dataset from any of the metastore\-aware engines
* When an external dataset has an associated metastore table, the definition of the dataset can be updated from the metastore. This is useful if the dataset was imported from the metastore


Multiple engines and features in DSS leverage the metastore (rather than the dataset definition) to perform computations:


* Hive recipes and notebooks (see [Hive](../hadoop/hive.html) \- Requires a Hadoop cluster)
* Hive datasets (see [Hive datasets](../hadoop/hive-dataset.html) \- Requires a Hadoop cluster)
* Impala recipes and notebooks (see [Impala](../hadoop/impala.html) \- Requires a Hadoop cluster)
* SparkSQL notebooks
* SparkSQL recipes (if “global metastore” mode is enabled)
* Athena


DSS can leverage three kinds of metastores:


* [Hive metastore (through HiveServer2\)](hive-metastore.html) if you use a Hadoop cluster
* [Glue metastore](glue-metastore.html) if you run on AWS
* [DSS itself as a virtual metastore](dss-metastore.html) for fully managed compute without a Hadoop cluster