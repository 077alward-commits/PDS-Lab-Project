
# PDS Lab Project

Distributed and Parallel Systems

## Problem 2: MPI Ring Communication

Language: C

This program implements ring communication using MPI.

Each process sends a message to its successor and receives
a message from its predecessor.

After communication, each process prints the received message.

### Requirements
- Microsoft MPI
- Microsoft MPI SDK
- GCC (MinGW-w64) on Windows

### Compilation
gcc -I "C:\Program Files (x86)\Microsoft SDKs\MPI\Include" ring.c "C:\Program Files (x86)\Microsoft SDKs\MPI\Lib\x64\msmpi.lib" -o ring.exe

### Execution
mpiexec -n 4 .\ring.exe

## Problem 3: Token Ring Mutual Exclusion

Language: Python

This program simulates a distributed printer system using
the Token Ring Mutual Exclusion algorithm.

Three independent processes communicate using UDP sockets.

Each process sends a printing request and waits for the token
before accessing the shared printer.

After printing, the process releases the printer and passes
the token to the next process.

### Requirements
- Python 3
- Three separate terminals

### Execution

Terminal 1:
python node.py 2

Terminal 2:
python node.py 3

Terminal 3:
python node.py 1

Press Enter in Terminal 3 to start the simulation.

### Note
The three processes were tested on one computer using
localhost to simulate three distributed nodes.

## Results

Both programs were executed successfully in local tests.
