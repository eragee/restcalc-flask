# restcalc-flask
A simple REST calculator service written in Python/Flask that can be containerized and/or deployed to Cloud Run.

## Functions

### Add

#### Request

GET /restcalc/2/plus/3

#### Response

```
{
  "status": "OK",
  "result": "5"
}
```

### Subtract

#### Request

GET /restcalc/4.330/minus/2.123

#### Response

```
{
  "status": "OK",
  "result": "2.207"
}
```

### Multiply

#### Request

GET /restcalc/3094/times/203.5

#### Response

```
{
  "status": "OK",
  "result": "629629"
}
```

### Divide

#### Request

GET /restcalc/125/dividedby/4

#### Response

```
{
  "status": "OK",
  "result": "31.25"
}
```
