Installing a Govern node[¶](#installing-a-govern-node "Permalink to this heading")
==================================================================================



* [Database requirements](#database-requirements)
* [Installation](#installation)
* [Post\-installation steps](#post-installation-steps)



You need to manually install a Govern node if you plan to use Dataiku governance capabilities. See [Governance](../../governance/index.html) for more information.


The process of installing a Govern instance is very similar to a regular DSS installation, except for the database requirement below. [Requirements](requirements.html) and [Installing a new DSS instance](initial-install.html) thus remain mostly valid.



[Database requirements](#id1)[¶](#database-requirements "Permalink to this heading")
------------------------------------------------------------------------------------


Govern is based on a Postgresql 12\+ database for the storage of data.
A dedicated database and user need to be created on the Postgresql instance for Govern:



```
CREATE USER <govern_user> WITH ENCRYPTED PASSWORD '<govern_pwd>';
CREATE DATABASE <govern_db> OWNER <govern_user>;

```


Where `<govern_user>`, `<govern_pwd>` and `<govern_db>` are the values of your choice.




[Installation](#id2)[¶](#installation "Permalink to this heading")
------------------------------------------------------------------


Unpack the kit, just like for a design node.


Then from the user account which will be used to run Dataiku Govern, enter the following command:



```
dataiku-dss-VERSION/installer.sh -t govern -d DATA_DIR -p PORT -l LICENSE_FILE

```


Where:


* `DATA_DIR` is the location of the data directory that you want to use. If the directory already exists, it must be empty.
* `PORT` is the base TCP port to be used for Govern.
* `LICENSE_FILE` is the path to your DSS license file.


In short, all installation steps are the same as for a design node, you simply need to add `-t govern` to the `installer.sh` command\-line.


Dependencies handling, enabling startup at boot time, and starting the govern node, work exactly as for the design node.




[Post\-installation steps](#id3)[¶](#post-installation-steps "Permalink to this heading")
-----------------------------------------------------------------------------------------


Before starting Govern, the Postgresql database connection needs to be setup in the settings.
Edit `DATA_DIR/config/dip.properties` and add the connection setting there:



```
psql.jdbc.url=jdbc:postgresql://<psql_host>:<psql_port>/<govern_db>?currentSchema=<govern_schema>
psql.jdbc.user=<govern_user>
psql.jdbc.password=<govern_pwd>

```


Where `<govern_user>`, `<govern_pwd>` and `<govern_db>` should be replaced with the value used previously to create the user and database for Govern.
In case there’s a specific schema to be used for govern, it can be specified with `?currentSchema=<govern_schema>`. This is optional, and this part may be removed from the URL if default schema configured in the database is to be used.
`<psql_host>` and `<psql_port>` should point to a running PostgreSQL server.


Finally, for bootstrapping the initial configuration of govern, issue the following command (only first time after kit installation):



```
DATA_DIR/bin/govern-admin init-db

```


Govern can then be started with the standard command:



```
DATA_DIR/bin/dss start

```