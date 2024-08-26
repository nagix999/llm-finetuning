Reusing Python code[¶](#reusing-python-code "Permalink to this heading")
========================================================================



* [Sharing Python code within a project](#sharing-python-code-within-a-project)


	+ [Working with multiple source folders](#working-with-multiple-source-folders)
* [Importing libraries from other projects](#importing-libraries-from-other-projects)
* [Sharing Python code globally](#sharing-python-code-globally)


	+ [Permissions](#permissions)
* [Manual editing of code library folders](#manual-editing-of-code-library-folders)
* [Packaging code as plugins](#packaging-code-as-plugins)



When you write a lot of Python code in a project, or across projects, you will often want to make reusable parts of code.


DSS provides several mechanisms for reusing Python code:


* Packaging your code as functions or modules, and making them available in a specific project
* Importing code that has been made available from one project to another
* Packaging your code as functions or modules, and making them available in all projects
* Packaging your code as a reusable plugin, and making it available for coder and non\-coder users alike



[Sharing Python code within a project](#id1)[¶](#sharing-python-code-within-a-project "Permalink to this heading")
------------------------------------------------------------------------------------------------------------------


In each project, you can write Python modules in the **Library editor**. The project’s library editor is available by going into the “Code” universe (orange), and selecting the “Libraries” tab.


![../_images/project-lib-editor-python.png](../_images/project-lib-editor-python.png)
You can then write code under a “Python source” folder, i.e. a folder that has the “Python” icon associated to it.


Modules that are written here are automatically available in all Python code in the same project. Import rules are the regular Python rules.


For example, to use the function shown in the above image, use:



```
from analyticfunctions import build_custom_keras_model
model = build_custom_keras_model()

```


or:



```
import analyticfunctions
model = analyticfunctions.build_custom_keras_model()

```



Note


Don’t forget that if you create subfolders in a Python source folder, each folder must have a `__init__.py` file in order to be a valid Python module



For a file at the root of the library editor:


![../_images/project-lib-editor-python-2.png](../_images/project-lib-editor-python-2.png)

[Importing libraries from other projects](#id3)[¶](#importing-libraries-from-other-projects "Permalink to this heading")
------------------------------------------------------------------------------------------------------------------------


If you have created libraries in a project A, you can import them in project B. The libraries of project A will be added to the source path of all code running in project B.


* Go to the library editor of project B
* Open the `external-libraries.json` file
* Edit the `importLibrariesFromProjects` list and add the project key (which appears in the URL, i.e. not the project display name) to it
* Save the `external-libraries.json` file


You need to have “Read project content” permission on A and “write project content” on B.




[Sharing Python code globally](#id4)[¶](#sharing-python-code-globally "Permalink to this heading")
--------------------------------------------------------------------------------------------------


In addition to the per\-project Python library editor, there is another global Python library editor for the whole instance.
The global Python library editor is available from the **Application menu \> Global Shared Code**.


![../_images/global-shared-code.png](../_images/global-shared-code.png)
Modules that are written here are automatically available in all Python code in all projects.
Import rules follow the regular Python rules (see above for more information).



### [Permissions](#id5)[¶](#permissions "Permalink to this heading")


You need the “Edit lib folders” global (group\-level) permission to use the global Python library editor.



Caution


Putting code in the global library increases the risk of having clashes or conflicts.
Generally speaking, it is preferable to use per\-project libraries.


Libraries in the global folder will be importable in all Python code,
regardless of the active [code environment](../code-envs/index.html).
You should ensure that your code is compatible with Python 3\.




Warning


Although global libraries are included in [API node service packages](../apinode/concepts.html),
they are not included in [project bundles](../deployment/creating-bundles.html).






[Manual editing of code library folders](#id6)[¶](#manual-editing-of-code-library-folders "Permalink to this heading")
----------------------------------------------------------------------------------------------------------------------


Although not recommended, if you have shell access to the DSS machine, you can modify the library folders directly:


* Per\-project library folder is in `DATA_DIR/config/projects/PROJECT_KEY/lib`
* Global library folder is in `DATA_DIR/lib/python`




[Packaging code as plugins](#id7)[¶](#packaging-code-as-plugins "Permalink to this heading")
--------------------------------------------------------------------------------------------


See [Plugins](../plugins/index.html)