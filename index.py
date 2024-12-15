def minimize_total_effort(effort):
    # Sort the array for efficient checking of smallest divisors
    sorted_effort = sorted(effort)
    
    # Create a new list for the transformed efforts
    minimized = []
    
    # For each element, find the smallest divisor in the sorted array
    for value in effort:
        for candidate in sorted_effort:
            # Check if candidate divides value
            if value % candidate == 0:
                minimized.append(candidate)
                break
    
    # Calculate and return the sum of minimized efforts
    return sum(minimized)

# Example usage:
if __name__ == "__main__":
    # Example given in the prompt
    effort = [3, 6, 2, 5, 25, 25, 25, 100, 100, 100, 25]
    result = minimize_total_effort(effort)
    print("Minimum total effort:", result)  # Expected: 17
