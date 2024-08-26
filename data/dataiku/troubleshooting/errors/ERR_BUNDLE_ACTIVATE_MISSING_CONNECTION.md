ERR\_BUNDLE\_ACTIVATE\_MISSING\_CONNECTION: Connection is missing[¶](#err-bundle-activate-missing-connection-connection-is-missing "Permalink to this heading")
===============================================================================================================================================================


The project you are trying to import/activate has a dependency on connection(s) that either do not exist or have been remapped to connection(s) that do not exist on the DSS instance.



Remediation[¶](#remediation "Permalink to this heading")
--------------------------------------------------------


Use the connection remapping option, and map the missing connection(s) to ones that exist on the DSS instance.
The connection remapping is available for both project import (tick the `Display advanced options after upload`) and bundle activation (in the `Activation settings` tab of the bundles management screen).