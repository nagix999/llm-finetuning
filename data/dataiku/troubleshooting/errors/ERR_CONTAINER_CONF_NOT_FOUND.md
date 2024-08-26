ERR\_CONTAINER\_CONF\_NOT\_FOUND: The selected container configuration was not found[¶](#err-container-conf-not-found-the-selected-container-configuration-was-not-found "Permalink to this heading")
=====================================================================================================================================================================================================


The recipe or visual ML task was configured on a containerized execution configuration that does not
exist anymore. It may also be the case that it is configured to inherit the containerized execution
configuration from the project, and that the project settings refer this non\-existing
configuration.



Remediation[¶](#remediation "Permalink to this heading")
--------------------------------------------------------


Either re\-create (or ask your DSS administrator to recreate) a containerized execution configuration
with the same name, or select another containerized execution configuration. If the configuration is
selected at the project level, you may need the DSS administrator or the project owner to do this.