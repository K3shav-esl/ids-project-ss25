def convert_seconds_to_hms(seconds):
    """
    Converts a duration in seconds to a human-readable H:M:S format.
    """
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    remaining_seconds = seconds % 60
    return f"{hours:02d}h {minutes:02d}m {remaining_seconds:.2f}s"

def estimate_runtime_complexity(algorithm_name, n):
    """
    Provides a theoretical runtime complexity estimate for common algorithms.
    n = number of machines.
    """
    if algorithm_name == 'nearest_neighbor':
        # For each of n nodes, we iterate through remaining n-1 nodes.
        # Roughly O(n^2) for a simple implementation.
        return f"O(n^2) where n is the number of machines. For n={n}, operations are roughly {n**2}."
    elif algorithm_name == 'optimal_tsp':
        # Exact TSP algorithms are typically NP-hard, e.g., O(n! * n) or O(2^n * n^2)
        return f"O(n! * n) or O(2^n * n^2) for exact TSP. Highly complex for large n."
    elif algorithm_name == 'kmeans':
        # K-Means complexity is roughly O(I * k * n * d) where I is iterations, k is clusters, n is points, d is dimensions.
        return f"O(I * k * n * d) for K-Means clustering. For n={n}, this is efficient."
    else:
        return "Runtime complexity estimate not available for this algorithm."

if __name__ == '__main__':
    # Example usage for testing utils
    print(f"3600 seconds is: {convert_seconds_to_hms(3600)}")
    print(f"5300 seconds is: {convert_seconds_to_hms(5300)}")
    print(f"8 hours is: {convert_seconds_to_hms(8 * 3600)}")

    print("\nRuntime complexity estimates:")
    print(f"Nearest Neighbor (n=10): {estimate_runtime_complexity('nearest_neighbor', 10)}")
    print(f"Optimal TSP (n=10): {estimate_runtime_complexity('optimal_tsp', 10)}")
    print(f"K-Means (n=100): {estimate_runtime_complexity('kmeans', 100)}")
