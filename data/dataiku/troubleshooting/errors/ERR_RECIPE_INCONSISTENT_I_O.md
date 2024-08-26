ERR\_RECIPE\_INCONSISTENT\_I\_O: Inconsistent recipe input or output[¶](#err-recipe-inconsistent-i-o-inconsistent-recipe-input-or-output "Permalink to this heading")
=====================================================================================================================================================================


There is an issue with that recipe’s inputs or outputs.
The specific error message should contain more details on the precise
cause of this error.


Some common examples include:


* The output dataset of a recipe is read\-only
* The output of a recipe is expected to ba a dataset but is not



Remediation[¶](#remediation "Permalink to this heading")
--------------------------------------------------------


Make sure that the recipe settings and inputs are correct. Check these
datasets’ status.


If the recipe’s inputs were recently changed, that is probably a good
place to start looking.