Q1- Write a C program to implement Quick Sort algorithm.
Introduction: Quick Sort is a popular sorting algorithm known for its efficiency and is often used in various applications. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.
Code: 
#include <stdio.h>

int partition(int arr[], int low, int high) {
    int pivot = arr[high]; 
    int i = low - 1;  
    for (int j = low; j < high; j++) {
    
        if (arr[j] <= pivot) {
            i++;
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }

    int temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;

    return i + 1;
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {

        int pivotIndex = partition(arr, low, high);

        quickSort(arr, low, pivotIndex - 1);
        quickSort(arr, pivotIndex + 1, high);
    }
}

// Function to print an array
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int arrSize;

    printf("Enter the size of the array: ");
    scanf("%d", &arrSize);

    int arr[arrSize];

    printf("Enter the elements of the array:\n");
    for (int i = 0; i < arrSize; i++) {
        scanf("%d", &arr[i]);
    }

    printf("Original array: ");
    printArray(arr, arrSize);
    quickSort(arr, 0, arrSize - 1);
    printf("Sorted array: ");
    printArray(arr, arrSize);

    return 0;
}











Q2- Write a C program to solve the Tower of Hanoi problem using Recursion.
Introduction: The Tower of Hanoi is a classic problem in computer science and mathematics. It involves three pegs and a number of disks of different sizes. The puzzle starts with the disks in a neat stack in ascending order of size on one peg, the smallest at the top, thus making a conical shape.
Code: 
#include <stdio.h>

// Function to solve Tower of Hanoi problem
void towerOfHanoi(int n, char source, char auxiliary, char destination) {
    if (n == 1) {
        printf("Move disk 1 from %c to %c\n", source, destination);
        return;
    }
    towerOfHanoi(n - 1, source, destination, auxiliary);
    printf("Move disk %d from %c to %c\n", n, source, destination);
    towerOfHanoi(n - 1, auxiliary, source, destination);
}

int main() {
    int n;
    printf("Enter the number of disks: ");
    scanf("%d", &n);
    towerOfHanoi(n, 'A', 'B', 'C');
    return 0;
}






Q3- Write a C program to solve N-Queens problem.
Introduction: The N-Queens problem is a classic problem in which you have to place N chess queens on an N×N chessboard in such a way that no two queens threaten each other.
Code: 
#include <stdio.h>
#include <stdbool.h>

#define N 10

// Function to print the chessboard
void printSolution(int board[N][N], int queens) {
    printf("Solution exists:\n");
    for (int i = 0; i < queens; i++) {
        for (int j = 0; j < queens; j++) {
            printf("%2d ", board[i][j]);
        }
        printf("\n");
    }
}

// Function to check if a queen can be placed on board[row][col]
bool isSafe(int board[N][N], int row, int col, int queens) {
    for (int i = 0; i < col; i++)
        if (board[row][i])
            return false;
    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--)
        if (board[i][j])
            return false;
    for (int i = row, j = col; i < queens && j >= 0; i++, j--)
        if (board[i][j])
            return false;

    return true;
}

// Recursive function to solve N-Queens problem
bool solveNQueensUtil(int board[N][N], int col, int queens) {
    if (col >= queens)
        return true;

    for (int i = 0; i < queens; i++) {
        if (isSafe(board, i, col, queens)) {
            board[i][col] = 1;

            if (solveNQueensUtil(board, col + 1, queens))
                return true;

            board[i][col] = 0; 
        }
    }

    return false;
}

// Function to solve the N-Queens problem
void solveNQueens(int queens) {
    int board[N][N] = {0};

    if (solveNQueensUtil(board, 0, queens)) {
        printSolution(board, queens);
    } else {
        printf("Solution does not exist.\n");
    }
}

int main() {
    int queens;

    printf("Enter the number of queens: ");
    scanf("%d", &queens);

    solveNQueens(queens);

    return 0;
}





Q4- Write a C program to implement graph traversal using BFS.
Introduction: Graph traversal is a fundamental operation in graph theory, allowing us to explore and visit each vertex in a graph. Breadth-First Search (BFS) is one such traversal algorithm that starts from a specified vertex and explores its neighbors before moving on to the next level of vertices. It utilizes a queue data structure to maintain the order of exploration.
Code: 
#include <stdio.h>
#include <stdlib.h>
#define MAX_VERTICES 100
struct Queue {
    int front, rear;
    int capacity;
    int* array;
};

