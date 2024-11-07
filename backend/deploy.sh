docker build -t suture-backend . 
docker run -d --name suture-backend -p 8000:8000 suture-backend