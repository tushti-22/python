import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    rows, cols = grid.shape

    open_set = [start]
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        current = min(open_set, key=lambda x: f_score.get(x, float('inf')))

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        open_set.remove(current)

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            neighbor = (current[0] + dx, current[1] + dy)

            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if grid[neighbor] == 1:
                    continue

                tentative_g = g_score[current] + 1

                if tentative_g < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + heuristic(neighbor, goal)

                    if neighbor not in open_set:
                        open_set.append(neighbor)

    return None

def visualize(grid, path, start, goal):
    plt.figure(figsize=(6,6))
    plt.imshow(grid, cmap='Greys', origin='upper')

    if path:
        y_coords = [p[1] for p in path]
        x_coords = [p[0] for p in path]
        plt.plot(y_coords, x_coords, 'ro-', label='Path')

    plt.scatter(start[1], start[0], c='green', s=100, label='Start')
    plt.scatter(goal[1], goal[0], c='blue', s=100, label='Goal')

    plt.title("A* Pathfinding Visualization (Without heapq)")
    plt.legend()
    plt.show()

def main():
    while True:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        grid = np.zeros((rows, cols), dtype=int)

        num_obstacles = int(input("Enter number of obstacles: "))
        for i in range(num_obstacles):
            r, c = map(int, input(f"Enter obstacle {i+1} (row col): ").split())
            if 0 <= r < rows and 0 <= c < cols:
                grid[r][c] = 1

        start = tuple(map(int, input("Enter start position (row col): ").split()))
        goal = tuple(map(int, input("Enter goal position (row col): ").split()))

        print("\n Grid Representation (0 = Free, 1 = Obstacle):")
        print(pd.DataFrame(grid))

        path = astar(grid, start, goal)

        if path:
            print("\n Path Found:")
            print(path)
        else:
            print("\n No valid path found.")

        visualize(grid, path, start, goal)

        retry = input("Do you want to try again? (y/n): ").lower()
        if retry != 'y':
            print(" Exiting program.")
            break

if __name__ == "__main__":
    main()
