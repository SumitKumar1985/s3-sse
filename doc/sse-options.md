Server-side Encryption with S3 is supported in the following modes:

- SSE-S3

Amazon S3 encrypts each object with a unique key. It encrypts each key itself with a master key that it regularly rotates. It uses AES-256 to encrypt data

You can use bucket policies to enforce that all objects stored in the bucket are protected by server-side encryption. (However, you cannot enforce whether or not objects are encrypted with SSE-S3, if objects are uploaded using pre-signed URLs)

- SSE-KMS

Amazon S3 encrypts each object using a unique data key that is generated using a CMK in KMS.
If the user chooses not to specify a CMK in KMS, S3 will choose a CMK generated automatically in KMS for the use of S3 service (for the account in that region). This CMK is visible in KMS to the customer on the account

- SSE-C

Amazon S3 encrypts each object (using AES) using a key supplied by the customer.
The data keys used to encrypt your data are also encrypted and stored alongside the data they protect.

Common aspects:
SSE encrypts only the object. Object metadata is not encrypted
