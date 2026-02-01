gcloud compute scp --recurse infra/caddy/* parsa1-dev-instance:~/caddy --zone=europe-west3-a --project=parsa1

gcloud compute scp infra/docker-compose.yml parsa1-dev-instance:~/docker-compose.yml --zone=europe-west3-a --project=parsa1