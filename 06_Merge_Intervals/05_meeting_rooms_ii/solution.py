class Solution:
    def minMeetingRooms(self, start, end):
        start.sort()
        end.sort()
        
        i, j = 0, 0
        active, rooms = 0, 0
        
        while i < len(start) and j < len(end):
            if start[i] < end[j]:
                active += 1
                i += 1
                rooms = max(rooms, active)
                
            elif end[j] <= start[i]:
                active -= 1
                j += 1
                
        return rooms