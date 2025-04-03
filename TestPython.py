import sys
import time
import random
import os

# ---------------------
# Dijkstra 
# ---------------------
def dijkstra(graph, src):
    V = len(graph)
    dist = [sys.maxsize] * V
    sptSet = [False] * V
    dist[src] = 0
    for _ in range(V - 1):
       
        u = min((v for v in range(V) if not sptSet[v]), key=lambda v: dist[v], default=-1)
        if u == -1:
            break
        sptSet[u] = True
        # update U
        for v in range(V):
            if graph[u][v] and not sptSet[v] and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]

# ---------------------
# ② Fibonacci 
# ---------------------
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# ---------------------
# 100 Mb file 
# ---------------------
def file_io_test(filename="test_python_io.dat", size_mb=100):
    data = os.urandom(size_mb * 1024 * 1024)       # random data 
    with open(filename, "wb") as f:
        f.write(data)
        f.flush()           
        os.fsync(f.fileno())  
    with open(filename, "rb") as f:
        _ = f.read()        

#
def generate_graph(v=100):
    random.seed(0)
    return [[random.randint(1, 10) if i != j else 0 for j in range(v)] for i in range(v)]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python3 {sys.argv[0]} [dijkstra|fibonacci|io]")
        sys.exit(1)
    task = sys.argv[1].lower()
    if task == "dijkstra":
        graph = generate_graph(100)
        for _ in range(3):
            dijkstra(graph, 0)
    elif task == "fibonacci":
        for _ in range(3):
            fibonacci(35)
    elif task == "io":
        for _ in range(3):
            file_io_test("test_python_io.dat", 100)
    else:
        print(f"Unknown task: {sys.argv[1]}")
        sys.exit(1)



