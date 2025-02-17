docker build -t ghcr.io/dreamteamse/sutureservice-arduino-manager:prod ../arduino_manager/.
docker build -t ghcr.io/dreamteamse/sutureservice-backend:prod ../backend/.
docker build -t ghcr.io/dreamteamse/sutureservice-frontend:prod ../frontend/.

docker push ghcr.io/dreamteamse/sutureservice-arduino-manager:prod
docker push ghcr.io/dreamteamse/sutureservice-backend:prod
docker push ghcr.io/dreamteamse/sutureservice-frontend:prod
