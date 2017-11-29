secv = 'AAATTTCTCTGGTAGA'
def number2(secv):
    
     n = len(str(filter(lambda x: x =='A' or x == 'T', secv)))
     return (n, len(secv)-n)
