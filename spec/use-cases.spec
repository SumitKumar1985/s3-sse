As a user Bob that is privileged to upload a file at a specific location (identified by a prefix in S3),
I want to upload a file to S3 and protect it using server-side encryption,
So that the file contents are not exposed.

As a user Alice that is privileged to read a file protected by SSE, at a specific location (identified by a key in S3),
I want to be able to read the file contents in plaintext (unencrypted),
So that the file contents are only visible to privileged users.

As users Charlie and David that are privileged to upload files at different locations (identified by different prefixes in the same bucket in S3 and protected by SSE),
These users can only perform operations on files (protected by SSE), under the respective locations,
So that file contents at different locations are restricted for use by different users. 

As users Charlie and David that upload files at different locations (identified by different prefixes in the same bucket in S3 and protected by SSE),
The keys used to encrypt the files at these locations are different,
So that file contents at different locations are encrypted and decrypted using different sets of encryption keys.

As user Eric that is administering the encryption keys used to protect files stored at different locations (identified by different prefixes in the same bucket in S3 and protected by SSE),
I can administer the encryption keys for each such location independently,
So that these keys may be created, expired, rotated, renewed, deleted, logged, and usage audited independently.
