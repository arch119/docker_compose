* Non-swarm mode
1. cd non_swarm && docker-compose up
2. go to http://localhost:5000/
3. docker-compose down in a new terminal to shut it down or use ctrl+c in the same terminal.
4. To rebounce individual service, use docker start/stop.
    e.g. docker stop web && docker start web 
    (to pick up any code changes in hello.py)