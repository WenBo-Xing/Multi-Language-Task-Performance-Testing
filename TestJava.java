import java.io.*;
import java.util.*;

public class TestJava {

    // ---------------------
    // Dijkstra
    // ---------------------
    static final int V = 100;

    int minDistance(int[] dist, boolean[] sptSet) {
        int min = Integer.MAX_VALUE, min_index = -1;
        for (int v = 0; v < V; v++) {
            if (!sptSet[v] && dist[v] <= min) {
                min = dist[v];
                min_index = v;
            }
        }
        return min_index;
    }

    void dijkstra(int[][] graph, int src) {
        int[] dist = new int[V];
        boolean[] sptSet = new boolean[V];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[src] = 0;
        // main loop ,update U
        for (int count = 0; count < V - 1; count++) {
            int u = minDistance(dist, sptSet);
            if (u == -1) break;
            sptSet[u] = true;
            for (int v = 0; v < V; v++) {
                if (!sptSet[v] && graph[u][v] != 0 && dist[u] + graph[u][v] < dist[v]) {
                    dist[v] = dist[u] + graph[u][v];
                }
            }
        }
    }

    int[][] generateGraph() {
        Random rand = new Random(0);
        int[][] graph = new int[V][V];
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                graph[i][j] = (i != j) ? rand.nextInt(10) + 1 : 0;
            }
        }
        return graph;
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
    void fileIOTest(String filename, int sizeMB) {
        byte[] buffer = new byte[1024 * 1024];
        Arrays.fill(buffer, (byte) 'A');
        try (FileOutputStream fos = new FileOutputStream(filename)) {
            for (int i = 0; i < sizeMB; i++) {
                fos.write(buffer);
                fos.flush();  //each upload 1mb, flush
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        try (FileInputStream fis = new FileInputStream(filename)) {
            for (int i = 0; i < sizeMB; i++) {
                fis.read(buffer);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // ---------------------
    // Main function
    // ---------------------
    public static void main(String[] args) {
        if (args.length < 1) {
            System.err.println("Usage: java TestJava [dijkstra|fibonacci|io]");
            return;  
        }
        String task = args[0].toLowerCase();
        TestJava test = new TestJava();
        if (task.equals("dijkstra")) {
            int[][] graph = test.generateGraph();
            for (int i = 0; i < 3; i++) {
                test.dijkstra(graph, 0);
            }
        } else if (task.equals("fibonacci")) {
            for (int i = 0; i < 3; i++) {
                test.fibonacci(35);
            }
        } else if (task.equals("io")) {
            for (int i = 0; i < 3; i++) {
                test.fileIOTest("test_java_io.dat", 100);
            }
        } else {
            System.err.println("Unknown task: " + args[0]);
            System.exit(1);  
        }
       
    }
}