// Function to create a new queue
struct Queue* createQueue(int capacity) {
    struct Queue* queue = (struct Queue*)malloc(sizeof(struct Queue));
    queue->capacity = capacity;
    queue->front = queue->rear = -1;
    queue->array = (int*)malloc(queue->capacity * sizeof(int));
    return queue;
}

// Function to check if the queue is empty
int isEmpty(struct Queue* queue) {
    return queue->front == -1;
}

// Function to enqueue an element to the queue
void enqueue(struct Queue* queue, int item) {
    if (isEmpty(queue))
        queue->front = 0;
    queue->rear++;
    queue->array[queue->rear] = item;
}

// Function to dequeue an element from the queue
int dequeue(struct Queue* queue) {
    int item = queue->array[queue->front];
    queue->front++;
    if (queue->front > queue->rear)
        queue->front = queue->rear = -1;
    return item;
}

// Function to perform BFS traversal on the graph
void BFS(int graph[MAX_VERTICES][MAX_VERTICES], int vertices, int startVertex) {
    struct Queue* queue = createQueue(vertices);
    int visited[MAX_VERTICES] = {0};

    // Mark the starting vertex as visited and enqueue it
    visited[startVertex] = 1;
    enqueue(queue, startVertex);

    printf("Breadth-First Search (BFS) starting from vertex %d:\n", startVertex);

    while (!isEmpty(queue)) {
        int currentVertex = dequeue(queue);
        printf("%d ", currentVertex);

        // Explore all adjacent vertices of the current vertex
        for (int i = 0; i < vertices; i++) {
            if (graph[currentVertex][i] && !visited[i]) {
                visited[i] = 1;
                enqueue(queue, i);
            }
        }
    }

    printf("\n");
}

int main() {
    int vertices, edges;
    printf("Enter the number of vertices and edges: ");
    scanf("%d %d", &vertices, &edges);

    int graph[MAX_VERTICES][MAX_VERTICES] = {0};

    printf("Enter the edges (format: vertex1 vertex2):\n");
    for (int i = 0; i < edges; i++) {
        int vertex1, vertex2;
        scanf("%d %d", &vertex1, &vertex2);
        graph[vertex1][vertex2] = 1;
        graph[vertex2][vertex1] = 1; // Assuming an undirected graph
    }

    int startVertex;
    printf("Enter the starting vertex for BFS: ");
    scanf("%d", &startVertex);

    BFS(graph, vertices, startVertex);

    return 0;
}










Q5- Write a C program to implement graph traversal using DFS.
Introduction: Depth-First Search (DFS) is another graph traversal algorithm that explores as far as possible along each branch before backtracking. It can be implemented using a recursive approach or using a stack data structure.
Code: 
#include <stdio.h>
#include <stdlib.h>

#define MAX_VERTICES 100

// Function to perform DFS traversal on the graph
void DFS(int graph[MAX_VERTICES][MAX_VERTICES], int vertices, int currentVertex, int visited[]) {
    printf("%d ", currentVertex);
    visited[currentVertex] = 1;

    // Explore all adjacent vertices of the current vertex
    for (int i = 0; i < vertices; i++) {
        if (graph[currentVertex][i] && !visited[i]) {
            DFS(graph, vertices, i, visited);
        }
    }
}

int main() {
    int vertices, edges;
    printf("Enter the number of vertices and edges: ");
    scanf("%d %d", &vertices, &edges);

    int graph[MAX_VERTICES][MAX_VERTICES] = {0};

    printf("Enter the edges (format: vertex1 vertex2):\n");
    for (int i = 0; i < edges; i++) {
        int vertex1, vertex2;
        scanf("%d %d", &vertex1, &vertex2);
        graph[vertex1][vertex2] = 1;
        graph[vertex2][vertex1] = 1; // Assuming an undirected graph
    }

    int startVertex;
    printf("Enter the starting vertex for DFS: ");
    scanf("%d", &startVertex);

    int visited[MAX_VERTICES] = {0};

    printf("Depth-First Search (DFS) starting from vertex %d:\n", startVertex);
    DFS(graph, vertices, startVertex, visited);

    return 0;
}

