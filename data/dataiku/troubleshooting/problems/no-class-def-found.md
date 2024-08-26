Receiving “java.lang.NoClassDefFoundError”[¶](#receiving-java-lang-noclassdeffounderror "Permalink to this heading")
====================================================================================================================


There are a couple of common situations that can result in seeing a `java.lang.NoClassDefFoundError` or `class not initialized` error message in the UI. Here are some common reasons and resolutions.



Receiving “java.lang.NoClassDefFoundError: org/apache/hadoop/”[¶](#receiving-java-lang-noclassdeffounderror-org-apache-hadoop "Permalink to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------


If you receive an error that has a reference to `org/apache/hadoop`, this usually means that the Hadoop integration has not been run. Some examples of what this type of error looks like are:


* `java.lang.NoClassDefFoundError: org/apache/hadoop/conf/Configuration`
* `java.lang.NoClassDefFoundError: org/apache/hadoop/mapred/JobConf`



### Resolution[¶](#resolution "Permalink to this heading")


If you are receiving an error that falls into this category, you will need to go through the steps listed under [Setting up DSS Hadoop integration](../../hadoop/installation.html#hadoop-integration).


Please note that if you use standalone libraries for Hadoop, the integration must be re\-run after upgrading DSS. This means that if you ran `DATADIR/bin/dssadmin install-hadoop-integration` in the past, but are receiving an error like this, the integration likely needs to be re\-run after upgrading.


If you do not have a Hadoop cluster but are managing Parquet files, you will also need to run the Hadoop integration. In this situation, you can download the `dataiku-dss-hadoop-standalone-libs-generic-hadoop3` binary from your usual Dataiku DSS download site, and then run the standalone hadoop integration:



```
./DATADIR/bin/dssadmin install-hadoop-integration -standalone generic-hadoop3 -standaloneArchive /PATH/TO/dataiku-dss-hadoop3-standalone-libs-generic...tar.gz

```





Receiving java.lang.NoClassDefFoundError for operations that previously did not throw an error[¶](#receiving-java-lang-noclassdeffounderror-for-operations-that-previously-did-not-throw-an-error "Permalink to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


If you are receiving a `java.lang.NoClassDefFoundError` while performing normal actions (i.e. exploring datasets) and do not see any reference to hadoop in the error message, you may have inadvertently upgraded Java while DSS was running.



### Resolution[¶](#id1 "Permalink to this heading")


To prevent this, Java should not be updated while DSS is running. If it was, DSS needs to be restarted in order to resolve this error. As the `dssuser`, restart DSS:



```
./DATADIR/bin/dss restart

```


If you want to point to a specific version of Java, please follow the instructions to [Switching the JVM](../../installation/custom/advanced-java-customization.html#java-custom-jre).