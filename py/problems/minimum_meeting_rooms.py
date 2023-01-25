"""
Given an array of meeting time instant containing the start and end time of the meeting, return the minimum number of meeting rooms required to hold all the meetings such that each meeting takes place in a separate room.

Note:

Meeting end times are exclusive e.g. meetings scheduled for [2, 5) and [5, 10) can be held in the same room.
Size of array can be upto 10^5.

Sample 0
Input
meetings: [[0,30],[5,10],[15,20]]

Output
2

Sample 1
Input
meetings: [[1,18],[18,23],[15,29],[4,15],[2,11],[5,13]]

Output
4
"""
from __future__ import annotations
import heapq
class MinimumMeetingRooms:
    def getMinimumRooms(self, meetings: list[list[int]]) -> int:
    	rooms = []
    	meetings.sort(key=lambda m:m[0])
    	for m in meetings:
    	    #print(rooms)
    	    if rooms and rooms[0]<=m[0]:
    		heapq.heappop(rooms)
    	    heapq.heappush(rooms, m[1])
    	return len(rooms)