Output: 

 


Remarks: In fulfillment of the lab requirements, the provided C program implements graph traversal using DFS.

















Q6- Write a C program to implement Prim’s algorithm using greedy method.
Introduction: Prim's algorithm is a greedy algorithm that finds a minimum spanning tree for a weighted, connected graph. It starts with an arbitrary node and grows the spanning tree one node at a time by adding the cheapest possible connection from the tree to a new node.

Code: 
#include <stdio.h>
#include <limits.h>

#define V 5  // Number of vertices in the graph

// Function to find the vertex with the minimum key value, which is not yet included in the minimum spanning tree
int minKey(int key[], int mstSet[]) {
    int min = INT_MAX, min_index;

    for (int v = 0; v < V; v++) {
        if (!mstSet[v] && key[v] < min) {
            min = key[v];
            min_index = v;
        }
    }

    return min_index;
}

// Function to print the constructed MST stored in parent[]
void printMST(int parent[], int graph[V][V]) {
    printf("Edge \tWeight\n");
    for (int i = 1; i < V; i++)
        printf("%d - %d \t%d \n", parent[i], i, graph[i][parent[i]]);
}

// Function to construct and print the MST for a graph represented using adjacency matrix representation
void primMST(int graph[V][V]) {
    int parent[V];  // Array to store constructed MST
    int key[V];     // Key values used to pick the minimum weight edge
    int mstSet[V];  // To represent the set of vertices included in MST

    // Initialize all keys as INFINITE
    // Set all vertices to not be in MST yet
    for (int i = 0; i < V; i++) {
        key[i] = INT_MAX;
        mstSet[i] = 0;
    }

    // Always include the first vertex in MST
    key[0] = 0;
    parent[0] = -1; // First node is always the root of MST

    // The MST will have V-1 edges
    for (int count = 0; count < V - 1; count++) {
        // Pick the minimum key vertex from the set of vertices not yet included in MST
        int u = minKey(key, mstSet);

        // Include the picked vertex in MST
        mstSet[u] = 1;

        // Update key value and parent index of the adjacent vertices of the picked vertex
        for (int v = 0; v < V; v++) {
            if (graph[u][v] && !mstSet[v] && graph[u][v] < key[v]) {
                parent[v] = u;
                key[v] = graph[u][v];
            }
        }
    }

    // Print the constructed MST
    printMST(parent, graph);
}

int main() {
    // Sample input for a graph represented using an adjacency matrix
    int graph[V][V] = {
        {0, 2, 0, 6, 0},
        {2, 0, 3, 8, 5},
        {0, 3, 0, 0, 7},
        {6, 8, 0, 0, 9},
        {0, 5, 7, 9, 0}
    };

    // Print the MST using Prim's algorithm
    primMST(graph);

    return 0;
}

Output:  

Remarks: Prim’s algorithm using greedy method is implemented.

Q7- Write a C program to implement Kruskal’s algorithm using greedy method.
Introduction: Kruskal's algorithm is another greedy algorithm used for finding a minimum spanning tree in a connected, undirected graph. It starts by sorting all the edges in non-decreasing order of their weights and then selects edges in ascending order until a minimum spanning tree is formed. The algorithm ensures that adding an edge to the growing spanning tree doesn't form a cycle.

Code: 
#include <stdio.h>
#include <stdlib.h>

// Structure to represent an edge in the graph
struct Edge {
    int src, dest, weight;
};

// Structure to represent a subset for union-find
struct Subset {
    int parent, rank;
};

// Function to find the set of an element 'i'
int find(struct Subset subsets[], int i) {
    if (subsets[i].parent != i)
        subsets[i].parent = find(subsets, subsets[i].parent);

    return subsets[i].parent;
}

// Function to perform union of two subsets
void unionSets(struct Subset subsets[], int x, int y) {
    int xroot = find(subsets, x);
    int yroot = find(subsets, y);

    if (subsets[xroot].rank < subsets[yroot].rank)
        subsets[xroot].parent = yroot;
    else if (subsets[xroot].rank > subsets[yroot].rank)
        subsets[yroot].parent = xroot;
    else {
        subsets[yroot].parent = xroot;
        subsets[xroot].rank++;
    }
}

