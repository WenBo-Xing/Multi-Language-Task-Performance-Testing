#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <time.h>
#include <string.h>

// ---------------------
// Dijkstra
// ---------------------
#define V 100

int minDistance(int dist[], int sptSet[]) {
    int min = INT_MAX, min_index = -1;
    for (int v = 0; v < V; v++) {
        if (!sptSet[v] && dist[v] <= min) {
            min = dist[v];
            min_index = v;
        }
    }
    return min_index;
}

void dijkstra(int graph[V][V], int src) {
    int dist[V];
    int sptSet[V];
    
    for (int i = 0; i < V; i++) {
        dist[i] = INT_MAX;
        sptSet[i] = 0;
    }
    dist[src] = 0;
    
    for (int count = 0; count < V - 1; count++) {
        int u = minDistance(dist, sptSet);
        if (u == -1) break;
        sptSet[u] = 1;
        for (int v = 0; v < V; v++) {
            if (!sptSet[v] && graph[u][v] && dist[u] + graph[u][v] < dist[v]) {
                dist[v] = dist[u] + graph[u][v];
            }
        }
    }
}

void generateGraph(int graph[V][V]) {
    srand(0);
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            graph[i][j] = (i != j) ? (rand() % 10 + 1) : 0;
        }
    }
}

// ---------------------
//Fibonacci
// ---------------------
int fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

// ---------------------
// 100MB file 
// ---------------------
void fileIOTest(const char* filename, int sizeMB) {
    FILE *f = fopen(filename, "wb");
    if (f == NULL) return;
    
    char *buffer = (char*)malloc(1024 * 1024);
    memset(buffer, 'A', 1024 * 1024);
    
    for (int i = 0; i < sizeMB; i++) {
        fwrite(buffer, 1, 1024 * 1024, f);
    }
    fclose(f);
    
    f = fopen(filename, "rb");
    if (f == NULL) {
        free(buffer);
        return;
    }
    for (int i = 0; i < sizeMB; i++) {
        fread(buffer, 1, 1024 * 1024, f);
    }
    fclose(f);
    free(buffer);
}


int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s [dijkstra|fibonacci|io]\n", argv[0]);
        return 1;  
    }
    const char *task = argv[1];
    if (strcmp(task, "dijkstra") == 0) {
        int graph[V][V];
        generateGraph(graph);
        for (int i = 0; i < 3; i++) {
            dijkstra(graph, 0);
        }
    } else if (strcmp(task, "fibonacci") == 0) {
        for (int i = 0; i < 3; i++) {
            fibonacci(35);
        }
    } else if (strcmp(task, "io") == 0) {
        for (int i = 0; i < 3; i++) {
            fileIOTest("test_c_io.dat", 100);
        }
    } else {
        fprintf(stderr, "Unknown task: %s. Use dijkstra, fibonacci or io.\n", task);
        return 1;  
    }
    return 0;
}
