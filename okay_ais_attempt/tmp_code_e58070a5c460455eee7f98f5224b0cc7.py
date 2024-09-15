from collections import deque

# Function to calculate the fewest number of moves needed to solve a puzzle using BFS
def calculate_fewest_moves(initial_state, solution_state, allowed_moves):
    queue = deque([(initial_state, 0)])  # Initialize queue with initial state and zero moves
    
    visited = set()  # Set to keep track of visited states
    
    while queue:
        current_state, moves = queue.popleft()  # Get the current state and number of moves
        
        if current_state == solution_state:
            return moves  # Return the number of moves when the solution state is reached
        
        if current_state in visited:
            continue  # Skip if the current state has been visited
        
        visited.add(current_state)
        
        # Generate next states by applying allowed moves
        for move in allowed_moves:
            # Placeholder logic to apply moves
            next_state = current_state  # Placeholder - Actual logic to apply moves needed here
            
            queue.append((next_state, moves + 1))  # Add the next state to the queue with updated number of moves
        
    return -1  # Return -1 if no solution is found within the constraints

# Example usage of the function
initial_state_example = "A;B;C"
solution_state_example = "C;B;A"
allowed_moves_example = ["A", "B"]
fewest_moves_example = calculate_fewest_moves(initial_state_example, solution_state_example, allowed_moves_example)

fewest_moves_example