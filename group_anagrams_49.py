class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_dict = {}
        for string in strs:
            list_of_letters = 26 * [0]
            for char in string:
                list_of_letters[ord(char) - ord('a')] += 1

            tuple_of_letters = tuple(list_of_letters)

            if tuple_of_letters not in map_dict:
                map_dict[tuple_of_letters] = []
            
            map_dict[tuple_of_letters].append(string)
            
        return list(map_dict.values())