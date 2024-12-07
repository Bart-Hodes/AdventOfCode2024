def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None


def findCycle(graph):
    visited = set()
    stack = []
    for node in graph:
        if node not in visited:
            if dfs(node, graph, visited, stack):
                return True
    return False


def dfs(node, graph, visited, stack):
    visited.add(node)
    stack.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs(neighbor, graph, visited, stack):
                return True
        elif neighbor in stack:
            print(f"Cycle found: {stack[stack.index(neighbor):]}")
            return True
    stack.pop()
    return False


# Read input from file
with open("test.txt", "r") as f:
    input = []
    for line in f:
        input.append(line.strip())

# Initialize variables
obstacleList = set()
start = None
directions = {"^": (0, -1), "v": (0, 1), ">": (1, 0), "<": (-1, 0)}

# Parse the input to find obstacles and start position with direction
for y, line in enumerate(input):
    for x, char in enumerate(line):
        if char == "#":
            obstacleList.add((x, y))
        elif char in directions:
            start = (x, y)
            direction = directions[char]

# Initialize the graph
graph = {}

# Find positions adjacent to obstacles and add them to the graph nodes
rows = len(input)
cols = len(input[0])
collisions = set()

for obstacle in obstacleList:
    x, y = obstacle
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        # Only valid positions and directions are added
        if 0 <= nx < cols and 0 <= ny < rows and (nx, ny) not in obstacleList:
            collisions.add((x, y, dx, dy))

print(collisions)
# Add edges for these positions based on the direction of movement
for x1, y1, dx1, dy1 in collisions:
    print(f"Checking for position {(x1, y1), dx1, dy1}")
    for x2, y2, dx2, dy2 in collisions:
        if (x1, y1) == (x2, y2):
            continue
        # Check if the two positions are adjacent
        if dx1 == 1:
            if x1 + dx1 == x2 and y1 > y2:
                print(f"Adding edge from {(x1+dx1, y1)} to {(x2, y2+1)}")
                graph[(x1 + dx1, y1)] = []
                graph[(x1 + dx1, y1)].append((x2, y2 + 1))
        elif dx1 == -1:
            if x1 + dx1 == x2 and y1 < y2:
                print(f"Adding edge from {(x1-1, y1)} to {(x2, y2-1)}")
                graph[(x1 + dx1, y1)] = []
                graph[(x1 + dx1, y1)].append((x2, y2 - 1))
        elif dy1 == 1:
            if y1 + dy1 == y2 and x1 < x2:
                print(f"Adding edge from {(x1, y1+1)} to {(x2-1, y2)}")
                graph[(x1, y1 + dy1)] = []
                graph[(x1, y1 + dy1)].append((x2 - 1, y2))
        elif dy1 == -1:
            if y1 + dy1 == y2 and x1 > x2:
                print(f"Adding edge from {(x1, y1-1)} to {(x2+1, y2)}")
                graph[(x1, y1 + dy1)] = []
                graph[(x1, y1 + dy1)].append((x2 + 1, y2))


# Print the graph to verify
for node, neighbors in graph.items():
    print(f"{node}: {neighbors}")

print(findCycle(graph))
