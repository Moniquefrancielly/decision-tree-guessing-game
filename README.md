# Decision Tree Guessing Game 

A guessing game in Python, simplified and inspired by the Akinator concept.
The system uses a **binary decision tree** where each node represents a question and each branch represents a possible answer ("yes" or "no"). By navigating the tree, the program attempts to guess what the user is thinking about.

The project demonstrates two fundamental tree traversal algorithms:
* **Breadth-First Search (BFS)**
* **Depth-First Search (DFS)**
These algorithms are implemented to analyze how different traversal strategies explore the same decision structure.

# Project Objectives
The main goals of this project are:

* Implement a **decision tree data structure**
* Apply **tree traversal algorithms (BFS and DFS)**
* Simulate a **guessing game based on yes/no questions**
* Compare the behavior and exploration order of different search strategies

# Decision Tree Structure
In this system:

* **Internal nodes** represent questions
* **Leaf nodes** represent final guesses
  
The program navigates through this tree until it reaches a final answer.

Example decision tree used in the project:

                 Is it a savory dish?
                 /                \
               Yes                 No
               /                    \
        Does it contain dough?    Is it cold?
           /        \             /        \
        Pizza      Sushi       Ice cream   Brownie

# Algorithms Implemented Information
## Breadth-First Search (BFS)
BFS explores the tree **level by level**, visiting all nodes at the same depth before moving deeper.
Characteristics:
* Uses a **queue**
* Explores nodes in breadth order

## Depth-First Search (DFS)
DFS explores **one branch completely before backtracking**.
Characteristics:
* Uses **recursion or a stack**
* Goes deep before exploring siblings

# Example Output
Example game interaction:
Example output will be added after the game implementation.

# Technologies
* Python
* Tree data structures
* BFS algorithm
* DFS algorithm
* Git & GitHub
