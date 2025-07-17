import matplotlib.pyplot as plt

def plot_machine_locations(all_points_data, title="Machine Locations by Floor"):
    """
    Creates a 2D scatter plot of machine locations, colored by floor.
    Labels points with their indices.
    
    Args:
        all_points_data (dict): Dictionary of all machine points {index: {'x': x, 'y': y, 'floor': floor}}.
        title (str): Title of the plot.
    """
    if not all_points_data:
        print("No points data to plot.")
        return

    # Group points by floor
    floors = sorted(list(set(p['floor'] for p in all_points_data.values())))
    
    plt.figure(figsize=(12, 8))
    
    for floor in floors:
        floor_points_x = [p['x'] for idx, p in all_points_data.items() if p['floor'] == floor]
        floor_points_y = [p['y'] for idx, p in all_points_data.items() if p['floor'] == floor]
        plt.scatter(floor_points_x, floor_points_y, label=f'Floor {floor}', alpha=0.7)

    # Label points with their indices
    for idx, p in all_points_data.items():
        plt.text(p['x'], p['y'], str(idx), fontsize=8, ha='right')

    # Highlight depot (index 0) if present
    if 0 in all_points_data:
        depot = all_points_data[0]
        plt.scatter(depot['x'], depot['y'], color='red', marker='X', s=200, label='Depot (0)', zorder=5)
        plt.text(depot['x'], depot['y'], 'Depot', fontsize=10, ha='left', va='bottom', color='red')

    plt.title(title)
    plt.xlabel("X-coordinate")
    plt.ylabel("Y-coordinate")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_tour(sequence, all_points_data, title="Robot Tour"):
    """
    Plots a robot tour sequence on a scatter plot.
    
    Args:
        sequence (list): The ordered list of machine indices in the tour.
        all_points_data (dict): Dictionary of all machine points {index: {'x': x, 'y': y, 'floor': floor}}.
        title (str): Title of the plot.
    """
    if not sequence or len(sequence) < 2:
        print("Sequence too short to plot a tour.")
        return
    
    tour_x = [all_points_data[idx]['x'] for idx in sequence if idx in all_points_data]
    tour_y = [all_points_data[idx]['y'] for idx in sequence if idx in all_points_data]

    if len(tour_x) != len(sequence):
        print("Warning: Some points in the sequence were not found in all_points_data.")
        return

    plt.figure(figsize=(10, 7))
    
    # Plot all points as background
    for idx, p in all_points_data.items():
        plt.scatter(p['x'], p['y'], color='lightgray', alpha=0.5)
        plt.text(p['x'], p['y'], str(idx), fontsize=7, ha='right', color='gray')

    # Plot the tour path
    plt.plot(tour_x, tour_y, 'b-o', markersize=8, linewidth=2, label='Tour Path')
    
    # Highlight start/end point (depot)
    if sequence[0] in all_points_data:
        depot = all_points_data[sequence[0]]
        plt.scatter(depot['x'], depot['y'], color='red', marker='X', s=200, label='Depot (Start/End)', zorder=5)
        plt.text(depot['x'], depot['y'], 'Depot', fontsize=10, ha='left', va='bottom', color='red')

    # Label points in the sequence
    for i, idx in enumerate(sequence):
        if idx in all_points_data:
            plt.text(all_points_data[idx]['x'], all_points_data[idx]['y'], f'{idx}', fontsize=9, ha='right', va='bottom')
            if i == 0: # Start point
                plt.text(all_points_data[idx]['x'], all_points_data[idx]['y'], 'Start', fontsize=9, ha='left', va='top', color='green')
            elif i == len(sequence) - 1: # End point
                plt.text(all_points_data[idx]['x'], all_points_data[idx]['y'], 'End', fontsize=9, ha='left', va='top', color='purple')


    plt.title(title)
    plt.xlabel("X-coordinate")
    plt.ylabel("Y-coordinate")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    # Example usage for testing visualization
    test_points = {
        0: {'x': 0, 'y': 0, 'floor': 0},
        1: {'x': 10, 'y': 10, 'floor': 1},
        2: {'x': 0, 'y': 10, 'floor': 0},
        3: {'x': 10, 'y': 0, 'floor': 1},
        4: {'x': 5, 'y': 5, 'floor': 0}
    }
    
    print("Plotting all test machine locations...")
    plot_machine_locations(test_points, title="Test Machine Locations")

    test_tour_sequence = [0, 2, 1, 3, 0]
    print(f"Plotting test tour: {test_tour_sequence}")
    plot_tour(test_tour_sequence, test_points, title="Test Robot Tour")
