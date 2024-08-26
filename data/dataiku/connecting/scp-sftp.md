SCP / SFTP (aka SSH)[¶](#scp-sftp-aka-ssh "Permalink to this heading")
======================================================================



* [Defining the SCP/SFTP connection](#defining-the-scp-sftp-connection)


	+ [SCP/SFTP connection parameters](#scp-sftp-connection-parameters)
* [Creating SCP or SFTP datasets](#creating-scp-or-sftp-datasets)



DSS can interact with remote servers through the use of SSH to:


* Read and write datasets
* Read and write managed folders


DSS can use either the SCP or the SFTP protocol to interact with the remote server.



Note


You can use the DSS [Download recipe](../other_recipes/download.html) to cache the contents from a SCP/SFTP server.


This can provide better performance if you need to read SCP/SFTP files a lot of time,
and don’t mind the copy of the data which is made into a DSS managed folder.


By default, the download recipe will still check the SCP/SFTP server for updates when its
output folder is rebuilt. This behavior can be disabled.




[Defining the SCP/SFTP connection](#id1)[¶](#defining-the-scp-sftp-connection "Permalink to this heading")
----------------------------------------------------------------------------------------------------------


Accessing remote files stored on SCP/SFTP servers first requires the definition of an SCP/SFTP connection to the remote server, as follows:


* Go to Administration \> Connections
* Click the “New connection” button and select “SCP/SFTP”
* Enter a name for the new connection, and the required connection parameters
* Save the new connection



### [SCP/SFTP connection parameters](#id2)[¶](#scp-sftp-connection-parameters "Permalink to this heading")




| Name | Description |
| --- | --- |
| Host | Host name or IP address of the SSH server to access, mandatory. |
| User | SSH username to use, mandatory. |
| Use public key authentication | * Checked to use public key authentication. * Unchecked to use password authentication. |
| Password | SSH password to use. Mandatory if using password authentication. |
| Key passphrase | In public\-key authentication mode, optional passphrase to use to decrypt the SSH private key. |


When using public\-key authentication mode, connection to the remote server will be
attempted using any of the two standard SSH keys for the Studio Linux user, stored
respectively in files `$HOME/.ssh/id_dsa` and `$HOME/.ssh/id_rsa`, where $HOME
is the home directory of the DSS user account. SSH keys generated using the Ed25519
algorithm are not supported and RSA keys must be in the PEM format.





[Creating SCP or SFTP datasets](#id3)[¶](#creating-scp-or-sftp-datasets "Permalink to this heading")
----------------------------------------------------------------------------------------------------


* From the “Datasets” screen of Data Science Studio, click the “New dataset” button and
select the “SCP” or “SFTP”
* Select the connection to use
* Click browse to locate your files