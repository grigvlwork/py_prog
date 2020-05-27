def mirror(arr): 
    arr.extend([s for s in arr[::-1]])
