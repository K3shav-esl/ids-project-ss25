import os

def load_points_data(filepath):
    """
    Loads machine point data from a text file.
    Expected format: index; x_coord; y_coord; floor
    Returns a dictionary: {index: {'x': x, 'y': y, 'floor': floor}}
    """
    points = {}
    try:
        with open(filepath, 'r') as f:
            for line in f:
                parts = line.strip().split(';')
                if len(parts) == 4:
                    idx = int(parts[0].strip())
                    x = float(parts[1].strip())
                    y = float(parts[2].strip())
                    floor = int(parts[3].strip())
                    points[idx] = {'x': x, 'y': y, 'floor': floor}
                else:
                    print(f"Warning: Skipping malformed line in {filepath}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
    except Exception as e:
        print(f"Error loading points data from {filepath}: {e}")
    return points

def load_lsm_matrix(filepath):
    """
    Loads the travel-service-time matrix from a text file.
    Expected format: start_idx; end_idx; time_in_seconds
    Returns a dictionary: {(start_idx, end_idx): time_in_seconds}
    """
    lsm_matrix = {}
    try:
        with open(filepath, 'r') as f:
            for line in f:
                parts = line.strip().split(';')
                if len(parts) == 3:
                    start_idx = int(parts[0].strip())
                    end_idx = int(parts[1].strip())
                    time_sec = float(parts[2].strip())
                    lsm_matrix[(start_idx, end_idx)] = time_sec
                else:
                    print(f"Warning: Skipping malformed line in {filepath}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
    except Exception as e:
        print(f"Error loading LSM matrix from {filepath}: {e}")
    return lsm_matrix

if __name__ == '__main__':
    # Example usage for testing data_loader
    current_dir = os.path.dirname(__file__)
    data_dir = os.path.join(os.path.dirname(current_dir), 'data')

    gianni_file = os.path.join(data_dir, 'points_gianni_55_42.txt')
    lsm_file = os.path.join(data_dir, 'ls_matrix_55_42.txt')

    print(f"Attempting to load: {gianni_file}")
    gianni_data = load_points_data(gianni_file)
    print(f"Loaded {len(gianni_data)} Gianni points.")
    if gianni_data:
        print(f"Sample Gianni point: {list(gianni_data.items())[0]}")

    print(f"\nAttempting to load: {lsm_file}")
    lsm_data = load_lsm_matrix(lsm_file)
    print(f"Loaded {len(lsm_data)} LSM entries.")
    if lsm_data:
        print(f"Sample LSM entry: {list(lsm_data.items())[0]}")
