def residency_index(days_detected, first_day, last_day):
    """
    Calculate residency index within the VPS array
    
    Parameters:
    days_detected - number of unique days the shark was detected in the array
    first_day - first detection date
    last_day - last detection date
    
    Returns:
    ri - Residency index based on days detected divided by days 
        between first and last detection
    """
    detection_interval = (last_day - first_day).days + 1
    ri = days_detected / detection_interval
    return ri
