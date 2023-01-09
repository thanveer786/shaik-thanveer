time=int(input())
entry=list(map(int, input().split()))
exit=list(map(int, input().split()))
present=0
total_guest=0
for i in range(time):
    present += entry[i]-exit[i]
    if total_guests < present:
        total_guests=present
print(total_guest, end = " ")
