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
    
    # Replacing whitespaces for easier string manipulation
    coord = coord.replace(" ", "")
    
    # Initialize components
    degrees = 0
    minutes = 0
    seconds = 0
    
    # Extracting components
    if '°' in coord:
        degrees = float(coord[: coord.index('°')])
    if "'" in coord:
        minutes = float(coord[coord.index("°") + 1 : coord.index("'")])
    if '"' in coord:
        seconds = float(coord[coord.index("'") + 1 : coord.index('"')])
        
    # Calcualting result
    minutes += seconds / 60
    converted_coord = degrees + minutes / 60
    
    # Handling NESW case
    if 'S' in coord or 'W' in coord:
        converted_coord *= -1
    
    # Returning result
    return converted_coord

print(convert_coordinate("34° 12' 34\" W"))
print(convert_coordinate("23.3245°"))
print(convert_coordinate("-23° 18.45'"))