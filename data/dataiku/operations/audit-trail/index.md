Audit trail[¶](#audit-trail "Permalink to this heading")
========================================================


DSS includes an audit trail that logs all actions performed by the users, with details about user id, timestamp, IP address, authentication method, …



* [Viewing the audit trail in DSS](viewing-in-dss.html)
* [Default storage of audit trail](default-storage.html)
* [Audit centralization and dispatch](centralization-and-dispatch.html)
	+ [Audit dispatching](centralization-and-dispatch.html#audit-dispatching)
	+ [Log4J target](centralization-and-dispatch.html#log4j-target)
	+ [EventServer target](centralization-and-dispatch.html#eventserver-target)
	+ [Kafka target](centralization-and-dispatch.html#kafka-target)
* [The DSS Event Server](eventserver.html)
	+ [Installing the event server](eventserver.html#installing-the-event-server)
	+ [Configuration of the event server](eventserver.html#configuration-of-the-event-server)
	+ [Security](eventserver.html#security)
	+ [Limitations](eventserver.html#limitations)
* [Configuration for API nodes](apinode.html)
	+ [Automatic configuration through API deployer](apinode.html#automatic-configuration-through-api-deployer)
		- [Automatic send to event server](apinode.html#automatic-send-to-event-server)
	+ [Sample setup: easy case](apinode.html#sample-setup-easy-case)
		- [Setup once (as admin)](apinode.html#setup-once-as-admin)
		- [For each service (as user)](apinode.html#for-each-service-as-user)
		- [Behind the scenes](apinode.html#behind-the-scenes)
	+ [Sample setup: high\-security API node centralization](apinode.html#sample-setup-high-security-api-node-centralization)
		- [Setup once (as admin)](apinode.html#id1)
		- [For each service (as admin)](apinode.html#for-each-service-as-admin)
		- [For each service (as user)](apinode.html#id2)
	+ [Manual usage](apinode.html#manual-usage)
* [Audit data](data.html)
	+ [Events envelopes](data.html#events-envelopes)
		- [In standard audit log files](data.html#in-standard-audit-log-files)
		- [In Event Server data files](data.html#in-event-server-data-files)
	+ [Event data](data.html#event-data)
		- [For “generic” topic](data.html#for-generic-topic)
		- [For “apinode\-query” topic](data.html#for-apinode-query-topic)
		- [For “compute\-resource\-usage” topic](data.html#for-compute-resource-usage-topic)
* [Audit trail on Dataiku Cloud](dataikucloud.html)
	+ [Access API node queries](dataikucloud.html#access-api-node-queries)
	+ [Access instances’ audit logs](dataikucloud.html#access-instances-audit-logs)