// Comparison function for sorting edges based on their weights
int compare(const void* a, const void* b) {
    return ((struct Edge*)a)->weight - ((struct Edge*)b)->weight;
}

// Function to find and print the minimum spanning tree using Kruskal's algorithm
void kruskalMST(struct Edge edges[], int V, int E) {
    struct Edge result[V];  // Array to store the result (minimum spanning tree)
    int e = 0;              // An index variable used for the result array
    int i = 0;              // An index variable used for sorted edges

    // Step 1: Sort all the edges in non-decreasing order of their weight
    qsort(edges, E, sizeof(edges[0]), compare);

    // Allocate memory for creating V subsets with single elements
    struct Subset* subsets = (struct Subset*)malloc(V * sizeof(struct Subset));

    // Create V subsets with single elements
    for (int v = 0; v < V; v++) {
        subsets[v].parent = v;
        subsets[v].rank = 0;
    }

    // Number of edges to be taken is equal to V-1
    while (e < V - 1 && i < E) {
        // Step 2: Pick the smallest edge. Increment index for the next iteration.
        struct Edge next_edge = edges[i++];

        int x = find(subsets, next_edge.src);
        int y = find(subsets, next_edge.dest);

        // If including this edge doesn't cause a cycle, add it to the result
        if (x != y) {
            result[e++] = next_edge;
            unionSets(subsets, x, y);
        }
        // Else discard the next_edge
    }

    // Print the constructed minimum spanning tree
    printf("Edges in the Minimum Spanning Tree:\n");
    for (i = 0; i < e; i++)
        printf("%d - %d : %d\n", result[i].src, result[i].dest, result[i].weight);

    free(subsets);
}

int main() {
    // Sample input for a graph represented using edges and their weights
    int V = 4; // Number of vertices
    int E = 5; // Number of edges
    struct Edge edges[] = {
        {0, 1, 10},
        {0, 2, 6},
        {0, 3, 5},
        {1, 3, 15},
        {2, 3, 4}
    };

    // Print the Minimum Spanning Tree using Kruskal's algorithm
    kruskalMST(edges, V, E);

    return 0;
}


Output:  

Remarks: Kruskal’s algorithm using greedy method is implemented. 





















Q8- Write a C program to implement Graph coloring method.
Introduction: Graph coloring is a problem of assigning colors to the vertices of a graph in such a way that no two adjacent vertices share the same color. It is a classical problem with applications in scheduling, register allocation in compilers, and various other areas. One popular algorithm for graph coloring is the Greedy Coloring algorithm.
Code:
#include <stdio.h>
#include <stdlib.h>

#define MAX_VERTICES 100

// Function to print the colors assigned to vertices
void printColors(int colors[], int vertices) {
    printf("Vertex Colors:\n");
    for (int i = 0; i < vertices; i++)
        printf("Vertex %d -> Color %d\n", i, colors[i]);
}

// Function to check if it's safe to color the vertex with the given color
int isSafe(int vertex, int graph[MAX_VERTICES][MAX_VERTICES], int vertices, int color[], int c) {
    for (int i = 0; i < vertices; i++) {
        if (graph[vertex][i] && color[i] == c)
            return 0;
    }
    return 1;
}

// Function to perform graph coloring using Greedy Coloring algorithm
void graphColoring(int graph[MAX_VERTICES][MAX_VERTICES], int vertices, int m) {
    int colors[MAX_VERTICES];
    for (int i = 0; i < vertices; i++)
        colors[i] = -1; // Initialize all vertices as uncolored

    // Assign the first color to the first vertex
    colors[0] = 0;

    // Assign colors to remaining vertices
    for (int vertex = 1; vertex < vertices; vertex++) {
        for (int c = 0; c < m; c++) {
            if (isSafe(vertex, graph, vertices, colors, c)) {
                colors[vertex] = c;
                break;
            }
        }
    }

    // Print the colors assigned to vertices
    printColors(colors, vertices);
}

