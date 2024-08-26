Project Access[¶](#project-access "Permalink to this heading")
==============================================================



* [Discoverable projects](#discoverable-projects)
* [Private projects](#private-projects)
* [Access Requests](#access-requests)


	+ [Initiating a project access request](#initiating-a-project-access-request)
	+ [Managing a project access request](#managing-a-project-access-request)



Projects have two levels of access. They are either Private or with Limited Access. Both are governed by the same [Main project permissions](permissions.html) and can benefit from access request workflows.


The level of access and activation of request workflows can be configured in the Permissions pane of the project’s Security menu.



[Discoverable projects](#id1)[¶](#discoverable-projects "Permalink to this heading")
------------------------------------------------------------------------------------


Discoverable projects are visible to all users through **Home \> Projects page** or the global search.
Only a subset of project information is displayed to users that don’t have access to the project:


* Project key
* Project name
* Project owner (name \& login)
* Project status
* Project tags
* Short description
* Long description
* Project Image
* Creation date \& author
* Project contributors (name, login \& email)
* Whether the project is an app instance or an app\-as\-recipe


Discoverable projects are not displayed on the user’s homepage except if they have permissions on the project.




[Private projects](#id2)[¶](#private-projects "Permalink to this heading")
--------------------------------------------------------------------------


Private projects are visible only to users having permissions on the project. No information on these projects is made available to the other users without any permission.




[Access Requests](#id3)[¶](#access-requests "Permalink to this heading")
------------------------------------------------------------------------


By activating access requests on the project, project administrators allow users without permissions on the project to initiate a project permission access request. The recipients of such requests are all project administrators. See [Requests](../collaboration/requests.html) for more information.



### [Initiating a project access request](#id4)[¶](#initiating-a-project-access-request "Permalink to this heading")


Only users without any permissions on the project will be able to initiate a project access request. They will be able to do so through a modal that will be displayed when landing on the URL of the project or from the right\-panel of the “Search DSS Items” page when such a project is selected.


Users requesting access will not be able to define the level of permissions wanted on the project. However, a free\-text box in the request modal enables them to add a message to their requests in order to explain why they are requesting access and the level of permissions they want.




### [Managing a project access request](#id5)[¶](#managing-a-project-access-request "Permalink to this heading")


Project administrators can manage access requests from within the project’s security section or by handling the request in the requests inbox.


If they manage the request in the requests inbox, they will be able to select the user or the user group they are granting permissions to and give only “read\-project content” or “write\-project content” permission. To provide more granular permissions, they must go to the project’s security section.



Note


Automatic updates of the request:


In the following cases, the status of the request will be automatically updated:


* Request is considered as approved if the project administrator manually grants the requester or a group including the requester any “read” permissions
* Request is rejected if the requester is deleted
* Request is deleted if the project is deleted