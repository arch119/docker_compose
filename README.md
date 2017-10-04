* Non-swarm mode
1. cd non_swarm && docker-compose up
2. go to http://localhost:5000/
3. docker-compose down in a new terminal to shut it down or use ctrl+c in the same terminal.
4. To rebounce individual service, use docker start/stop.
    e.g. docker stop web && docker start web 
    (to pick up any code changes in hello.py)

* Swarm Mode (with a single node a.k.a docker stack)
1. cd swarm_single_node && docker swarm init
2. docker build -t hello_swarm .
3. docker stack deploy -c docker-compose.yml hello_from_swarm
4. go to http://localhost:5000
5. To stop: docker stack rm hello_from_swarm
6. To leave the swarm : docker swarm leave --force (use docker node ls to check )

* Swarm Mode (with multiple nodes)
1. cd swarm_multi_node && /bin/sh setup.sh  and note the IP addresses of both Vms
2. Make VM1 the manager node
docker-machine ssh myvm1 "docker swarm init --advertise-addr <myvm1 ip add>"
Note the command to be executed for the worker
3. Run the command for myvm2
e.g. docker swarm join --token SWMTKN-1-2126j8dbb3iqwtl1y9w1s17jjo7ufwcpc8iqgfpoqm2b2capsv-8euhkp1t79b00602jy4zj93el 192.168.99.100:2377
4. Confirm the status of nodes
docker-machine ssh myvm1 "docker node ls"
5. Make docker-machine talk to myvm1 by default without the ssh
eval $(docker-machine env myvm1)
docker-machine ls
6. Now move to previous directory
cd ../swarm_single_node and create the docker image one more time
docker build -t hello_swarm .
(this needs to be done in all the vms - unless the docker image is published to docker hub)
7. And run the same command
docker stack deploy -c docker-compose.yml hello_swarm
8. Use 'docker service ls' or 'docker stack ps hello_swarm' to check the status
9. Access the website at http://<ip add of myvm1 or myvm2>:5000
10. CLeanup Swarm: 'docker stack rm hello_swarm'
11. Cleanup VMs: 'docker-machine rm myvm1', 'docker-machine rm myvm2'