int main() {
    int vertices, edges, m;

    printf("Enter the number of vertices and edges: ");
    scanf("%d %d", &vertices, &edges);

    int graph[MAX_VERTICES][MAX_VERTICES] = {0};

    printf("Enter the edges (format: vertex1 vertex2):\n");
    for (int i = 0; i < edges; i++) {
        int vertex1, vertex2;
        scanf("%d %d", &vertex1, &vertex2);
        graph[vertex1][vertex2] = 1;
        graph[vertex2][vertex1] = 1; // Assuming an undirected graph
    }

    printf("Enter the number of colors available: ");
    scanf("%d", &m);

    graphColoring(graph, vertices, m);

    return 0;
}

Output:  

Remarks: Graph coloring method is implemented in c. 



Q9- Write a C program to implement All Pair Shortest Path algorithm
Introduction: The All Pairs Shortest Path algorithm is a dynamic programming approach that finds the shortest paths between all pairs of vertices in a directed graph. One common algorithm for this purpose is the Floyd-Warshall algorithm. It considers all pairs of vertices as intermediate vertices and gradually builds the shortest paths between them.
Code: 
#include <stdio.h>
#include <limits.h>

#define V 4  // Number of vertices

// Function to print the solution matrix
void printSolution(int dist[V][V]) {
    printf("All Pairs Shortest Paths:\n");
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            if (dist[i][j] == INT_MAX)
                printf("INF\t");
            else
                printf("%d\t", dist[i][j]);
        }
        printf("\n");
    }
}

// Function to perform All Pairs Shortest Path using Floyd-Warshall algorithm
void floydWarshall(int graph[V][V]) {
    int dist[V][V];

    // Initialize the solution matrix with the input graph
    for (int i = 0; i < V; i++)
        for (int j = 0; j < V; j++)
            dist[i][j] = graph[i][j];

    // Update the solution matrix by considering all vertices as intermediate vertices
    for (int k = 0; k < V; k++) {
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                if (dist[i][k] != INT_MAX && dist[k][j] != INT_MAX && dist[i][k] + dist[k][j] < dist[i][j])
                    dist[i][j] = dist[i][k] + dist[k][j];
            }
        }
    }

    // Print the solution matrix
    printSolution(dist);
}

int main() {
    // Sample input for a weighted directed graph represented using an adjacency matrix
    int graph[V][V] = {
        {0, 5, INT_MAX, 10},
        {INT_MAX, 0, 3, INT_MAX},
        {INT_MAX, INT_MAX, 0, 1},
        {INT_MAX, INT_MAX, INT_MAX, 0}
    };

    // Perform All Pairs Shortest Path using Floyd-Warshall algorithm
    floydWarshall(graph);

    return 0;
}

Output:
 

Remarks: All Pair Shortest Path algorithm is implemented in C.















Q10- Write a C program to solve knapsack problem using Greedy method.
Introduction: The Knapsack Problem is a classic optimization problem where the goal is to select items from a set, each with a weight and a value, to maximize the total value while not exceeding a given weight capacity. The Greedy method for the Knapsack Problem involves sorting the items based on their value-to-weight ratio and selecting items in descending order of this ratio until the capacity is reached.
Code:
#include <stdio.h>

#define MAX_ITEMS 100

// Structure to represent an item
struct Item {
    int weight;
    int value;
};

// Function to compare items based on their value-to-weight ratio (for qsort)
int compareItems(const void* a, const void* b) {
    double ratioA = ((double)((struct Item*)a)->value) / ((struct Item*)a)->weight;
    double ratioB = ((double)((struct Item*)b)->value) / ((struct Item*)b)->weight;
    return (ratioB - ratioA); // Sort in descending order of value-to-weight ratio
}

// Function to solve the Knapsack Problem using the Greedy method
void knapsackGreedy(struct Item items[], int n, int capacity) {
    // Sort items based on their value-to-weight ratio
    qsort(items, n, sizeof(struct Item), compareItems);

    int currentWeight = 0; // Current weight in the knapsack
    double totalValue = 0.0; // Total value obtained

    // Select items in descending order of value-to-weight ratio
    for (int i = 0; i < n; i++) {
        if (currentWeight + items[i].weight <= capacity) {
            // Include the whole item if it fits in the knapsack
            currentWeight += items[i].weight;
            totalValue += items[i].value;
        } else {
            // Include a fraction of the item if it doesn't fit completely
            int remainingWeight = capacity - currentWeight;
            totalValue += (double)remainingWeight * items[i].value / items[i].weight;
            break;
        }
    }

    // Print the total value obtained
    printf("Maximum value obtained: %.2lf\n", totalValue);
}

