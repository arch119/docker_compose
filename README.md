* Non-swarm mode
1. cd non_swarm && docker-compose up
2. go to http://localhost:5000/
3. docker-compose down in a new terminal to shut it down or use ctrl+c in the same terminal.
4. To rebounce individual service, use docker start/stop.
    e.g. docker stop web && docker start web 
    (to pick up any code changes in hello.py)

* Swarm Mode (with a single node a.k.a docker stack)
1. cd swarm && docker swarm init
2. docker build -t hello_swarm .
3. docker stack deploy -c docker-compose.yml hello_from_swarm
4. go to http://localhost:5000
5. To stop: docker stack rm hello_from_swarm
6. To leave the swarm : docker swarm leave --force (use docker node ls to check )