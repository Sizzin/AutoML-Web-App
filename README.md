# Deploying to Cloud Run

### Cloud Registry Build

```
gcloud builds submit --tag gcr.io/project_id/service_name
```

### Cloud Run Deploy

```
gcloud run deploy --image gcr.io/project_id/service_name
```