import heapq

def uniform_cost_search(graph, start, goal):
    # Create a priority queue and add the start node with cost 0
    queue = [(0, start)]
    # Create a set to keep track of visited nodes
    visited = set()

    while queue:
        # Get the node with the minimum cost
        cost, current_node = heapq.heappop(queue)

        # If the current node is the goal, we have found the path
        if current_node == goal:
            return cost

        # Mark the current node as visited
        visited.add(current_node)

        # Explore the neighbors of the current node
        for neighbor, neighbor_cost in graph[current_node].items():
            # Calculate the new cost to reach the neighbor
            new_cost = cost + neighbor_cost

            # If the neighbor has not been visited or has a lower cost,
            # update its cost and add it to the queue
            if neighbor not in visited:
                heapq.heappush(queue, (new_cost, neighbor))

    # If no path is found, return None
    return None


# The graph representation
graph = {
    "Tumkur": {"KB Cross":45,"Sira":50},
    "KB Cross":{"Tiptur":20,"Hosadurga":75},
    "Sira":{"Hiriyur":40},
    "Tiptur":{"Arasikere":25},
    "Hosadurga":{"Arasikere":70,"Holalkere":30},
    "Hiriyur":{"Chitradurga":40,"Hosadurga":50},
    "Chitradurga":{"Holalkere":30},
    "Arasikere":{"Shivamogga":110},
    "Holalkere":{"Shivamogga":75},
    
    }

# Define the start and goal nodes
start_node = "Tumkur"
goal_node = "Shivamogga"

# Execute the Uniform Cost Search algorithm
result = uniform_cost_search(graph, start_node, goal_node)

if result is not None:
    print(f"The minimum cost from {start_node} to {goal_node} is {result}.")
else:
    print(f"There is no path from {start_node} to {goal_node}.")