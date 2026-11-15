# PDS Lab Project

482 CCS – Parallel and Distributed Systems
King Khalid University – College of Computer Science

## Files

| File | Problem |
|------|---------|
| `ring.c` | Problem 2 – MPI Ring Communication (C) |
| `node.py` | Problem 3 – Token Ring Mutual Exclusion (Python) |

## Problem 2: MPI Ring Communication

Language: C

This program implements ring communication using MPI.
Each process sends a message to its successor `(rank + 1) % size`
and receives a message from its predecessor `(rank - 1 + size) % size`.

`MPI_Sendrecv` is used so that sending and receiving happen in one call,
which avoids deadlock. `fflush(stdout)` makes sure every process's line
is printed before the program exits.

### Requirements
- Microsoft MPI
- Microsoft MPI SDK
- GCC (MinGW-w64) on Windows

### Compilation
```
gcc -I "C:\Program Files (x86)\Microsoft SDKs\MPI\Include" ring.c "C:\Program Files (x86)\Microsoft SDKs\MPI\Lib\x64\msmpi.lib" -o ring.exe
```

### Execution
```
mpiexec -n 4 .\ring.exe
```

### Expected output (order may vary)
```
Process 0 sent to Process 1 and received from Process 3: Hello from Process 3
Process 1 sent to Process 2 and received from Process 0: Hello from Process 0
Process 2 sent to Process 3 and received from Process 1: Hello from Process 1
Process 3 sent to Process 0 and received from Process 2: Hello from Process 2
```

## Problem 3: Token Ring Mutual Exclusion

Language: Python

This program simulates a distributed printer shared by three processes
(P1, P2, P3) using the Token Ring Mutual Exclusion algorithm.
The processes form a logical ring (P1 → P2 → P3 → P1) and communicate using UDP sockets.

How it works:
1. P1 starts with the token and sends `START` to P2 and P3.
2. Each process sends a `REQUEST` message that travels around the ring.
3. When a process's own request returns and it holds the `TOKEN`,
   it enters the critical section and prints.
4. After printing, it releases the printer, informs P1 with `DONE`,
   and passes the `TOKEN` to the next process.
5. When all three jobs are done, P1 sends `STOP` and all processes finish.

A process keeps the token until its own request is complete,
so only one process can print at a time and the token does not circulate without need.

### Requirements
- Python 3
- Three separate terminals

### Execution
```
Terminal 1:  python node.py 2
Terminal 2:  python node.py 3
Terminal 3:  python node.py 1
```
Press Enter in Terminal 3 to start the simulation.

### Note
The three processes were tested on one computer using localhost
(ports 5001, 5002, 5003) to simulate three distributed nodes.

## Results

Both programs were executed successfully. Screenshots of the output
are included in the lab report.
