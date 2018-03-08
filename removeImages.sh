#!/bin/bash

echo "REMOVING ALL IMAGES"

sudo docker rmi -f $(sudo docker images -a -q)
