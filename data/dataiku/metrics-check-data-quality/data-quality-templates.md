Data Quality Templates[¶](#data-quality-templates "Permalink to this heading")
==============================================================================


Data Quality templates allow you to easily share and reuse Data Quality rules across datasets.


A template is a set of Data Quality rules, that can easily be applied to a dataset.
Templates are global, allowing you to share standard configurations across your entire instance.



* [Creating a template](#creating-a-template)
* [Reusing a template](#reusing-a-template)
* [Managing templates](#managing-templates)
* [Security](#security)




[Creating a template](#id1)[¶](#creating-a-template "Permalink to this heading")
--------------------------------------------------------------------------------


You can create a template from the Data Quality Rule edition panel of any dataset, using the three\-dot *Actions* menu on the right side of the screen.
This will create a snapshot of the rules from this dataset, available to all other users of the instance.


It is also possible to create a new template from scratch, from the *Templates* tab of the instance Data Quality page.




[Reusing a template](#id2)[¶](#reusing-a-template "Permalink to this heading")
------------------------------------------------------------------------------


From the Data Quality rule edition page, you can use a template using the *Add from template* button.
This will add all rules from the template to the dataset you’re in.
Some rule configurations may be invalid or missing, since the dataset it was created from may differ from the current one. For example, the configuration will be invalid if a rule was created on a column name that doesn’t exist in your current dataset.




[Managing templates](#id3)[¶](#managing-templates "Permalink to this heading")
------------------------------------------------------------------------------


The full list of templates, with their names and descriptions is available from the instance Data Quality page, using the *Templates* tab.
From this page, you can also delete templates or copy their content in order to manually use them in a dataset.


It is also possible to create or edit an existing template from this page.




[Security](#id4)[¶](#security "Permalink to this heading")
----------------------------------------------------------


Templates are publicly usable and manageable.
Any authenticated user may discover, create, update, delete and use any template of the instance.