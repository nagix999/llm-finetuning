Plugins’ code environments[¶](#plugins-code-environments "Permalink to this heading")
=====================================================================================


Since plugins package Python or R code, they sometimes need to impose requirements on the installed packages so that they can run on an instance of DSS.



Defining requirements of a plugin[¶](#defining-requirements-of-a-plugin "Permalink to this heading")
----------------------------------------------------------------------------------------------------


Making the plugin package a code environment definition is one of the 2 modes available to plugins writers, and the preferred one. See [Other topics](../plugins/reference/other.html)




Creating code environment instances for plugins[¶](#creating-code-environment-instances-for-plugins "Permalink to this heading")
--------------------------------------------------------------------------------------------------------------------------------


After installing a plugin that contains a code environment definition, the user is prompted to create a code environment for the plugin. To create the code environment for a plugin after the plugin’s installation:


* go to Administration \> Plugins
* open the plugin or expand its requirements notice in the list
* use Create or Create a new one to create a new code environment with the definition in the plugin
* or select among the existing code environments for that plugin
* Be sure to click the ‘Create’ button in lower left of the plugin home page


![../_images/plugin_create_env.png](../_images/plugin_create_env.png)


Plugin code environment types[¶](#plugin-code-environment-types "Permalink to this heading")
--------------------------------------------------------------------------------------------


Code environments for plugins are only of 2 types:


* managed code environments are created by DSS according to the definition in the plugin
* non\-managed code environments are empty code environments where the user has to run the installation commands manually