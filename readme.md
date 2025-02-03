Installation & Running Instructions
# NATS Cluster Setup with Docker

## Prerequisites
- Docker installed
- `docker-compose` installed

## Setup & Running the Cluster
1. Clone this repository:

   git clone <repo-url>

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


# Working with Key-Value Store in NATS

Once your NATS cluster is running, you can use the following Python script to interact with JetStream and perform Key-Value operations. This script will help you store and retrieve values from the Key-Value store in your JetStream-enabled NATS cluster.

1. Run the Script

   Ensure your NATS cluster is running using docker-compose up -d

   Once the cluster is up, run the script:

   python nats_kv.py

   The script will prompt you to confirm when the cluster is up and running. After that, it will create a Key-Value bucket, store a value, and then ask you to manually stop one of the NATS servers. It will then attempt to retrieve the value again, demonstrating the cluster's resilience to server failures.

2. Stop a NATS Server

   Follow the prompt in the script to stop one of the NATS servers manually. You can do this by running:

   docker stop nats-server-demo1

3. Observe the Result

   After stopping one of the servers, press ENTER in the script to see if it can still retrieve the stored value from the Key-Value store. The script will demonstrate how the JetStream Key-Value store handles a server failure in the cluster.