R integration[¶](#r-integration "Permalink to this heading")
============================================================


Due to the large number of additional system dependencies, DSS R integration is not installed by default.


You can install R integration at any time.



* [Prerequisites](#prerequisites)
* [Case 1: Automatic installation, if your DSS server has Internet access](#case-1-automatic-installation-if-your-dss-server-has-internet-access)
* [Case 2: If your DSS server does not have Internet access](#case-2-if-your-dss-server-does-not-have-internet-access)
* [Case 3: Custom installation](#case-3-custom-installation)
* [Troubleshooting](#troubleshooting)


	+ [Rebuilding the R environment](#rebuilding-the-r-environment)
	
	
		- [Rebuilding the default R environment](#rebuilding-the-default-r-environment)
		- [Rebuilding managed R code environments](#rebuilding-managed-r-code-environments)
	+ [macOS](#macos)




[Prerequisites](#id1)[¶](#prerequisites "Permalink to this heading")
--------------------------------------------------------------------


DSS requires R version 3\.6 or R version 4\.



Warning


For R version 3\.6, DSS only supports up to snapshot `2024-06-10`. You can use the CRAN repository `https://packagemanager.posit.co/cran/2024-06-10` to freeze package versions when running the R integration script or in administration settings for code environments.



Only a single version of R can be used.



Note


On some platforms (notably, at the time of writing, SLES 15 systems) the version of R available through the system package manager may not be compatible with DSS.


In that case, automatic installation of R itself by the DSS installer is not possible, and integrating DSS with R requires manually installing a compatible version of R.



On macOS, you must first install R from [http://www.r\-project.org/](http://www.r-project.org/). Note that you might need to also install XQuartz.


On Dataiku Cloud, to install R you only need to activate the R integration in the Extension tab of the Launchpad. For more details see [see the dedicated documentation](https://knowledge.dataiku.com/latest/kb/dku-online/work-with-r.html).




[Case 1: Automatic installation, if your DSS server has Internet access](#id2)[¶](#case-1-automatic-installation-if-your-dss-server-has-internet-access "Permalink to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


This procedure installs the required R packages and configures R integration for DSS. It prompts you to install any missing dependency
as root if needed. Internet access (direct or through a proxy) may be needed to download missing packages.


* Go to the DSS data dir



```
cd DATADIR

```
* Stop DSS



```
./bin/dss stop

```
* Run the installation script



```
./bin/dssadmin install-R-integration

```



Note


The install\-R\-integration script automatically checks for any missing system dependencies. If any is missing, it will give you the command to run to install them with superuser privileges. After the installation of dependencies is complete, you can retry the install\-R\-integration script



* Start DSS



```
./bin/dss start

```



Note


The above procedure downloads missing R packages from a default Internet\-based repository using the HTTPS protocol.
If required, you can switch to another repository ([CRAN mirror](https://cran.r-project.org/mirrors.html))
by specifying option `-repo REPO_URL`, as in:



```
./bin/dssadmin install-R-integration -repo http://cran.univ-paris1.fr

```




Note


If the DSS server has Internet access only through a web proxy, you can configure it using the standard `http_proxy`
and/or `https_proxy` environment variables, as follows:



```
export http_proxy=http://PROXY_HOST:PROXY_PORT
export https_proxy=http://PROXY_HOST:PROXY_PORT
./bin/dssadmin install-R-integration

```





[Case 2: If your DSS server does not have Internet access](#id3)[¶](#case-2-if-your-dss-server-does-not-have-internet-access "Permalink to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------


To help with R package installation when the DSS server does not have Internet access (directly nor through a proxy), the DSS installation kit
includes a standalone script which may be used to download the required set of R package sources on a third\-party Internet\-connected system,
and store them to a directory suitable for offline installation on the DSS server.


* Check for missing system dependencies on the DSS server, including the base R system, the development tools, and libraries required by the
mandatory R packages. If any dependency is missing, you will need to install it from a local package repository for your OS distribution.



```
dataiku-dss-VERSION/scripts/install/install-deps.sh -check -without-java -without-python -with-r

```
* Retrieve the standalone download script `dataiku-dss-VERSION/scripts/install/download-R-packages.sh` and transport it to the system which you will
use for download. This system should run Linux or macOS, should have R installed, and should have Internet connection, directly or through a proxy.
* On this download system, run the download script as follows:



```
./download-R-packages.sh -dir DIR

```


where `DIR` is a temporary directory which will hold the downloaded packages.
* Transport the resulting directory `DIR` to the DSS server.
* On the DSS server, install any missing R packages from this download directory, and finish configuring DSS R integration:



```
DATADIR/bin/dssadmin install-R-integration -pkgDir DIR

```
* Restart DSS



```
DATADIR/bin/dss restart

```



Note


The `download-R-packages.sh` can be run with additional command\-line arguments naming R packages. It will then download these packages
along with their dependencies in addition to the mandatory set of packages required by DSS.


This can be used to install additional R packages to DSS on a server without Internet access, by running `DATADIR/bin/R` and calling
`install.packages(PACKAGE_NAME, repos = "file://PATH_TO_PKGDIR_DIRECTORY")`





[Case 3: Custom installation](#id4)[¶](#case-3-custom-installation "Permalink to this heading")
-----------------------------------------------------------------------------------------------


Installing DSS R integration consists in the following steps, which you can perform in any way suitable to your environment:


* Install R on the DSS server (version 3\.6 or version 4\)


Data Science Studio references it by looking up “R” in the PATH. If needed, you can override this by defining environment variable `DKURBIN` in the local customization file `DATADIR/bin/env-site.sh`.
* Install the following R packages, either in the global R library, or in the user library of the DSS user account:



| Packages | Repository |
| --- | --- |
| httr RJSONIO dplyr curl IRkernel sparklyr ggplot2 gtools tidyr rmarkdown base64enc filelock | CRAN ([https://cran.r\-project.org](https://cran.r-project.org)) |
* Configure DSS R integration, with the option which omits the default dependency check, and restart DSS



```
cd DATADIR
./bin/dssadmin install-R-integration -noDeps
./bin/dss restart

```




[Troubleshooting](#id5)[¶](#troubleshooting "Permalink to this heading")
------------------------------------------------------------------------



### [Rebuilding the R environment](#id6)[¶](#rebuilding-the-r-environment "Permalink to this heading")


In case a system upgrade of the DSS host installed a new version of R (for example: R 3\.4\.x to R 3\.5\.x), DSS\-installed R packages may become
incompatible and stop working properly.


You should then force a full rebuild of all R environments, as follows:



#### [Rebuilding the default R environment](#id7)[¶](#rebuilding-the-default-r-environment "Permalink to this heading")


* Rename the `DATADIR/R.lib` directory into `DATADIR/R.lib.BAK`
* Replay the `dssadmin install-R-integration` command using one of the methods above, to reinstall all required R packages from scratch
* Optionally, check the `DATADIR/R.lib.BAK` directory for additional packages which you would have manually installed, and reinstall those as well
* Restart DSS
* Once R has been checked to work correctly, remove the backup directory.




#### [Rebuilding managed R code environments](#id8)[¶](#rebuilding-managed-r-code-environments "Permalink to this heading")


You should force a full rebuild of all R\-based managed code environments by navigating to the Administration / Code Envs page, opening each R
environment, selecting “Rebuild env” and clicking “UPDATE”.



Warning


If any R packages were manually installed in the default R library (typically, by calling “install.packages()” from a R session run
by the root account), they may need to be reinstalled as well.






### [macOS](#id9)[¶](#macos "Permalink to this heading")


Some R versions (notably the one coming through Homebrew) are configured to use source packages by default rather than binary packages.
If you leave this option, automatic installation may fail as you need the development tools installed, and quite a number of additional
libraries.


If you get a compilation error when installing one of the missing packages while running install\-R\-integration,
you may try to manually install the binary version of this package instead. At the R prompt:



```
options(pkgType="both")
install.packages("PACKAGE_NAME", repos = "http://cloud.r-project.org/")

```


Then run the install\-R\-integration command again.