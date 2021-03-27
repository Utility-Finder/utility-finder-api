# Deploy

## Setup Google Cloud Storage

### Instructions

- Create service account
  - Create a service account and give it `Editor` permissions.
  - Add a new key and download the credentials. Place in project root and rename to `service_creds.json`.

- Create bucket
  - Create a new bucket on Google Cloud Storage. Its name will be `GCLOUD_BUCKET_ID`.
  - Under Permissions tab, add member `allUsers` with permission `Storage Object Viewer`. This will make the bucket publicly visible.

## Deploy on Heroku

### Pre-requisites

  - Cloud storage is set up

### Instructions

  - Set up new app
    - Create a new app.
    - Add `heroku/python` and `https://github.com/buyersight/heroku-google-application-credentials-buildpack.git` as buildpacks.
  
  - Set up Postgres
    - Add [Heroku Postgres](https://www.heroku.com/postgres) to app.
    - Create `cube` and `earthdistance` extensions to database via pgAdmin or pgsql
  
  - Set up environment
    - Create config var with key `GOOGLE_CREDENTIALS` and copy the contents of `service_creds.json` as value.
    - Create config var with key `GOOGLE_APPLICATION_CREDENTIALS` and value `google-credentials.json`.
    - Create config var with key `GCLOUD_BUCKET_ID` and corresponding value.
  
  - Deploy
    - Follow instructions under Deploy tab