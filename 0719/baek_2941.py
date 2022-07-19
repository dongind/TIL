croatia= ['c=','c-','dz=','d-','lj','nj','s=','z=']
word = str(input())
sample = ''
cnt = 0
for i in word :
    sample += i
    if len(sample) == 1:
        continue
    elif len(sample) == 2:
        if sample in croatia:
            cnt += 1
            sample = ''
    elif len(sample) == 3:
        if sample in croatia:
            cnt += 1
            sample = ''
        else :
            cnt += 1
            sample = sample[1:]
            if sample in croatia :
                cnt += 1
                sample = ''
if sample :
    if sample in croatia:
        cnt += 1
    else : 
        cnt += len(sample)

print(cnt)