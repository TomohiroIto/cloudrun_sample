
```
gcloud builds submit --config=cloudbuild.yaml --substitutions=_PROJECT="xxxx"
```

```
npm install -g ajv-cli ajv-formats
curl -o workflows.schema.json https://json.schemastore.org/workflows.json
```

```
npx ajv validate -c ajv-formats -s .\workflows.schema.json -d ./**/*.yaml
```


## GitHub Actions

```yaml
name: Validate Workflows

on:
  pull_request:
    paths:
      - "workflows/**"

jobs:
  validate-workflow-schema:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Validate workflow schema
        run: |
          npx -y \
              -p "ajv-cli@5.0.0" \
              -p "ajv-formats@2.1.1" \
              ajv validate \
                -c ajv-formats \
                -s workflows.schema.json \
                -d "workflows/**/*.yaml"
```