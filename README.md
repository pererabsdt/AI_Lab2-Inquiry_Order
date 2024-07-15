# United Household Customer Service System

This project is part of a group assignment to develop a customer service system for United Household, a multi-national company. The system tracks customer inquiries in a tree structure, where each node represents an inquiry, and its sub-nodes represent follow-up inquiries. The goal is to find the quickest way to respond to all customer inquiries, ensuring that the earliest inquiries are answered first.

## Algorithm Selection

The suitable algorithm for systematically processing and responding to customer inquiries in the order they were received is **Breadth-first search (BFS)**. BFS processes nodes level by level, ensuring that we address the earliest inquiries before moving on to follow-up inquiries.

## Project Structure

- `input.txt`: Contains the input tree structure of inquiries.
- `bfs_inquiries.py`: The Python script that reads the input file and performs BFS to determine the order of inquiries.
- `README.md`: Documentation for the project.

## Input Format

The input file `input.txt` contains the tree structure in the following format:
  'root': ['A', 'B'],
  'A': ['C', 'D'],
  'B': ['E'],
  'C': [],
  'D': [],
  'E': []

## Output

The output will be a list representing the order in which inquiries should be processed:
  ['root', 'A', 'B', 'C', 'D', 'E']


## Usage

1. Ensure you have Python installed on your system.
2. Place your input file `input.txt` in the same directory as the script.
3. Run the script:

