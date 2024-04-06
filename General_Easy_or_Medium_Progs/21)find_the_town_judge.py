n=4
trust = [[1,2],[4,1],[3,2],[3,1],[4,3]]

def findTrust(n, trust):
    trust_count = {i : { "in" : 0, "out" : 0 } for i in range(1, n+1)}   #Disctionary comprehension
    
    for a, b in trust:
        trust_count[a]["out"] += 1
        trust_count[b]["in"] += 1
   # print(trust_count)

    for person, count in trust_count.items():
        if count["in"] == n-1 and count["out"] == 0:
            return person
        
    return -1
    


print(findTrust(n, trust))