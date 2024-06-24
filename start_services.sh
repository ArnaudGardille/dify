#!/bin/bash

# Function to start a command in a named screen session
start_in_screen() {
    local session_name=$1
    local command=$2
    screen -dmS "$session_name" bash -c \"$command\"
    echo "Started '$command' in screen session '$session_name'"
    echo "screen -dmS "$session_name" bash -c "$command""
}

# Start each command in a separate screen session
start_in_screen "middleware" "cd docker; docker compose -f docker-compose.middleware.yaml up -d"
start_in_screen "api_flask" "cd api; conda activate dify; flask run --host 0.0.0.0 --port=5001 --debug"
start_in_screen "api_celery" "cd api; conda activate dify; celery -A app.celery worker -P gevent -c 1 -Q dataset,generation,mail --loglevel INFO"
start_in_screen "frontend" "conda activate dify; cd web; npm run start"
