cauzoeng.api
============

## Cauzoeng API

### User

#### Get

```
curl localhost:8080/_ah/api/core/v1/user/
```

#### Post

```
curl -X POST localhost:8080/_ah/api/core/v1/user/ -d '{"mac": "00:00:00:00", "name": "NAME"}' -H "Content-Type: application/json"
```
