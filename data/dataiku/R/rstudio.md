RStudio integration[¶](#rstudio-integration "Permalink to this heading")
========================================================================


In addition to the ability to [use the DSS R API outside of DSS](../R-api/outside-usage.html), DSS features several integration points with RStudio.



* [RStudio Server in a Code Studio](#rstudio-server-in-a-code-studio)
* [RStudio Desktop](#rstudio-desktop)
* [RStudio Server (running on a separate server)](#rstudio-server-running-on-a-separate-server)


	+ [Embedding the RStudio Server UI in DSS](#embedding-the-rstudio-server-ui-in-dss)
* [RStudio Server (running on the DSS server)](#rstudio-server-running-on-the-dss-server)


	+ [Installing the R package](#installing-the-r-package)
	+ [Setup connectivity](#setup-connectivity)
	+ [Create RStudio project](#create-rstudio-project)




[RStudio Server in a Code Studio](#id1)[¶](#rstudio-server-in-a-code-studio "Permalink to this heading")
--------------------------------------------------------------------------------------------------------


Code Studios allow you to run and expose a RStudio server in Dataiku to interactively edit and debug R recipes, libraries…


Learn more about [Code Studios](../code-studios/index.html) and how to [launch a RStudio Server](../code-studios/code-studio-ides/rstudio.html).


![../_images/rstudio-in-code-studio.png](../_images/rstudio-in-code-studio.png)


[RStudio Desktop](#id2)[¶](#rstudio-desktop "Permalink to this heading")
------------------------------------------------------------------------



Note


See this [Knowledge Base how\-to](https://knowledge.dataiku.com/latest/code/work-environment/how-to-rstudio.html) for setting up and using the RStudio Desktop integration.



As soon as you install the `dataiku` package in your RStudio Desktop (as documented in [Using the R API outside of DSS](../R-api/outside-usage.html)), new RStudio extensions become available in the “Addins” menu:


![../_images/rstudio-addins-menu.png](../_images/rstudio-addins-menu.png)
These extensions allow you to:


* Setup connection to a DSS instance (URL and API key)
* Download the code of a R recipe in order to edit it locally in RStudio
* Once you’re done editing the recipe, uploading it back to DSS for saving and execution.




[RStudio Server (running on a separate server)](#id3)[¶](#rstudio-server-running-on-a-separate-server "Permalink to this heading")
----------------------------------------------------------------------------------------------------------------------------------


Integration with RStudio Server runs exactly like with RStudio Desktop, in the case where RStudio Server is not running on the same server as DSS.


In addition, in order to provide a better user experience to your users, you can choose to embed the RStudio Server UI directly within the Dataiku UI.



### [Embedding the RStudio Server UI in DSS](#id4)[¶](#embedding-the-rstudio-server-ui-in-dss "Permalink to this heading")


* Edit `/etc/rstudio/rserver.conf` and add a line `www-frame-origin = BASE_URL_OF_DSS`
* Restart RStudio Server
* Edit `DSS_DATA_DIR/config/dip.properties` and add a line `dku.rstudioServerEmbedURL=http(s)://URL_OF_RSTUDIO_SERVER/`
* Restart DSS


![../_images/menu_rstudio_server.png](../_images/menu_rstudio_server.png)
In a project, from the top navigation bar, the code menu will now have a new “RStudio Server” entry that gets you to RStudio Server. You need to login to RStudio Server independently from DSS.


You can then install the `dataiku` package and use the RStudio extensions (as documented above) to interact with DSS. If your RStudio Server is running on the same machine as DSS, more advanced integrations are possible. See below.





[RStudio Server (running on the DSS server)](#id5)[¶](#rstudio-server-running-on-the-dss-server "Permalink to this heading")
----------------------------------------------------------------------------------------------------------------------------


If:


* You are running RStudio Server
* RStudio Server is running on the same host as DSS
* You are using [User Isolation Framework](../user-isolation/index.html), and you are using the same UNIX account name in DSS and RStudio Server


You can use an enhanced version of the RStudio integration. In addition to the features documented above, this gives you the following (for each user of DSS who also uses RStudio Server):


* DSS can automatically install the `dataiku` package in the R library of the user
* DSS can automatically setup the connectivity between DSS and RStudio Server, so that you don’t have to go through the URL and API key declaration phase
* DSS can automatically create a RStudio Server project corresponding to a Dataiku project, giving you RStudio workspaces per DSS project.


To benefit from these:


* Embed RStudio Server as described above
* In the RStudio page, you’ll have a “RStudio actions” button



### [Installing the R package](#id6)[¶](#installing-the-r-package "Permalink to this heading")


Select the “Install R package” action. The `dataiku` package (and its dependencies) will be installed into the personal R library of the user.




### [Setup connectivity](#id7)[¶](#setup-connectivity "Permalink to this heading")


Select the “Setup connectivity to DSS” action. This action creates a personal API key and configures the `dataiku` package running in the personal R library of the user to be able to talk with DSS.


After this action, you can use the RStudio extensions documented above.




### [Create RStudio project](#id8)[¶](#create-rstudio-project "Permalink to this heading")


Select the “Create RStudio project” action. This action creates a folder in the home directory of the user and adds it to the “Recent projects” list. Afterwards, in RStudio Server, click “File \> Recent Projects” to switch to the project.