int main() {
    int n, capacity;

    printf("Enter the number of items: ");
    scanf("%d", &n);

    struct Item items[MAX_ITEMS];

    printf("Enter the weight and value of each item:\n");
    for (int i = 0; i < n; i++) {
        printf("Item %d: ", i + 1);
        scanf("%d %d", &items[i].weight, &items[i].value);
    }

    printf("Enter the knapsack capacity: ");
    scanf("%d", &capacity);

    // Solve the Knapsack Problem using Greedy method
    knapsackGreedy(items, n, capacity);

    return 0;
}

Output:  

Remarks: Knapsack problem using Greedy method is implemented in C.









Q11- Write a C program to solve Travelling salesman problem.
Introduction: The Traveling Salesman Problem (TSP) is a classic optimization problem where the objective is to find the shortest possible tour that visits a given set of cities and returns to the starting city. It is an NP-hard problem, and there are various approaches to solving it.
Code: 
#include <stdio.h>
#include <stdlib.h>

#define MAX_CITIES 10
#define INF 999999

// Function to swap the values at two pointers
void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Function to reverse the array from start to end
void reverse(int arr[], int start, int end) {
    while (start < end) {
        swap(&arr[start], &arr[end]);
        start++;
        end--;
    }
}

// Function to generate the next lexicographically greater permutation
int nextPermutation(int arr[], int n) {
    int i = n - 2;
    while (i >= 0 && arr[i] >= arr[i + 1])
        i--;

    if (i < 0)
        return 0; // No next permutation is possible

    int j = n - 1;
    while (arr[j] <= arr[i])
        j--;

    swap(&arr[i], &arr[j]);
    reverse(arr, i + 1, n - 1);

    return 1; // Next permutation generated successfully
}

// Function to calculate the total distance of a tour
int calculateTourDistance(int tour[], int graph[MAX_CITIES][MAX_CITIES], int numCities) {
    int distance = 0;
    for (int i = 0; i < numCities - 1; i++) {
        if (graph[tour[i]][tour[i + 1]] == INF) {
            // If there is no direct connection, the tour is not valid
            return INF;
        }
        distance += graph[tour[i]][tour[i + 1]];
    }
    // Add the distance from the last city back to the starting city
    distance += graph[tour[numCities - 1]][tour[0]];
    return distance;
}

// Function to find the minimum tour using the brute-force approach
void tspBruteForce(int graph[MAX_CITIES][MAX_CITIES], int numCities) {
    int tour[MAX_CITIES];
    for (int i = 0; i < numCities; i++) {
        tour[i] = i; // Initialize the tour with the default order of cities
    }

    int minDistance = INF;
    int minTour[MAX_CITIES];

    // Generate all possible permutations of the cities
    do {
        int currentDistance = calculateTourDistance(tour, graph, numCities);
        if (currentDistance < minDistance) {
            // Update the minimum tour if a shorter one is found
            minDistance = currentDistance;
            for (int i = 0; i < numCities; i++) {
                minTour[i] = tour[i];
            }
        }
    } while (nextPermutation(tour, numCities));

    // Print the optimal tour and its distance
    printf("Optimal Tour: ");
    for (int i = 0; i < numCities; i++) {
        printf("%d ", minTour[i]);
    }
    printf("\nOptimal Tour Distance: %d\n", minDistance);
}

int main() {
    int numCities;

    printf("Enter the number of cities: ");
    scanf("%d", &numCities);

    int graph[MAX_CITIES][MAX_CITIES];

    // Input the distance matrix representing connections between cities
    printf("Enter the distance matrix (INF for no direct connection):\n");
    for (int i = 0; i < numCities; i++) {
        for (int j = 0; j < numCities; j++) {
            scanf("%d", &graph[i][j]);
            if (graph[i][j] == 0) {
                // Assuming 0 distance means no direct connection
                graph[i][j] = INF;
            }
        }
    }

    // Solve the Traveling Salesman Problem using brute-force approach
    tspBruteForce(graph, numCities);

    return 0;
}

Output: 
 

Remarks: Travelling salesman problem is implemented in C. 
