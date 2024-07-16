# Vigie IA 
## Run
### Backend

```bash
cd docker
docker compose -f docker-compose.middleware.yaml up -d
```

```bash
cd api
conda activate dify
flask run --host 0.0.0.0 --port=5001 --debug
```

```bash
cd api
conda activate dify
celery -A app.celery worker -P gevent -c 1 -Q dataset,generation,mail --loglevel INFO
```

### Frontend

```bash
conda activate dify 
cd web
npm run start
```

Open [http://localhost:3000](http://localhost:3000) 

## Update
### Backend

```bash
conda create --name dify python=3.10
pip install --upgrade -r requirements.txt
flask db upgrade
```
### Frontend

```bash
npm install
npm run build
```


```bash
sudo docker stop $(sudo docker ps -q)
docker container prune
sudo docker rmi $(sudo docker images -a -q)
```

```bash
sudo kill $(sudo lsof -t -i :5432)
sudo kill $(sudo lsof -t -i :3000)
sudo kill $(sudo lsof -t -i :5001)
sudo kill $(sudo lsof -t -i :6379)
sudo kill $(sudo lsof -t -i :8080)
sudo kill $(sudo lsof -t -i :3128)
sudo kill $(sudo lsof -t -i :80)
```

## Documentation

Visit <https://docs.dify.ai/getting-started/readme> to view the full documentation.




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
