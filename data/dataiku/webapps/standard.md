“Standard” web apps[¶](#standard-web-apps "Permalink to this heading")
======================================================================


To create a standard web app, go to the Webapps list (click on the Code icon on the main toolbar then click on the Webapps tab), click new web app and select “Standard” web app


For a standard web app, you need to write at least:


* The HTML of your frontend
* Some CSS code if you want to style it
* Some Javascript code to make it do something


The Javascript code can use [The Javascript API](../api/js/index.html) to interact with datasets.


In addition, you can add a Python backend. A Python backend is a Python file which uses the Flask library. In the Python code, declare your Flask routes, and query them from the JS part using any AJAX library.