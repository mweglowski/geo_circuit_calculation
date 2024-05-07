import pandas as pd
import csv

data = pd.read_csv('points.csv', quoting=csv.QUOTE_NONE)

# Converting coordinate function
def convert_coordinate(coord: str) -> float:
    """
    Convert various geographical coordinate formats to decimal degrees.
    
    Args:
        coord (str): Coordinate presented in different formats:
            1. Degrees with decimal (e.g., 34.1234°)
            2. Degrees and minutes with decimal (e.g., 34° 12.345')
            3. Degrees, minutes, and seconds (e.g., 34° 12' 34")
            4. Includes direction letters (N, E, S, W) (e.g., 34° 5' 15.22" W)
    
    Returns:
        converted_coord (float) : Converted coordinate in decimal degrees format (1).
    """

    # Removing quotes at the end and the beginning
    coord = coord[1:-1]

    # Handling the case with NESW letters
    reverse = False
    if 'S' in coord or 'W' in coord:
        reverse = True

    for char in 'NESW':
        coord = coord.replace(char, "")
    
    # Replacing whitespaces for easier string manipulation
    coord = coord.replace(" ", "").replace("\\", "")
    
    # Initialize components
    degrees = 0
    minutes = 0
    seconds = 0
    
    # Extracting degrees
    if '°' in coord:
        degrees = float(coord[: coord.index('°')])
        if degrees < 0:
            degrees *= -1
    # Extracting minutes
    if "'" in coord:
        minutes = float(coord[coord.index("°") + 1 : coord.index("'")])
    # Extracting seconds
    if '"' in coord:
        seconds = float(coord[coord.index("'") + 1 : coord.index('"')])
        
    # Calcualting result
    minutes += seconds / 60
    converted_coord = degrees + minutes / 60
    
    # Handling the case with NESW letters
    if reverse:
        converted_coord *= -1

    # Rounding to clean numbers with long decimal expansion (e.g. 23.666666666)
    converted_coord = round(converted_coord, 4)

    # Returning result
    return converted_coord

for index, row in data.iterrows():
    print(row['latitude'], row['longitude'])
    print(row['name'], convert_coordinate(row['latitude']), convert_coordinate(row['longitude']))