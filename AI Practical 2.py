"""
Assignment-A2 (A* for 8 Puzzle Problem)

Problem Statement: Problem Statement: Implement A star Algorithm for 8 puzzle problem.
"""

# This code implements A* algorithm for 8 puzzle problem since the problem
# statement in our syllabus and handout demands implementing A* algorithm 
# for any game search problem.

# A* implementation for maze problem and direct implementation can be found
# in the "Alternatives" folder.


# Enter the initial state as 9 numbers (0 represents the blank tile):
# Enter row 1 (3 numbers separated by spaces): 1 2 3
# Enter row 2 (3 numbers separated by spaces): 0 4 6
# Enter row 3 (3 numbers separated by spaces): 7 5 8

import heapq

goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

# Directions for moving the blank tile
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

def h_misplaced_tiles(state):
    misplaced = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
                misplaced += 1
    return misplaced

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def is_valid(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def state_to_tuple(state):
    return tuple(tuple(row) for row in state)

def a_star(start_state):
    start = state_to_tuple(start_state)
    g = 0
    h = h_misplaced_tiles(start_state)
    f = g + h

    # Priority queue with elements: (f, g, state, path)
    pq = [(f, g, start_state, [])]
    visited = set()

    while pq:
        f, g, current, path = heapq.heappop(pq)
        current_tuple = state_to_tuple(current)

        if current_tuple in visited:
            continue
        visited.add(current_tuple)

        if current == goal_state:
            return path + [current]

        x, y = find_blank(current)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                # Create new state by swapping blank
                new_state = [row[:] for row in current]
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]

                if state_to_tuple(new_state) not in visited:
                    new_g = g + 1
                    new_h = h_misplaced_tiles(new_state)
                    new_f = new_g + new_h
                    heapq.heappush(pq, (new_f, new_g, new_state, path + [current]))

    return None

def print_path(path):
    for step, state in enumerate(path):
        print(f"Step {step}:")
        for row in state:
            print(row)
        print()

def get_input_state():
    print("Enter the initial state as 9 numbers (0 represents the blank tile):")
    state = []
    for i in range(3):
        row = input(f"Enter row {i+1} (3 numbers separated by spaces): ").split()
        state.append([int(num) for num in row])
    return state

initial_state = get_input_state()

solution_path = a_star(initial_state)

if solution_path:
    print_path(solution_path)
else:
    print("No solution found.")

"""
SAMPLE OUTPUT

Enter the initial state as 9 numbers (0 represents the blank tile):
Enter row 1 (3 numbers separated by spaces): 1 2 3
Enter row 2 (3 numbers separated by spaces): 0 4 6
Enter row 3 (3 numbers separated by spaces): 7 5 8
Step 0:
[1, 2, 3]
[0, 4, 6]
[7, 5, 8]

Step 1:
[1, 2, 3]
[4, 0, 6]
[7, 5, 8]

Step 2:
[1, 2, 3]
[4, 5, 6]
[7, 0, 8]

Step 3:
[1, 2, 3]
[4, 5, 6]
[7, 8, 0]
"""


'''
🔢 Step-by-Step Explanation of Output:
✅ Step 0:
Initial state:

csharp
Copy
Edit
[1, 2, 3]
[0, 4, 6]
[7, 5, 8]
Move possibilities for 0: it can go right (swap with 4) or down (swap with 7). A* picks the best move based on cost.

✅ Step 1:
Moved 0 right → 4 left:

csharp
Copy
Edit
[1, 2, 3]
[4, 0, 6]
[7, 5, 8]
Getting closer to the goal by positioning 4 correctly.

✅ Step 2:
Moved 0 down → 5 up:

csharp
Copy
Edit
[1, 2, 3]
[4, 5, 6]
[7, 0, 8]
Now 5 is in place, almost solved.

✅ Step 3:
Moved 0 right → 8 left:

csharp
Copy
Edit
[1, 2, 3]
[4, 5, 6]
[7, 8, 0]
This is the goal state. Puzzle solved in 3 moves.

✅ Summary:
A* evaluated moves and chose the shortest path to the goal using a cost function.

It solved the puzzle in 3 steps, finding the optimal path.

Each step shows the board after a move of the blank tile.

Would you like a visualization or explanation of the code behind it?'''
