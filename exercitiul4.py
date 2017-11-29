#popescu ionut cosmin


L = [1,2,4,8,16,32,64]
X = 2


for i in L:
    
    if 2 ** X == L[i]: 
        print(X, 'at index', i)
        break
    else:
        print('not found')
    
