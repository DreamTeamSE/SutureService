docker build -t ghcr.io/dreamteamse/sutureservice-arduino-manager:dev ../arduino_manager/.
docker build -t ghcr.io/dreamteamse/sutureservice-backend:dev ../backend/.
docker build -t ghcr.io/dreamteamse/sutureservice-frontend:dev ../frontend/.

docker push ghcr.io/dreamteamse/sutureservice-arduino-manager:dev
docker push ghcr.io/dreamteamse/sutureservice-backend:dev
docker push ghcr.io/dreamteamse/sutureservice-frontend:dev
