L = []

def parr(i, j, m, n, seq, L):
    if i < m or j < n:
        if i < m:
            seq1 = seq + 'd'
            parr(i+1, j, m, n, seq1, L)
            
        if j < n:
            seq2 = seq + 'h'
            parr(i, j+1, m, n, seq2, L)
            
    else:
        L.append(seq)
        


seq = ""
i, j, m, n = 0, 0, 2, 2
parr(i, j, m, n, seq, L)
print(L)
