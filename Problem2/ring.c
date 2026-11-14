
#include <stdio.h>
#include <mpi.h>

int main(int argc, char *argv[]) {
    int rank, size;
    int next, previous;
    char message[100];
    char received[100];

    MPI_Init(&argc, &argv);

    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    next = (rank + 1) % size;
    previous = (rank - 1 + size) % size;

    sprintf(message, "Hello from Process %d", rank);

    MPI_Sendrecv(
        message, 100, MPI_CHAR, next, 0,
        received, 100, MPI_CHAR, previous, 0,
        MPI_COMM_WORLD, MPI_STATUS_IGNORE
    );

    printf("Process %d received: %s\n", rank, received);

    MPI_Finalize();

    return 0;
}
