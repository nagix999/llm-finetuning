Hadoop filesystems connections (HDFS, S3, EMRFS, WASB, ADLS, GS)[¶](#hadoop-filesystems-connections-hdfs-s3-emrfs-wasb-adls-gs "Permalink to this heading")
===========================================================================================================================================================



* [HDFS connections in DSS](#hdfs-connections-in-dss)


	+ [Managed datasets setup](#managed-datasets-setup)
* [Connecting to the “default” FS](#connecting-to-the-default-fs)
* [Connecting to the HDFS of other clusters](#connecting-to-the-hdfs-of-other-clusters)
* [Connecting to S3](#connecting-to-s3)


	+ [Using S3A](#using-s3a)
	+ [Using EMRFS](#using-emrfs)
	+ [Using VPC Endpoints](#using-vpc-endpoints)
* [Connecting to Azure Blob Storage](#connecting-to-azure-blob-storage)
* [Connecting to Google Cloud Storage](#connecting-to-google-cloud-storage)
* [Connecting to Azure Data Lake Store (gen1\)](#connecting-to-azure-data-lake-store-gen1)
* [Connecting to Azure Data Lake Store (gen2\)](#connecting-to-azure-data-lake-store-gen2)
* [Additional details](#additional-details)


	+ [Cloud storage credentials](#cloud-storage-credentials)
	+ [Checking access to a Hadoop filesystem](#checking-access-to-a-hadoop-filesystem)
	+ [Relation to the Hive metastore](#relation-to-the-hive-metastore)



DSS can connect to multiple “Hadoop Filesystems”. A Hadoop filesystem is defined by a URL. Implementations of Hadoop filesystems exist that provide connectivity to:


* HDFS
* Amazon S3
* Azure Data Lake Storage
* Azure Blob Storage
* Google Cloud Storage
* …


The “main” Hadoop filesystem is traditionally a HDFS running on the cluster, but through Hadoop filesystems, you can also access to HDFS filesystems on other clusters, or even to different filesystem types like cloud storage.


The prime benefit of framing other filesystems as Hadoop filesystems is that it enables the use of the Hadoop I/O layers, and as a corollary, of important Hadoop file formats: Parquet and ORC.


To access data on a filesystem using Hadoop, 3 things are needed:


* libraries to handle the filesystem have to be installed on the cluster and on the node hosting DSS. Hadoop distributions normally come with at least HDFS and S3A
* a fully\-qualified URI to the file, of the form `scheme://host[:port]/path-to-file` . Depending on the scheme, the `host[port]` part can have different meanings; for example, for cloud storage filesystems, it is the bucket.
* Hadoop configuration parameters that get passed to the relevant tools (Spark, Hive, MapReduce, HDFS libraries) \- This is generally used to pass credentials and tuning options



[HDFS connections in DSS](#id1)[¶](#hdfs-connections-in-dss "Permalink to this heading")
----------------------------------------------------------------------------------------



Warning


In DSS, all Hadoop filesystem connections are called “HDFS”. This wording is not very precise since there can
be “Hadoop filesystem” connections that precisely do not use “HDFS” which in theory only refers to the distributed implementation using NameNode/DataNode.



To setup a new Hadoop filesystem connection, go to Administration → Connections → New connection → HDFS.


A HDFS connection in DSS consists of :


* a root path, under which all the data accessible through that connection resides. The root path can be fully\-qualified, starting with a `scheme://`, or starting with `/` and relative to what is defined in *fs.defaultFS*
* Hadoop configuration parameters that get passed to the relevant tools (Spark, Hive, MapReduce, HDFS libraries)



### [Managed datasets setup](#id2)[¶](#managed-datasets-setup "Permalink to this heading")


We suggest to have at least two connections:


* A read\-only connection to all data:



> + `root: /`           *(This is a path on HDFS, the Hadoop file system.)*
> 	+ Allow write, allow managed datasets: unchecked
> 	+ max nb of activities: 0
> 	+ name: hdfs\_root
* A read\-write connection, to allow DSS to create and store managed datasets:



> + root: /user/dataiku/dss\_managed\_datasets
> 	+ allow write, allow managed datasets: checked
> 	+ name: hdfs\_managed


When “Hive database name” is configured, DSS declares its HDFS datasets in the Hive metastore, in this database namespace.
This allows you to refer to DSS datasets in external Hive programs, or in Hive notebooks within DSS.





[Connecting to the “default” FS](#id3)[¶](#connecting-to-the-default-fs "Permalink to this heading")
----------------------------------------------------------------------------------------------------


All Hadoop clusters define a ‘default’ filesystem, which is traditionally a HDFS on the cluster.


When missing, the `scheme://host[:port]` is taken from the `fs.defaultFS` Hadoop property in `core-site.xml`, so that a URI like ‘/user/john/data/file’ is generally interpreted as a path on the local HDFS filesystem of the cluster. However, if the `fs.defaultFS` of your cluster points to S3, an unqualified URI will similarly point to S3\.




[Connecting to the HDFS of other clusters](#id4)[¶](#connecting-to-the-hdfs-of-other-clusters "Permalink to this heading")
--------------------------------------------------------------------------------------------------------------------------


A HDFS located on a different cluster can be accessed with a HDFS connection that specified the host (and port) of the namenode of that other filesystem, like `hdfs://namenode_host:8020/user/johndoe/` . DSS will access the files on all HDFS filesystems with the same user name (even if [User Isolation Framework](../user-isolation/index.html) is being used for HDFS access).



Warning


When the local cluster is using Kerberos, it is possible to access a non\-kerberized cluster, but a HDFS configuration property is needed : `ipc.client.fallback-to-simple-auth-allowed=true`





[Connecting to S3](#id5)[¶](#connecting-to-s3 "Permalink to this heading")
--------------------------------------------------------------------------


There are several options to access S3 as a Hadoop filesystem (see the [Apache doc](https://cwiki.apache.org/confluence/display/HADOOP2/AmazonS3)).



Note


The S3 dataset in DSS has native support for using Hadoop software layers whenever needed, including for fast read/write from Spark and Parquet support. Using a Hadoop dataset for accessing S3 is not usually required.




Warning


* Using S3 as a Hadoop filesystem is not supported on [MapR](distributions/mapr.html)




### [Using S3A](#id6)[¶](#using-s3a "Permalink to this heading")


“S3A” is the primary mean of connecting to S3 as a Hadoop filesystem.



Warning


S3A is not supported when running on [EMR](distributions/emr.html)


S3A support has not been validated on [MapR](distributions/mapr.html)



Access using the S3A filesystem involves using a URI like `s3a://bucket_name/path/inside/bucket/` , and ensuring the credentials are available. The credentials consist of the access key and the secret key. They can be passed :


* either globally, using the `fs.s3a.access.key` and `fs.s3a.secret.key` Hadoop property
* or for the bucket only, using the `fs.s3a.bucket_name.access.key` and `fs.s3a.bucket_name.secret.key` Hadoop property




### [Using EMRFS](#id7)[¶](#using-emrfs "Permalink to this heading")


EMRFS is an alternative mean of connecting to S3 as a Hadoop filesystem, which is only available on [EMR](distributions/emr.html)


Access using the EMRFS filesystem involves using a URI like `s3://bucket_name/path/inside/bucket/` , and ensuring the credentials are available. The configuration keys for the access and secret keys are named `fs.s3.awsAccessKeyId` and `fs.s3.awsSecretAccessKey`. Note that this is only possible from an EMR\-aware machine.




### [Using VPC Endpoints](#id8)[¶](#using-vpc-endpoints "Permalink to this heading")


When accessing S3 buckets through a VPC Endpoint (of the form `http[s]://bucket.vpce-__identifier__.s3.__region__.vpce.amazonaws.com`), an additional config file is required.


You will have to download and edit [awssdk\_config\_default.json](https://github.com/aws/aws-sdk-java/blob/master/aws-java-sdk-core/src/main/resources/com/amazonaws/internal/config/awssdk_config_default.json#L145), and add the following in the `hostRegexToRegionMappings` section :



```
{
    "hostNameRegex" : "https://bucket\\.vpce\\-.+\\.s3\\.us\\-west\\-1\\.vpce\\.amazonaws\\.com",
    "regionName"    : "us-west-1"
}

```


(replacing `us\\-west\\-1` by the region of your bucket as needed).


This file is to be repacked in a jar and moved to your lib/java folder:



```
mkdir -p com/amazonaws/internal/config/
mv awssdk_config_default.json com/amazonaws/internal/config/
jar -cf awssdk_config.jar com
mv awssdk_config.jar DATA_DIR/lib/java

```





[Connecting to Azure Blob Storage](#id9)[¶](#connecting-to-azure-blob-storage "Permalink to this heading")
----------------------------------------------------------------------------------------------------------



Note


The Azure Blob dataset in DSS has native support for using Hadoop software layers whenever needed, including for fast read/write from Spark and Parquet support. Using a Hadoop dataset for accessing Azure Blob Storage is not usually required.



The URI to access blobs on Azure is `wasb://container_name@your_account.blob.core.windows.net/path/inside/container/` (see the [Hadoop Azure support](http://hadoop.apache.org/docs/r2.7.1/hadoop-azure/index.html)).


The credentials being already partly in the URI (the account name), the only property needed to allow access is `fs.azure.account.key.your_account.blob.core.windows.net` to pass the access key.




[Connecting to Google Cloud Storage](#id10)[¶](#connecting-to-google-cloud-storage "Permalink to this heading")
---------------------------------------------------------------------------------------------------------------



Note


The Google Cloud Storage dataset in DSS has native support for using Hadoop software layers whenever needed, including for fast read/write from Spark and Parquet support. Using a Hadoop dataset for accessing Google Cloud Storage is not usually required.



The URI to access blobs on Google Cloud Storage is `gs://bucket_name/path/inside/bucket/` (see the [GCS connect](https://cloud.google.com/dataproc/docs/connectors/cloud-storage))




[Connecting to Azure Data Lake Store (gen1\)](#id11)[¶](#connecting-to-azure-data-lake-store-gen1 "Permalink to this heading")
------------------------------------------------------------------------------------------------------------------------------


Access to ADLS gen 1 is possible with Oauth tokens provided by Azure


* Make sure that your service principal is owner of the ADLS account and has read/write/execute access to the ADLS gen 1 root container recursively
* Retrieve your App Id, Token endpoint and Secret for the registered application in Azure portal


The URI to access ADLS is `adl://<datalake_storage_name>.azuredatalakestore.net/<optional_path>` (see the [Hadoop ADLS support](https://hadoop.apache.org/docs/current/hadoop-azure-datalake/index.html)).


Add the following key values as Extra Hadoop Conf of the connection:


* `fs.adl.oauth2.access.token.provider.type` \-\> `ClientCredential`
* `fs.adl.oauth2.refresh.url` \-\> `<your_token_endpoint>`
* `fs.adl.oauth2.client.id` \-\> `<your_app_id>`
* `fs.adl.oauth2.credential` \-\> `<your_app_secret_key`




[Connecting to Azure Data Lake Store (gen2\)](#id12)[¶](#connecting-to-azure-data-lake-store-gen2 "Permalink to this heading")
------------------------------------------------------------------------------------------------------------------------------



Note


The Azure Blob Storage dataset in DSS has native support ADLS gen2 and for using Hadoop software layers whenever needed, including for fast read/write from Spark and Parquet support. Using a Hadoop dataset for accessing ADLS gen2 is not usually required.





[Additional details](#id13)[¶](#additional-details "Permalink to this heading")
-------------------------------------------------------------------------------



### [Cloud storage credentials](#id14)[¶](#cloud-storage-credentials "Permalink to this heading")


Cloud storage filesystems require credentials to give access to the data they hold. Most of them allow these credentials to be passed by environment variable or by Hadoop configuration key (the preferred way). The mechanisms to make the credentials available to DSS are:


* adding them as configuration properties for the entire cluster (ie. in `core-site.xml`)
* adding them as environment variables in DSS’s `$DATADIR/bin/env-site.sh` (when it’s possible to pass them as environment variables), and DSS and any of its subprocess can access them
* adding them as extra configuration keys on DSS’s HDFS connections, and then only usages of the HDFS connection will receive the credentials



Warning


Proper usage of cloud storage filesystems implies that the credentials are passed to the processes needing them. In particular, the Hive metastore and Sentry will need to be given the credentials in their configurations.





### [Checking access to a Hadoop filesystem](#id15)[¶](#checking-access-to-a-hadoop-filesystem "Permalink to this heading")


Since DSS uses the standard Hadoop libraries, before attempting to access files on different filesystems, command\-line access to these filesystems should be checked. The simplest test is to run:



```
> hadoop fs -ls uri_to_file

```


If Kerberos authentication is active, logging in with `kinit` first is required. If credentials need to be passed as Hadoop configuration properties, they can be added using the `-D` flag, like



```
> hadoop fs -D fs.s3a.access.key=ABABABABA -D fs.s3a.secret.key=ABCDABCDABCDCDA -ls uri_to_file

```


To check that Hive is functional and gets the credentials it needs, creating a dummy table will uncover potential problems :



```
> beeline -u 'jdbc:hive2://localhost:10000/default'
beeline> CREATE EXTERNAL TABLE dummy (a string) STORED AS PARQUET LOCATION 'fully_qualified_uri_to_some_folder'

```




### [Relation to the Hive metastore](#id16)[¶](#relation-to-the-hive-metastore "Permalink to this heading")


Hadoop clusters most often have Hive installed, and with Hive comes a Hive Metastore to hold the definitions and locations of the tables Hive can access. The location of a Hive table does not need to be on the local cluster, but can be any location provided it’s defined as a fully\-qualified URI. But a given Hive installation, and in particular a given Hiveserver2, only knows one Hive Metastore. If Hive tables are defined in a different Hive Metastore, on a different cluster, Hive doesn’t access them.