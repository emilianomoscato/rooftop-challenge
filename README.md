# rooftop-challenge
Career switch technical challenge



## Install instructions
### Docker
Docker file is included, just run:
```
cd path-to-project
docker build -t rf-ch-emoscato .
docker run --rm -ti rf-ch-emoscato:latest bash
```
You would need docker privileges to build/run the image.

### Standalone (Linux)
I recommend to run under a virtual environment.
```
cd path-to-project
pip install -r requirements.txt
```

## How to run 
Once installed, you can run test.py, pytest tests and sort_blocks.py
```
python3 test.py
pytest -v
python3 sort_blocks.py emiliano.moscato@gmail.com
python3 sort_blocks.py -t <token>

```
