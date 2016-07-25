We would like to explore viable use of server side encryption for S3.
Our requirements are summarized as below:
- multi-tenancy within single S3 bucket,
- prefix-based isolation for data from multiple customers, within single S3 bucket
- no shared keys across customers
- key rotation support for customer data/objects
- consider the performance impact when ingesting 2-4TB/hr, (typical object sizes around 100 KB)
- FIPS-140-2 level 2 certification support for SSE
