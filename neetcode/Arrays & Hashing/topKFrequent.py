def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    hMap = defaultdict(int)
    for n in nums:
        hMap[n] += 1
    
    lst = sorted(hMap, key=hMap.get, reverse=True)

    
    return lst[:k]