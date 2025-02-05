# How to Implement Security in NATS using Distributed Authentication

Follow the steps below to implement security in NATS using JWT and distributed authentication.

## Step 1: Initialize NATS Security

1. Open PowerShell inside the `jwt` folder in your repository.

2. Run the following Docker command to access the `nats-box` container:
   
   docker run --rm -it --network nats-network -v ${PWD}:/nsc -w /nsc natsio/nats-box
3. Initialize the nsc environment:

    nsc init --name nats_anglesey_setup
4. Add an operator with a signing key:

    nsc add operator --generate-signing-key --sys --name AngleseyDemoOperator
5. Edit the operator configuration to require signing keys and set the account JWT server URL:

    nsc edit operator --require-signing-keys --account-jwt-server-url "nats://0.0.0.0:4222"
6. Add an account:

    nsc add account --name AngleseyDemoAccount
7. Edit the account and generate a signing key:

    nsc edit account AngleseyDemoAccount --sk generate
8. Add a user to the account:

    nsc add user --account AngleseyDemoAccount anglesey_client_demo
9. Generate the credentials file for the user:

    nsc generate creds --account AngleseyDemoAccount --name anglesey_client_demo
10. List the available keys:

    nsc list keys -A
11. Generate a NATS resolver configuration:

    nsc generate config --nats-resolver --sys-account SYS > resolver.conf
12. Generate the credentials file for the user:

    nsc generate creds -n anglesey_client_demo > anglesey_client_demo.cred

## Step 2: Push Security Credentials to NATS Server

1. Before pushing the credentials to NATS, make sure the NATS server is up and running using the command:

    docker-compose up -d
2. Push the generated JWT credentials to the NATS server:

    nsc push -u nats://nats_jwt_demo:4222 -A
3. Once the push is successful, exit the nsc environment:

    exit

## Step 3: Test Connectivity with NATS

1. In the same folder, run the Python script to check the connectivity:

    python nats_jwt.py

This will connect to the NATS server using JWT authentication and print a success message Received message: Hello, NATS!.





