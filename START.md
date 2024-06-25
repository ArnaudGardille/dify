# Vigie IA 
## Run
### Backend

```bash
screen -R docker
cd docker
docker compose -f docker-compose.middleware.yaml up -d
```

```bash
screen -R flask
cd api
poetry env use 3.10
poetry shell   
poetry run python -m flask run --host 0.0.0.0 --port=5001 --debug
```

```bash
screen -R celery 
cd api
poetry env use 3.10
poetry shell   
celery -A app.celery worker -P gevent -c 1 -Q dataset,generation,mail --loglevel INFO
```

### Frontend

```bash
screen -R frontend
cd web
npm run start
```

Open [http://localhost:3000](http://localhost:3000) 

## Update
### Backend

```bash
poetry env use 3.10
poetry install
poetry shell                                               
poetry add $(cat requirements.txt) 
poetry run python -m flask db upgrade
```
### Frontend

```bash
npm install
npm run build
```


```bash
sudo docker stop $(sudo docker ps -q)
docker container prune
```

```bash
sudo kill $(sudo lsof -t -i :5432)
sudo kill $(sudo lsof -t -i :3000)
sudo kill $(sudo lsof -t -i :5001)
sudo kill $(sudo lsof -t -i :6379)
sudo kill $(sudo lsof -t -i :8080)
sudo kill $(sudo lsof -t -i :3128)
```

## Documentation

Visit <https://docs.dify.ai/getting-started/readme> to view the full documentation.