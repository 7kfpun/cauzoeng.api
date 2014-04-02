cauzoeng.api
============

## Cauzoeng API

### Lottery

#### Get

```
curl localhost:8080/_ah/api/lottery/v1/lottery/
```

#### Post

```
curl -X POST localhost:8080/_ah/api/lottery/v1/lottery/ -d '{"title": "", "subject": "", "description": "", "url": "", "created": "", "finished": ""}' -H "Content-Type: application/json""
```
