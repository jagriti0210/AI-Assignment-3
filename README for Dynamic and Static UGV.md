UGV PATH PLANNING USING A* ALGORITHM

1. INTRODUCTION
   In this work, a path planning method is implemented for an Unmanned Ground Vehicle (UGV). The objective is to move from a given start position to a goal position in a grid while avoiding obstacles and finding the shortest possible path.

Two situations are considered:
(i) Obstacles are known beforehand (static case)
(ii) Obstacles may appear during movement (dynamic case)

---

2. METHOD USED
   The A* (A-star) algorithm is used for path finding. It is chosen because it is efficient and gives the shortest path when a suitable heuristic is used.

The heuristic used in this problem is the Manhattan distance.

---

3. ENVIRONMENT REPRESENTATION
   The environment is represented as a grid (for example 20×20 or 70×70).
   Each cell in the grid represents:
   0 → free space
   1 → obstacle

The vehicle is allowed to move in four directions:
up, down, left, and right.

---

4. STATIC OBSTACLE CASE
   In this case, all obstacles are known before the algorithm starts.

Steps:

1. Generate a grid with obstacles using a chosen density
2. Define start and goal positions
3. Apply A* algorithm
4. Trace the path from start to goal

The algorithm finds the shortest path if it exists.

---

5. DYNAMIC OBSTACLE CASE
   In real-world situations, obstacles may not be known in advance and can appear during movement.

Steps:

1. Start from the initial position
2. Compute path using A*
3. Move step by step along the path
4. If a new obstacle appears:

   * Update the grid
   * Recompute path from current position
5. Continue until the goal is reached or no path is available

This approach is called replanning.

---

6. MEASURES OF EFFECTIVENESS
   The performance of the system can be evaluated using:

* Path length (number of steps taken)
* Time required to compute the path
* Number of nodes explored
* Whether the goal is reached successfully
* Optimality of the path

---

7. PROGRAM FILES
   
   astar_static.py – Implementation for static obstacles using A*
   
   UGV_dynamic.py – Implementation for dynamic obstacles with replanning
---

8. CONCLUSION
   The implementation shows how the A* algorithm can be used to find optimal paths in a grid. It also demonstrates how replanning helps in handling dynamic environments where obstacles are not fixed. This is useful in real-world applications such as robotics and autonomous navigation.

---
