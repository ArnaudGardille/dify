
sudo chown $(whoami):staff /Users/gardille/.docker/buildx/activity/desktop-linux

docker build -t vigie-api .
docker build -t vigie-web .

docker tag vigie-api arnaudbg/vigie-api
docker tag vigie-web arnaudbg/vigie-web

docker tag vigie-api myRegistryVigie/vigie/vigie-api
docker tag vigie-web myRegistryVigie/vigie/vigie-web

docker push arnaudbg/vigie-web
docker push arnaudbg/vigie-api

docker tag vigie-api myRegistryVigie/vigie/vigie-api
docker tag vigie-web myRegistryVigie/vigie/vigie-web

docker push myRegistryVigie/vigie/vigie-api
docker push myRegistryVigie/vigie/vigie-web


docker cp management/add_tenant.py docker-api-1:/app/api/ # Or replace with /app/ if the app directory is directly under root
docker exec -it docker-api-1 bash
python api/add_tenant.py <account_id> --tenant_name "<new_tenant_name>" <role>
python api/add_tenant.py <account_id> --tenant_name "<new_tenant_name>" <role>


docker cp management/list_accounts.py docker-api-1:/app/api/

docker cp management/. docker-api-1:/app/api/



# List your docker containers
docker ps

# Connect to PostgreSQL container
docker exec -it <postgres-container-id> bash

# Connect to the PostgreSQL database
psql -U postgres -d dify