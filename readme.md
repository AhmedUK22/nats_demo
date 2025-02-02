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

5. Simulating the Cluster Environment

   Steps 1: Starts the NATS Cluster

   Ensure all NATS server are up and running using
   docker-compose up -d
   
   Step 2: Create a Subscriber

   Run the following command to subscribe to the demo subject with 10 subscribers across the cluster:

   nats bench demo --sub=10 -s nats://admin:natsdemo@localhost:4222,nats://admin:natsdemo@localhost:4223,nats://admin:natsdemo@localhost:4224

   Step 3: Publish Messages
   
   Create a publisher that sends messages to the demo subject across all available servers:

   nats pub demo hi --count=-1 --sleep=500ms -s nats://localhost:4222,nats://localhost:4223,nats://localhost:4224 --user admin --password natsdemo

   Step 4: Test Cluster Failover

   Stop a NATS server and observe how the cluster handles failover:

   docker stop nats-server-demo2

   Even with one server down, the remaining servers should continue processing messages.

   Restart the server to restore full cluster functionality:
   
   docker start nats-server-demo2

6. Stopping the Cluster

   To gracefully shut down all NATS servers:
    
   docker-compose down
