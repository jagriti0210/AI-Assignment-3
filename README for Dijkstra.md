# Dijkstra Algorithm using CSV Data

This project implements Dijkstra’s algorithm to find the shortest path between cities using road distance data stored in a CSV file.

## Description

The program reads a CSV file containing city connections in the format:

source, destination, distance

Each row represents a road between two cities along with the distance between them. The graph is treated as undirected.

Using this data, the program constructs a graph and applies Dijkstra’s algorithm to compute the shortest distance from a user-specified source city to all other cities.

## Files

* Indian_cities.csv
  Contains the list of cities and distances between them.

* Dijkstra.py
  Python implementation of Dijkstra’s algorithm.

## How It Works

1. The CSV file is read using Python’s csv module.
2. A graph is created using adjacency list representation.
3. Dijkstra’s algorithm is applied to compute shortest paths.
4. The shortest distances from the selected source city are displayed.

## How to Run

1. Make sure both files are in the same folder.

2. Open terminal in that folder.

3. Run:

   python Dijkstra.py

4. Enter the source city when prompted.

## Example

Input:
Delhi

Output:
Delhi -> 0 km
Mumbai -> 1400 km
Jaipur -> 280 km

## Notes

* The graph is treated as undirected.
* Distances are approximate.
* More cities can be added by editing the CSV file.

## Conclusion

This implementation shows how Dijkstra’s algorithm can be applied to real-world datasets using a simple CSV-based approach.
