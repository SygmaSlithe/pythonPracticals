## Aim:- Find Captain Room Number.
## Student_Name:- Darshan Shah
## Student_ID:- 20CS077

from collections import Counter

K = int(input())
room_list = input().split()

list = [int(captain_room) for captain_room in room_list]

c = Counter(list)

for captain_room in c:
    key = captain_room
    value = c[captain_room]
    if value == 1:
        print(key)
