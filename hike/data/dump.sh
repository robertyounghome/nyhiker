#!/bin/bash 
python ../../manage.py dumpdata hike.Range -o range.json
python ../../manage.py dumpdata hike.Mountain -o mountain.json
python ../../manage.py dumpdata hike.Condition -o condition.json
python ../../manage.py dumpdata hike.Hike -o hike.json
python ../../manage.py dumpdata hike.HikeDetail -o hikeDetail.json
python ../../manage.py dumpdata hike.Challenge -o challenge.json
python ../../manage.py dumpdata hike.Grade -o grade.json
python ../../manage.py dumpdata hike.TrailLink -o traillink.json 
python ../../manage.py dumpdata hike.HikePart -o hikepart.json 
