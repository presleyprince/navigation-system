# Intro-to-AI-Assignment-2A: Tree-Based Search Algorithms

**COS30019 Introduction to Artificial Intelligence**  
**Assignment 2A – Tree Based Search**

## Team Information

**Group 4:**
- Viresh Joshi (105910175)
- Presley Prince (105352641)
- Kyle Perry (105911291)
- Jake Hardy (105921038)

---

## Project Overview

This project implements tree-based search algorithms to solve the Route Finding Problem. The program searches for optimal (lowest cost) paths between an origin node and destination nodes on a 2D graph. Both informed and uninformed search methods have been implemented.

**Implemented Algorithms:**
- **BFS** - Breadth-First Search (uninformed)
- **DFS** - Depth-First Search (uninformed)
- **GBFS** - Greedy Best-First Search (informed)
- **A\*** - A Star Search (informed)
- **CUS1** - Beam Search (custom uninformed)
- **CUS2** - Dijkstra's Algorithm (custom informed)

---

## How to Run the Program

### Opening Terminal

**Windows:** 
- Press `Win + R`, type `cmd` and press Enter.

**Mac:** 
- Press `Cmd + Space`, type `terminal` and press Enter.

**Linux:** 
- Press `Ctrl + Alt + T` or search for "terminal".

---

### Running the Program

You have two options for running the program:

#### Option 1: Navigate to the Folder

Use the `cd` (change directory) command to navigate to the folder containing `search.py`:

```
cd C:\Users\name\Documents\Intro-to-AI-Assignment-2A
python search.py <filename> <method>
```

Example:
```
python search.py PathFinder-test.txt bfs
```

#### Option 2: Use Absolute Path

Run the program using absolute paths for both `search.py` and the input file:

```
python "C:\Users\name\Documents\search.py" "C:\Users\name\Documents\<filename>" <method>
```

Example:
```
python "C:\Users\name\Documents\Intro-to-AI-Assignment-2A\search.py" "C:\Users\name\Documents\Intro-to-AI-Assignment-2A\PathFinder-test.txt" bfs
```

---

## Parameters

### Filename
- **Requirement:** Only correctly formatted files will work
- The file must follow the specified format with Nodes, Edges, Origin, and Destinations sections

### Method
The method parameter allows the following values:

| Method | Algorithm | Type |
|--------|-----------|------|
| `bfs` | Breadth-First Search | Uninformed |
| `dfs` | Depth-First Search | Uninformed |
| `gbfs` | Greedy Best-First Search | Informed |
| `as` | A\* Search | Informed |
| `cus1` | Beam Search | Uninformed (Custom) |
| `cus2` | Dijkstra's Algorithm | Informed (Custom) |

---

## Command Format Explanation

In the command `python search.py <filename> <method>`:

- **`python`** - Executes a Python script
- **`search.py`** - The main program file that accepts parameters
- **`<filename>`** - The input file containing the graph data (nodes, edges, origin, destinations)
- **`<method>`** - The search algorithm to use for finding the path

---

## Example Usage

```
python search.py PathFinder-test.txt bfs
python search.py "Test Cases/TinyGraph.txt" as
python search.py "Test Cases/SmallDense.txt" cus2
```

---

## Output Format

The program will output:
```
<filename> <method>
<goal_node> <number_of_nodes_explored>
[<path>]
```

Example:
```
PathFinder-test.txt bfs
5 7
[2, 3, 5]
```

---

## Test Cases

The following test cases are available in the `Test Cases/` folder:
- `TinyGraph.txt` - Small graph for basic testing
- `SmallDense.txt` - Small dense graph
- `OriginAsDestination.txt` - Origin is also a destination
- `Disconnected.txt` - Graph with unreachable destinations
- `MultiDestinations.txt` - Multiple destination nodes
- `PathGraph.txt` - Path-structured graph
- `PathFinder-test-random.txt` - Randomly generated graph
- `Very Large Test.txt` - Large-scale performance test

---

## File Format

Input files must follow this format:

```
Nodes:
1: (4,1)
2: (2,2)
3: (4,4)

Edges:
(2,1): 4
(3,1): 5
(1,3): 5

Origin:
2

Destinations:
3; 4
```

---

## Notes

- Edge weights must be non-negative
- At least one destination must be specified
- The program will find a path to any one of the specified destinations
- When all else is equal, nodes are expanded in ascending order (smaller node IDs first)
- When nodes have equal priority on different branches, the chronologically earlier node is expanded first
