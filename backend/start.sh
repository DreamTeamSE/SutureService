
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m pip install grpcio
python -m pip install grpcio-tools
uvicorn main:app --reload
