Websockets problems[¶](#websockets-problems "Permalink to this heading")
========================================================================



I am seeing the “Could not establish WebSocket connection” message[¶](#i-am-seeing-the-could-not-establish-websocket-connection-message "Permalink to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------


![../../_images/websockets-1.png](../../_images/websockets-1.png)
Data Science Studio uses a web technology called “Websockets” to provide a more dynamic user experience.
In some setups, Websockets cannot work and you see this message.



### Causes[¶](#causes "Permalink to this heading")


The most common cause of Websocket error is when you connect to DSS through a proxy. Websockets is a fairly recent protocol and many enterprise proxies do not support it. The websocket connection will not establish and you will see this message.


Note that using a reverse proxy in front of DSS can also lead to this behaviour. Please refer to our
[reverse proxy configuration page](../../installation/custom/reverse-proxy.html) for details.


If you are not in any of these cases, please [contact Dataiku support](http://support.dataiku.com).




### Consequences[¶](#consequences "Permalink to this heading")


If your setup does not allow Websockets to work, the following features of DSS will not work :


* The whole Python / R notebook. You will not be able to load, execute, export or convert to recipe any Python / R notebook
* Dynamic notifications (connections, disconnections, end of job, comments, exports, …)
* Some lists refresh when new events happen (end of training a model bench, …)
* Editor’s conflict detection
* Achievements




### Remedies[¶](#remedies "Permalink to this heading")


If you can, please ensure that your connection to DSS is not done through a proxy. Generally, connections within a company do not require a proxy.


Another possibility is to use DSS on HTTPS. Proxies generally do not filter SSL connections and Websockets will work correctly. Please refer to
the [installation guide](../../installation/custom/advanced-customization.html#config-https) for help on setting up DSS on HTTPS.