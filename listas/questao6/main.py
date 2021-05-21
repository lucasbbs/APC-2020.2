from itertools import accumulate
input = list(map(int,input().split()))
print(" ".join(map(str,list(accumulate(input)))))
print(" ".join(map(str,input)))


l = [int(i) for i in input().split()]
res = [sum(l[:i + 1]) for i in range(len(l))] 
print(*res, sep=' ')
print(*l, sep=' ')

# Solucao alternativa: Vinicius

#vetor = [int(x) for x in input().split()]

#psum = [0]*(len(vetor)+1)

#for i in range(0,len(vetor)):
#  psum[i+1] = psum[i]+vetor[i]

#ans1 = str(psum[1])
#ans2 = str(vetor[0])

#for i in range(1,len(vetor)):
#  ans1=ans1+" "+str(psum[i+1])
#  ans2=ans2+" "+str(vetor[i])
#print(ans1+"\n"+ans2)
