 Installation & Running Instructions
# NATS Cluster Setup with Docker

## Prerequisites
- Docker installed
- `docker-compose` installed

## Setup & Running the Cluster
1. Clone this repository:

   git clone <repo-url>
   cd nats_impl

2. Start the NATS cluster:

    docker-compose up -d
    
    Check if all servers are running:
    
    docker ps
    
3. To test the cluster's resilience, stop one server:
    
    docker stop nats-server-demo2
    
    The cluster should remain operational.

4. Restart the stopped server:

    docker start nats-server-demo2

5. Connecting to the Cluster

   To connect a client to the cluster:
    
   Use any running server's address:

   nats bench demo --sub=10 -s nats://admin:natsdemo@localhost:4222
    
6. Stopping the Cluster

    To shut down all servers:
    
    docker-compose down
