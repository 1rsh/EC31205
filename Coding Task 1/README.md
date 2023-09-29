# [Coding Task 1](/Coding%20Task%201/Coding%20Task%201%20Report.pdf)
### 1. Naive Robot Navigation Problem:
**Problem Statement:**<br>
The Naive Robot Navigation Problem involves designing a program to navigate a grid maze using a Breadth-First Search (BFS) algorithm. The robot's objective is to find the shortest navigation route while following only white tiles. The program takes into account various input parameters, including the maze configuration, starting and ending coordinates, and the option to allow or disallow diagonal movements. <br><br>
**The Code:**<br>
Refer [Naive Robot Navigation.ipynb](/Coding%20Task%201/Naive%20Robot%20Navigation.ipynb).<br>
Allowed_directions is appended to include diagonal movements if all_direction is True. Once an allowed point is visited it is added to the set and BFS is implemented until it reaches the end. 
<br><br>
**Results:**<br>
The program provides two outputs in the form of a tuple:<br>

 - **Reachability:** The first element of the tuple is a boolean value that indicates whether the endpoint is reachable from the starting point. It returns True if the endpoint is reachable and False if it is not.
- **Navigation Path:** The second element of the tuple is a list that represents the navigation plan for the robot. This list contains a sequence of coordinates representing the path from the starting point to the endpoint, considering the shortest possible route.
****
### 2. Smarter Robot Navigation Problem:
**Problem Statement:**<br>
The Smarter Robot Navigation Problem builds upon the previous Naive Robot Navigation Problem by considering the loss of speed due to changing directions. The objective is to find the shortest navigation route for a robot navigating a grid maze while taking into account the overhead costs associated with different degrees of turns. The program should use Dijkstra's shortest path algorithm to determine the optimal route.
<br>
<br>
Refer [Smarter Robot Navigation.ipynb](/Coding%20Task%201/Smarter%20Robot%20Navigation.ipynb).
<br><br>
**Results:** <br>
We can see a difference between outputs in the bigger maze when all_directions are allowed using the naive and smarter robot navigation (lesser turns).
