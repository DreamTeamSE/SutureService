docker build -t ghcr.io/dreamteamse/sutureservice-arduino-manager:staging ../arduino_manager/.
docker build -t ghcr.io/dreamteamse/sutureservice-backend:staging ../backend/.
docker build -t ghcr.io/dreamteamse/sutureservice-frontend:staging ../frontend/.

docker push ghcr.io/dreamteamse/sutureservice-arduino-manager:staging
docker push ghcr.io/dreamteamse/sutureservice-backend:staging
docker push ghcr.io/dreamteamse/sutureservice-frontend:staging
