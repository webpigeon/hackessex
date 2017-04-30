# hackessex

## Notes
* ws://localhost:8000/faqs/2/stream - Websocket url for room 2
* This branch is django channels enabled - websockets \o/

## Getting it running
* You might have to manually install twisted from the interwebs (or python-dev on debian) for this to work...
* pip install -r requirements.txt
* ./manage.py migrate
* ./manage.py makesuperuser
* ./manage.py runserver
