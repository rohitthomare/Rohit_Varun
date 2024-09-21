import heapq
from collections import defaultdict

def processing_perations(n, operations):
    hard_drive = {}
    eviction_queue = []
    current_time = 0
    results = []
    
    def evict_if_needed():
        if len(hard_drive) >= n:
            #find the last access and older files 
            while eviction_queue:
                access_count, timestamp, name = heapq.heappop(eviction_queue)
                if name in hard_drive and hard_drive[name]['access_count'] == access_count and hard_drive[name]['timestamp'] == timestamp:
                    del hard_drive[name]
                    break
    
    for op in operations:
        current_time += 1
        if op[0] == 1:
            #find moie is there in drive or not 
            movie = op[1]
            if movie in hard_drive:
                #Access count 
                hard_drive[movie]['access_count'] += 1
                hard_drive[movie]['timestamp'] = current_time
                results.append(str(hard_drive[movie]['rating']))
                
                #pushing to heap with timestamp
                heapq.heappush(eviction_queue, (hard_drive[movie]['access_count'], current_time, movie))
            else:
                results.append("-1")
                
        elif op[0] == 2:
            movie, rating = op[1]
            
            if movie in hard_drive:
                #updating the ratings
                hard_drive[movie]['rating'] = rating
                hard_drive[movie]['access_count'] += 1
                hard_drive[movie]['timestamp'] = current_time
            else:
                evict_if_needed()
                
                #adding movie 
                hard_drive[movie] = {
                    'rating': rating,
                    'access_count': 1,
                    'timestamp': current_time
                }
            
            # push or update to heap 
            heapq.heappush(eviction_queue, (hard_drive[movie]['access_count'], current_time, movie))
    
    return results






n = 2  
operations = [
    (1, "GOT"),
    (2, ("GOT", 9)),
    (1, "GOT"),
    (2, ("NARUT", 10)),
    (1, "NARUT"),
    (2, ("BARUT", 6)),
    (1, "GOT"),
    (1, "BARUT")
]

print(processing_perations(n, operations))
