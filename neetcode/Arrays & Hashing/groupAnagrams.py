def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    '''
    - iterate thry the list
        - copy and sort the element
        - sorted element -> [element]
    - iterate thru the map
        - append values to list
    '''
    
    hMap = collections.defaultdict(list)
    
    for s in strs:
        keyS = ''.join(sorted(s))
        hMap[keyS].append(s)
        
    return hMap.values()