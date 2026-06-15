import sys
i=sys.stdin.read().split()
capital,string=int(i[0]),i[1]
r,m="",0
for j in range(capital-1):
  t=string[j:j+2]
  c=sum(1 for k in range(capital-1) if string[k:k+2]==t)
  if c>m:m,r=c,t
print(r)