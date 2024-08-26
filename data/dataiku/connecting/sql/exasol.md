Exasol[¶](#exasol "Permalink to this heading")
==============================================



Warning


**Tier 2 support**: Connection to Exasol is covered by [Tier 2 support](../../troubleshooting/support-tiers.html)




Note


You might want to start with our resources on [data connections](https://knowledge.dataiku.com/latest/data-sourcing/connections/index.html) in the Knowledge Base.



DSS supports the full range of features on Exasol:


* Reading and writing datasets
* Executing SQL recipes
* Performing visual recipes in\-database
* Using live engine for charts



Limitations[¶](#limitations "Permalink to this heading")
--------------------------------------------------------


* Parallel writes to the same table are not supported by Exasol, which means that:


	+ You cannot use redispatch partitioning to Exasol
	+ Partitioned recipes writing to Exasol must be limited to a single concurrent activity