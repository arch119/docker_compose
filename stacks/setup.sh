#!/bin/sh

#Prerequisite: VirtualBox
echo "Creating 2 VirtualBox VMs"
docker-machine create --driver virtualbox myvm1
docker-machine create --driver virtualbox myvm2

docker-machine ls