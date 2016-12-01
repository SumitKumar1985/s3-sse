# use virtualenv and obtain and install the required modules

```
$ virtualenv sse-environment
$ source sse-environment/bin/activate
$ pip install -r requirements.txt
```

# Configure credentials to access AWS (specifically s3)

```
$ export AWS_PROFILE=me@my-account
```

# Run the tests

```
$ python -m unittest test_s3
```
