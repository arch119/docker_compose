#!/bin/sh
git init
git add .
git commit -m "first commit"
git remote add origin https://github.com/arch119/docker_compose.git
git push -u origin master

