Reporting on scenario runs[¶](#reporting-on-scenario-runs "Permalink to this heading")
======================================================================================


Dataiku DSS provides the means to add reporters in a scenario. These reporters can be used to inform teams of users about scenario activities. For example, scenario reporters can update users about the training of models or changes in data quality. Reporters can also create actionable messages that users can receive within their [email](#scenario-reporter-mail) or through other [messaging channels](#scenario-reporter-channels).



Note


See our tutorial on [reporting scenario activities](https://knowledge.dataiku.com/latest/mlops-o16n/automation/tutorial-reporters.html) to learn how to send scenario updates to messaging channels.




Executing scenario reporters[¶](#executing-scenario-reporters "Permalink to this heading")
------------------------------------------------------------------------------------------


You can instruct a reporter to send messages at any point of a scenario run:


* To send a message right before a scenario run starts, add a reporter to the scenario in the **Settings** pane, and set the value of “Send on scenario” to **Start**.
* To send a message during the scenario run, add a **Send message** step (in a step\-based scenario) or use `get_message_sender()` on the `Scenario` object (in a script scenario).
* To send a message right after a scenario run ends, add a reporter to the scenario in the **Settings** pane, and set “Send on scenario” to **End**. You can further control whether the reporter runs at the end of the scenario, by specifying the “Run condition” as one of the expressions: `outcome == 'SUCCESS'` or `outcome == 'FAILED'` or `outcome == 'ABORTED'`. You can set up several reporters, each having a run condition and a corresponding message.




Building the message contents[¶](#building-the-message-contents "Permalink to this heading")
--------------------------------------------------------------------------------------------


Each reporter must define a message to broadcast on the selected messaging channel, and/or define some channel variables to pass to the reporter itself.


Reporting to mail provides the most versatility when building messages.



### Mail reporter[¶](#mail-reporter "Permalink to this heading")


Before you can send emails, an administrator needs to set up a mail channel (e.g. SMTP) in Administration \> Settings \> Notifications \& Integrations. Additional configuration outside of DSS may be necessary in some cases (cf. end of this section).


Dataiku DSS sends messages by mail in either HTML or plain text format, and two engines are available to build the messages:


* [Freemarker](http://freemarker.org/)\-based templating
* Variable\-based formatting, using [DSS formulas](https://knowledge.dataiku.com/latest/data-preparation/formulas/concept-formula-master.html)


In both cases, the results of the scenario run are offered to the engines as named variables.


DSS comes with a default Freemarker\-based template, and changing the “Message source” to **Inline** gives you the possibility to write your own message.


The “Recipients” field of the mail reporter can take a list of recipients in any of the following syntaxes:


* regular: `john.doe@here.com, jane.smith@there.org`
* JSON\-array style: `["john.doe@here.com", "jane.smith@there.org"]`


To send one individualized mail to each recipient, the syntax for the “Recipients” field is :



```
{
   "mails": [
      {
         "to": "[[email protected]](/cdn-cgi/l/email-protection)",
         "variables": {
            "variable1": "Sir",
            "variable2": "some special message for john"
         }
      },
      {
         "to": "[[email protected]](/cdn-cgi/l/email-protection)",
         "variables": {
            "variable1": "Madam"
         }
      }
   ]
}

```


The `variables` object for each recipient is then available for replacement in the mail message as a JSON string `mailVariables`, and its fields as `mailVariables_variableName`. For example, you can type:



```
Dear ${mailVariables_variable1},

${if(parseJson(mailVariables).hasField("variable2"), parseJson(mailVariables).get("variable2"), "message for not-john")}

Yours truly,
    A humble documentation

```



#### Microsoft 365 integration setup[¶](#microsoft-365-integration-setup "Permalink to this heading")


DSS can send emails via Microsoft 365 using OAuth2\. To do this, you have to first create and configure a new application in Azure with the right permissions:


1. Sign in to your Azure portal and navigate to the AAD resource. Click **App registrations** and provide a name for your application (there is no need for a redirect URI). After you register your application, make a note of **Application (client) ID** and **Directory (tenant) ID**.
2. Click **Certificates \& secrets** and create a new secret for your application. Make a note of **Value** (you won’t be able to view it anymore after you refresh this page).
3. Click **API permissions** and add permission **Mail.Send** under **Microsoft Graph** then **Application permissions** (it must be of type Application, not Delegated). Ask your Azure admin to **Grant admin consent** as well. By default, this would allow the application to send emails as any user of the Azure directory (tenant) with a valid Microsoft 365 license: the Azure admin could [restrict it to specific users](https://learn.microsoft.com/en-us/graph/auth-limit-mailbox-access).


Then, add a new channel in DSS, in Administration \> Settings \> Notifications \& Integrations:


1. Add a new **Mail (via Microsoft 365 with OAuth)** channel.
2. Fill in **Application (client) ID**, **Directory (tenant) ID**, and **Client secret** with what you noted down earlier.
3. Fill in **Sender email address** with the email address (AAD User Principal Name) of a user of the Azure directory (tenant) with a valid Microsoft 365 license.





### Slack, Microsoft Teams, Webhook and Twilio reporters[¶](#slack-microsoft-teams-webhook-and-twilio-reporters "Permalink to this heading")


These reporters only offer variable\-based formatting using DSS formulas for the message body. These reporters also take additional parameters, like message color or sender alias, that can be computed using DSS formulas. Note that Slack uses a specific [format](https://api.slack.com/docs/message-formatting) for its messages, and leaves html as\-is.



#### Slack integration setup[¶](#slack-integration-setup "Permalink to this heading")


Slack provides 2 methods to automatically send messages on a channel, and both are available in DSS:


* Through an [incoming webhook](https://api.slack.com/incoming-webhooks)
* Through a [bot user](https://api.slack.com/bot-users)


To use an incoming webhook in a DSS integration, specify “Mode” as **Use incoming webhook** and provide a value for the “Webhook URL”. In Slack, you can find the webhook URL by navigating to *Apps \& Integrations* \-\> *Manage* \-\> *Custom integrations* \-\> *Incoming webhooks*. To create an incoming webhook in your Slack channel, go to *Apps \& Integrations* \-\> *Build* (top right corner) \-\> *Make a Custom integration*, and from there you can create a new *Incoming webhook*.


A bot user has the advantage (over a simple incoming webhook) that the bot can have a preset appearance in the Slack channel. Using a bot user in a DSS integration means selecting the API mode and specifying the bot’s API token as authentication token. The API token can be found by navigating to *Apps \& Integrations* \-\> *Build* \-\> *Make a Custom integration* \-\> *Bots*.


Alternatively, you can use a [testing token](https://api.slack.com/docs/oauth-test-tokens) instead of a bot user, since they both rely on the same API token mechanism. Once they are created, you can access the token for your bot or incoming webhook by going to *Apps \& Integrations* \-\> *Manage* (top right corner) \-\> *Custom integrations*.




#### Microsoft Teams integration setup[¶](#microsoft-teams-integration-setup "Permalink to this heading")


Integration with Microsoft Teams from DSS requires that you set up and configure a workflow based on the template “Post to a channel when a webhook request is received”. Once configured, the integration with DSS supports simple text messages, as well as more complex and rich [Adaptive Cards](https://adaptivecards.io/) created via JSON.


Here is an example of a card with displays a message with a title and a color depending on the outcome of the scenario:



```
{
   "attachments":[
      {
         "contentType":"application/json",
         "content":{
            "$schema":"http://adaptivecards.io/schemas/adaptive-card.json",
            "type":"AdaptiveCard",
            "version":"1.0",
            "body":[
               {
                  "type":"Container",
                  "items":[
                     {
                        "type":"TextBlock",
                        "text":"${scenarioName} run report",
                        "weight":"bolder",
                        "size":"medium",
                        "style":"heading",
                        "wrap":true,
                        "color":"${if(outcome == 'FAILED', 'attention', 'default')}"
                     },
                     {
                        "type":"TextBlock",
                        "wrap":true,
                        "text":"[${scenarioName}](${scenarioRunURL}): **${outcome}**"
                     },
                     {
                        "type":"FactSet",
                        "facts":[
                           {
                              "title":"Project",
                              "value":"${scenarioProjectKey}"
                           },
                           {
                              "title":"Triggered by",
                              "value":"${triggerName}"
                           }
                        ]
                     }
                  ]
               }
            ]
         }
      }
   ]
}

```


A key advantage of this integration is the ability to utilize the power of working on data projects in DSS while harnessing the ease of communication and collaboration that Microsoft Teams provides to users.


Note that you can also send messages to Teams in custom scenarios. See [Custom scenarios](custom_scenarios.html) for some examples.





### Shell reporter[¶](#shell-reporter "Permalink to this heading")


DSS sends results of the scenario run to the shell script. You can use DSS formulas in the Administration section to specify values for environment variables that define the shell script.




### Scenario run URL[¶](#scenario-run-url "Permalink to this heading")


In order to use the reporter variable `${scenarioRunURL}`, an administrator must configure the “DSS URL” under Administration \> Settings \> Notifications \& Integrations \> DSS Location \> DSS URL.





Common variables[¶](#common-variables "Permalink to this heading")
------------------------------------------------------------------


You can use variables from the DSS instance, project, and scenario run, in the message. Two mechanisms are also available to help with customizing the message:


* Define new variables with a custom Python script.
* Handle variables in the message as DSS formulas.