ERR\_TRANSACTION\_GIT\_COMMMIT\_FAILED: Failed committing changes[¶](#err-transaction-git-commmit-failed-failed-committing-changes "Permalink to this heading")
===============================================================================================================================================================


An internal error occurred while trying to save changes performed by a user (saving a recipe, a dataset, a notebook, …)



Remediation[¶](#remediation "Permalink to this heading")
--------------------------------------------------------


A common issue is when the exception contains “Cannot lock /path/to/DSS/……/.git/index”. This error usually means that
an offending “index.lock” has remained in the mentioned folder, possibly after another error:


* Stop DSS, and make sure no processes are still running
* Make sure that no “git” process is running in the mentioned folder
* Remove the “index.lock” file
* Restart DSS


If you are not in this case, the backend log file may contain additional information. Else, please report the issue to Dataiku support.