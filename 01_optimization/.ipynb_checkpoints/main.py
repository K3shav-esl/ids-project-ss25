import os
from src.data_loader import load_points_data, load_lsm_matrix
from src.robot_fleet_optimizer import optimize_routes, calc_total_tour_time
from src.visualization import plot_machine_locations, plot_tour
from src.utils import convert_seconds_to_hms

def main():
    # Define data paths
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    gianni_file = os.path.join(data_dir, 'points_gianni_55_42.txt')
    lissi_file = os.path.join(data_dir, 'points_lissi_55_42.txt')
    ben_file = os.path.join(data_dir, 'points_ben_55_42.txt')
    lsm_file = os.path.join(data_dir, 'ls_matrix_55_42.txt')

    # 1. Load Data
    print("Loading machine points data...")
    gianni_points = load_points_data(gianni_file)
    lissi_points = load_points_data(lissi_file)
    ben_points = load_points_data(ben_file)
    all_points = {**gianni_points, **lissi_points, **ben_points} # Combine all points, handle duplicates if any

    print("Loading travel-service-time matrix...")
    lsm_matrix = load_lsm_matrix(lsm_file)

    # 2. Data Overview and Visualization (Initial Thoughts)
    print("\nGenerating initial overview plots...")
    # Example: Plot all machine locations, colored by floor
    plot_machine_locations(all_points)

    # 3. Robot Specifications
    # Robot Type 1: 10 hours battery (36000 seconds)
    # Robot Type 2: 6 hours battery (21600 seconds)
    # Early shift duration: 8 hours (28800 seconds)
    robot_specs = {
        "Type1": {"battery_capacity_sec": 10 * 3600},
        "Type2": {"battery_capacity_sec": 6 * 3600}
    }
    shift_duration_sec = 8 * 3600

    # 4. Optimize Routes for Employee Rounds
    print("\nOptimizing routes for existing employee rounds...")
    # For each employee's set of machines, determine an optimal sequence
    # and assess robot requirements.
    # This is where you'll implement your chosen optimization algorithm (e.g., Nearest Neighbor)

    # Example for Gianni's route:
    gianni_machine_indices = list(gianni_points.keys())
    # Ensure depot (0) is included and handled correctly for starting/ending
    if 0 not in gianni_machine_indices:
        gianni_machine_indices.insert(0, 0) # Add depot if not present

    print(f"\n--- Optimizing Gianni's Route ({len(gianni_machine_indices)} machines) ---")
    gianni_optimized_sequence = optimize_routes(gianni_machine_indices, lsm_matrix)
    gianni_tour_time_sec = calc_total_tour_time(gianni_optimized_sequence, lsm_matrix)
    print(f"Gianni's optimized tour time: {convert_seconds_to_hms(gianni_tour_time_sec)}")
    print(f"Gianni's optimized sequence: {gianni_optimized_sequence}")
    plot_tour(gianni_optimized_sequence, all_points, title="Gianni's Optimized Tour")

    # Repeat for Lissi and Ben
    # Repeating the calculation for Lissi 
    lissi_machine_indices = list(lissi_points.keys())
    # Ensure depot (0) is included and handled correctly for starting/ending
    if 0 not in lissi_machine_indices:
        lissi_machine_indices.insert(0, 0) # Add depot if not present

    print(f"\n--- Optimizing lissi's Route ({len(lissi_machine_indices)} machines) ---")
    lissi_optimized_sequence = optimize_routes(lissi_machine_indices, lsm_matrix)
    lissi_tour_time_sec = calc_total_tour_time(lissi_optimized_sequence, lsm_matrix)
    print(f"lissi's optimized tour time: {convert_seconds_to_hms(lissi_tour_time_sec)}")
    print(f"lissi's optimized sequence: {lissi_optimized_sequence}")
    plot_tour(lissi_optimized_sequence, all_points, title="Lissi's Optimized Tour")


    #Repeating the calculation for Ben 

    ben_machine_indices = list(ben_points.keys())
    # Ensure depot (0) is included and handled correctly for starting/ending
    if 0 not in ben_machine_indices:
        ben_machine_indices.insert(0, 0) # Add depot if not present

    print(f"\n--- Optimizing ben's Route ({len(ben_machine_indices)} machines) ---")
    ben_optimized_sequence = optimize_routes(ben_machine_indices, lsm_matrix)
    ben_tour_time_sec = calc_total_tour_time(ben_optimized_sequence, lsm_matrix)
    print(f"ben's optimized tour time: {convert_seconds_to_hms(ben_tour_time_sec)}")
    print(f"ben's optimized sequence: {ben_optimized_sequence}")
    plot_tour(ben_optimized_sequence, all_points, title="ben's Optimized Tour")

    # 5. Assess Robot Fleet Sizing
    print("\nAssessing robot fleet sizing...")
    # Based on the optimized tour times, determine how many robots of each type are needed.
    # Consider the 8-hour shift limit and robot battery capacities.

    # Example assessment for Gianni's route:
    print("\n--- Robot Assessment for Gianni's Route ---")
    if gianni_tour_time_sec <= shift_duration_sec:
        print(f"Gianni's route fits within an 8-hour shift ({convert_seconds_to_hms(shift_duration_sec)}).")
        if gianni_tour_time_sec <= robot_specs["Type2"]["battery_capacity_sec"]:
            print("  - Robot Type 2 (6h battery) is sufficient.")
        elif gianni_tour_time_sec <= robot_specs["Type1"]["battery_capacity_sec"]:
            print("  - Robot Type 1 (10h battery) is required.")
        else:
            print("  - Neither robot type can complete this route in one charge.")
    else:
        print(f"Gianni's route ({convert_seconds_to_hms(gianni_tour_time_sec)}) exceeds an 8-hour shift.")
        # Further logic needed here if a route exceeds shift duration (e.g., splitting routes)

    # 6. Explore Advanced Scenarios (e.g., K-Means Clustering for 2 Robots)
    print("\nExploring advanced scenarios (e.g., K-Means clustering for 2 robots)...")
    # This part will involve clustering all machines and then optimizing routes for the clusters.
    # You'll need to implement K-Means and then apply route optimization to the resulting clusters.

    print("\nOptimization complete. Review plots and console output for results.")

if __name__ == "__main__":
    main()


## kartik made changes here 
    
