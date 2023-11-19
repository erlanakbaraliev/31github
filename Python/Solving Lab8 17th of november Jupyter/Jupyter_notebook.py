s = "()"        
s_arr = []
for each in s:
    s_arr += [each]
        
s_len = len(s_arr)
arr_bool = []
for i in range(s_len-1):
    j = i + 1
    while j < s_len and (ord(s_arr[i]) - ord(s_arr[j])) != -1 or (ord(s_arr[i]) - ord(s_arr[j])) != -2:
        j += 1
    if j < s_len:
        arr_bool += [True]
    else:
        arr_bool += [False]