IBM DB2[¶](#ibm-db2 "Permalink to this heading")
================================================



Warning


**Tier 2 support**: Connection to IBM DB2 is covered by [Tier 2 support](../../troubleshooting/support-tiers.html)




Note


You might want to start with our resources on [data connections](https://knowledge.dataiku.com/latest/data-sourcing/connections/index.html) in the Knowledge Base.



DSS supports the full range of features on DB2:


* Reading and writing datasets
* Executing SQL recipes
* Performing visual recipes in\-database
* Using live engine for charts



Installing the JDBC driver[¶](#installing-the-jdbc-driver "Permalink to this heading")
--------------------------------------------------------------------------------------


The DB2 JDBC driver is available in your DB2 installation and can be provided by your DB2 administrator.


The driver is made of a single JAR file `db2jcc4.jar`


To install:


* Copy this JAR file to the `lib/jdbc` driver of DSS
* Restart DSS




Creating a DB2 connection[¶](#creating-a-db2-connection "Permalink to this heading")
------------------------------------------------------------------------------------


As a beta\-support database, there is not a dedicated “DB2” connection in DSS.


Instead, create a “Other databases (JDBC)” connection, and enter the following information:


* JDBC Driver class: `com.ibm.db2.jcc.DB2Driver`
* JDBC URL: `jdbc:db2://yourHost:yourPort/yourDatabase`
* JDBC properties:
	+ `user`: your username
	+ `password`: your password
* SQL dialect: IBM DB2




Creating DB2 datasets[¶](#creating-db2-datasets "Permalink to this heading")
----------------------------------------------------------------------------


To create a DB2 dataset, you need to create a “Other SQL databases” dataset. You can also Import your tables.