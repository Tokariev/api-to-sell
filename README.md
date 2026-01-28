# API-to-Sell

Monorepo for building and selling APIs on RapidAPI. Supports services written in Python (FastAPI) and TypeScript (NestJS).

## Project Structure

```
api-to-sell/
├── .github/workflows/          # CI/CD - one workflow per service
├── services/
│   ├── sample-nestjs/          # Sample NestJS API with Swagger docs
│   └── sample-python/          # Sample FastAPI with auto-generated docs
└── infra/
    ├── caddy/Caddyfile         # Production reverse proxy + RapidAPI auth
    ├── caddy/Caddyfile.dev     # Dev reverse proxy (no auth)
    ├── docker-compose.yml      # Production stack (Docker Hub images + Watchtower)
    ├── docker-compose.dev.yml  # Local dev stack (builds from source, hot reload)
    └── terraform/
        ├── modules/compute/    # Reusable GCE VM module
        └── environments/
            ├── dev/            # Dev environment (e2-small)
            └── prod/           # Prod environment (e2-medium)
```

## Key Design Decisions

- **Caddy as gateway** - handles TLS termination. In production, validates `X-RapidAPI-Proxy-Secret` header on API routes (docs endpoints are accessible without auth). In local dev, no auth is required.
- **API documentation** - FastAPI auto-generates Swagger UI at `/docs` and ReDoc at `/redoc`. NestJS uses `@nestjs/swagger` at `/docs`. Docs are served through Caddy at `/sample-*-docs/docs` without requiring the RapidAPI secret.
- **One database, multiple services** - single PostgreSQL container shared by all services. Each service connects via `DATABASE_URL` environment variable.
- **Auto-deploy via Watchtower** - production compose includes Watchtower, which polls Docker Hub every 60 seconds for new image versions and auto-restarts containers.
- **Per-service CI/CD** - each service has its own GitHub Actions workflow, triggered only when files in that service's directory change.
- **Terraform per environment** - shared compute module with separate env configs (dev/prod) for GCP Compute Engine VMs running Container-Optimized OS.

## How It Works

```
RapidAPI → Caddy (validates X-RapidAPI-Proxy-Secret) → Service containers
                                                         ↕
                                                      PostgreSQL
```

1. RapidAPI sends requests to your server with the `X-RapidAPI-Proxy-Secret` header
2. Caddy validates the header — rejects with 403 if missing/invalid
3. Caddy strips the service path prefix and forwards to the correct container
4. Each service runs independently and connects to the shared PostgreSQL database

**Routing:**

| Path | Target | Auth (prod only) |
|------|--------|-------------------|
| `/sample-nestjs/*` | NestJS service (port 3000) | Yes |
| `/sample-python/*` | Python service (port 8000) | Yes |
| `/sample-nestjs-docs/*` | NestJS Swagger docs | No |
| `/sample-python-docs/*` | Python Swagger docs | No |

## Getting Started Locally

1. Navigate to the infra directory:

```bash
cd infra
```

2. Start all services:

```bash
docker compose -f docker-compose.dev.yml up --build
```

3. Test the endpoints (no auth required in dev):

```bash
# API
curl -sk https://localhost/sample-python/health
curl -sk https://localhost/sample-nestjs/health

# Docs
open https://localhost/sample-python-docs/docs
open https://localhost/sample-nestjs-docs/docs
```

The dev compose mounts source directories as volumes, so changes to Python and NestJS code are reflected without rebuilding.

## Required GitHub Secrets for CI/CD

Configure these in your GitHub repository settings under **Settings > Secrets and variables > Actions**:

| Secret | Description |
|--------|-------------|
| `DOCKERHUB_USERNAME` | Your Docker Hub username |
| `DOCKERHUB_TOKEN` | Docker Hub access token ([create one here](https://hub.docker.com/settings/security)) |

## Adding a New Service

1. Create a new directory under `services/` with a `Dockerfile`:

```
services/my-new-api/
├── Dockerfile
└── ... (your service code)
```

2. Add a `route` block (with auth) and a `handle` block (for docs) in `infra/caddy/Caddyfile`:

```caddy
route /my-new-api/* {
    @unauthorized not header X-RapidAPI-Proxy-Secret {$RAPIDAPI_PROXY_SECRET}
    respond @unauthorized "Unauthorized" 403
    uri strip_prefix /my-new-api
    reverse_proxy my-new-api:8000
}

handle /my-new-api-docs/* {
    uri strip_prefix /my-new-api-docs
    reverse_proxy my-new-api:8000
}
```

3. Add the service to both `infra/docker-compose.yml` (production) and `infra/docker-compose.dev.yml` (dev). For FastAPI services, set `ROOT_PATH` to the docs prefix so Swagger UI generates correct URLs:

```yaml
my-new-api:
  image: ${DOCKERHUB_USERNAME}/my-new-api:latest  # production
  # build:                                         # dev
  #   context: ../services/my-new-api
  environment:
    - ROOT_PATH=/my-new-api-docs  # FastAPI only - enables docs behind reverse proxy
    - DATABASE_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@postgres:5432/${POSTGRES_DB}
  depends_on:
    - postgres
```

4. Copy an existing workflow in `.github/workflows/` and update the service name and path trigger:

```yaml
on:
  push:
    branches: [main]
    paths:
      - "services/my-new-api/**"
```

