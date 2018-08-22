n,m =map(int, input().split())
target_list=map(int,input().split())
set1=set(map(int,input().split()))
set2=set(map(int,input().split()))

print (sum([(i in set1) - (i in set2) for i in target_list]))