class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        hash_map = {}
        alphabet = string.ascii_lowercase
        key = key.replace(' ', '')
        count, index = 0, 0
        
        while count < 26:
            if not key[index] in hash_map.keys():
                hash_map[key[index]] = alphabet[count]
                count += 1
            index += 1
            
        res = ""
        for value in message:
            if value == ' ':
                res += " "
            else:
                res += hash_map[value]
        return res
