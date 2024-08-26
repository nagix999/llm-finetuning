GCP “Sandbox” marketplace image[¶](#gcp-sandbox-marketplace-image "Permalink to this heading")
==============================================================================================


Dataiku provides a pre\-built image for running DSS on GCP



Note


Of course, you can use the regular Linux installation procedure ([Installing a new DSS instance](../custom/initial-install.html)) on any compatible GCP Linux instance.


The image provides a shorter path to having a working standalone DSS instance
with default options.




Warning


This image is provided as a way to quick start a DSS instance, mainly for testing purposes.
It comes with several “pre\-made” choices (accounts, disks, installation directories, …) and installed packages and may not be suitable for all purposes.


For production purposes, we strongly recommend using [Dataiku Cloud Stacks for GCP](../cloudstacks-gcp/index.html) instead


This image does not come with any specific upgrade features. Use the regular DSS upgrade mechanisms.


This image is generally not suitable for use as edge node of an existing Hadoop cluster. See [DSS and Hadoop](../../hadoop/index.html) for more information. For these cases, we recommend you install a new instance of DSS on a manually installed Linux Azure instance.




* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [How to](#how-to)


	+ [How do I use DSS?](#how-do-i-use-dss)
	+ [How do I log into the virtual machine instance?](#how-do-i-log-into-the-virtual-machine-instance)
	+ [Where is the DSS data directory?](#where-is-the-dss-data-directory)
	+ [What is installed by default?](#what-is-installed-by-default)
	+ [How do I install JDBC drivers?](#how-do-i-install-jdbc-drivers)




[Prerequisites](#id1)[¶](#prerequisites "Permalink to this heading")
--------------------------------------------------------------------


You need a Google Cloud account and a Cloud project to proceed. You will be billed only for the virtual machine instance; the image itself is free.




[Installation](#id2)[¶](#installation "Permalink to this heading")
------------------------------------------------------------------


See [https://www.dataiku.com/product/get\-started/google/](https://www.dataiku.com/product/get-started/google/)




[How to](#id3)[¶](#how-to "Permalink to this heading")
------------------------------------------------------



### [How do I use DSS?](#id4)[¶](#how-do-i-use-dss "Permalink to this heading")


DSS is available:


* As regular HTTP, on the port 80 of the instance.
* As HTTPS, on the port 443 of the instance \- DSS is preloaded with a self\-signed certificate, so you will get a security error. You can replace this with a real certificate afterwards.


When first accessing the DSS UI:


* You will be required to provide the login and password printed in the Solution deployment UI.
* You will be prompted to register for the DSS free edition, or enter your DSS enterprise license.




### [How do I log into the virtual machine instance?](#id5)[¶](#how-do-i-log-into-the-virtual-machine-instance "Permalink to this heading")


Administrative (command\-line) access can be obtained by logging in through SSH using the credentials configured in your compute engine metadata configuration .


Beware: DSS run under the `dataiku` account.
The administrative account is sudoer, so from its shell, you can use `sudo su dataiku` to get a shell as the `dataiku` user.


Out of the box, you cannot login as the `dataiku` user, and the `dataiku` user is not sudoer (you can add your SSH key to the authorized keys of dataiku, though) unless you configure your public key in the in your Compute engine Metadata to be deployed in DSS.




### [Where is the DSS data directory?](#id6)[¶](#where-is-the-dss-data-directory "Permalink to this heading")


The DSS data directory on the Compute Engine instance is `/home/dataiku/dss`. All operations on this data directory (like installing JDBC drivers, …) must be performed as the `dataiku` user (see above).




### [What is installed by default?](#id7)[¶](#what-is-installed-by-default "Permalink to this heading")


The Dataiku image is based on on CentOS 7\. It contains:


* A standard installation of Dataiku DSS running under Linux user account “dataiku”.
* A local PostgreSQL database, with a connection to it pre\-configured in DSS.
* A standard installation of R, also pre\-configured in DSS.
* A nginx reverse proxy exposing DSS onto the standard HTTP port 80, and the standard HTTPS port 443 using a self\-signed certificate. For better security, you can provide your own certificate in directory /etc/nginx/ssl.




### [How do I install JDBC drivers?](#id8)[¶](#how-do-i-install-jdbc-drivers "Permalink to this heading")


JDBC drivers must be installed by copying the relevant files in the “lib/jdbc” folder of the DSS data directory (See [Installing database drivers](../custom/jdbc.html)).


You can either download files from the instance or upload them using SSH. Copy into the `/home/dataiku/dss/lib/jdbc` folder must be done as the `dataiku` user (see above).