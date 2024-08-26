Using Plot.ly[¶](#using-plot-ly "Permalink to this heading")
============================================================



Note


This section deals with using plot.ly using Python code. plot.ly can also be used through R code.



Plot.ly is a service and Python interactive visualization library that lets users easily create interactive charts and dashboards, that can optionally be shared through an online service. There are several ways you can use Plot.ly in DSS:


* To display interactive (pan/zoom/…) charts within a Jupyter notebook
* To display interactive (pan/zoom/…) charts on a Dashboard


Documentation for Plot.ly is available at <https://plot.ly/python/>



Installing plot.ly[¶](#installing-plot-ly "Permalink to this heading")
----------------------------------------------------------------------


You need to install the `plotly` package. The recommended method for doing so is to use a [code environment](../code-envs/index.html). See [how to install Python packages](packages.html)




Displaying charts in a Jupyter notebook[¶](#displaying-charts-in-a-jupyter-notebook "Permalink to this heading")
----------------------------------------------------------------------------------------------------------------


To display plot.ly charts in a Jupyter notebook, use:



```
import plotly.offline as py

py.iplot(data_object)

```


For example, to display a simple line:



```
import plotly.offline as py
import plotly.graph_objs as go

scatter = go.Scatter(x =[1,2,3], y = [10, 15, 13])
data = go.Data([scatter])

py.iplot(data)

```




Displaying charts on a dashboard[¶](#displaying-charts-on-a-dashboard "Permalink to this heading")
--------------------------------------------------------------------------------------------------


plot.ly charts generated using Python code can be shared on a DSS dashboard using the “static insights” system.


Each plot.ly figure can become a single insight in the dashboard. Each chart will retain full zoom/pan/select/export capabilities;


To do so, create [static insights](https://developer.dataiku.com/latest/api-reference/python/static-insights.html "(in Developer Guide)")



```
from dataiku import insights

# f is a plot.ly figure, or any object that can be passed to iplot()

insights.save_plotly("my-plotly-plot", f)

```


From the Dashboard, you can then add a new “Static” insight, select the `my-plotly-plot` insight



### Refreshing charts on a dashboard[¶](#refreshing-charts-on-a-dashboard "Permalink to this heading")


You can refresh the charts automatically on a dashboard by using a scenario to re\-run the above piece of code.


This call to `dataiku.insights` code can be:


* In a DSS recipe (use a regular “Build” scenario step)
* In a Jupyter notebook (use a “Export notebook” scenario step)
* As a custom Python scenario step