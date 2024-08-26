ERR\_SECURITY\_DECRYPTION\_FAILED: Decryption failed due to invalid HMAC[¶](#err-security-decryption-failed-decryption-failed-due-to-invalid-hmac "Permalink to this heading")
==============================================================================================================================================================================


If you receive an error similar to `Decryption Failed, caused by: CodedException: Invalid HMAC` or `Decryption Failed`, this is usually caused by copying over your `connections.json` file from one instance to another. Passwords in `connections.json` are encrypted with an encryption key that is specific to the original instance.



Remediation[¶](#remediation "Permalink to this heading")
--------------------------------------------------------


To resolve this, do not copy over your `connections.json` file from one instance to another. If you receive this error, you will need to re\-enter the passwords in each connection’s settings page of the instance.