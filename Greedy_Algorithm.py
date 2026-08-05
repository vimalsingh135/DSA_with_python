## N meetings in one room
def n_meetings(start,end,n):
    meetings = []
    for i in range(n):
        meetings.append((start[i], end[i], i+1))
    
    # Sort meetings based on their end time
    meetings.sort(key=lambda x: x[1])
    
    result = []
    last_end_time = 0
    
    for meeting in meetings:
        if meeting[0] > last_end_time:
            result.append(meeting[2])  # Append meeting number
            last_end_time = meeting[1]
    
    return result