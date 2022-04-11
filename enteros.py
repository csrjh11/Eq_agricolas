def palindromChecker(initial):
    j = len(initial) - 1
    for i in range(int(len(initial)/2)):
        if initial[i] != initial[j]:
            return(0)
        j -= 1
    return (1)

print(palindromChecker("222"))