def lengthOfLastWord(self, s: str) -> int:
        charCount = 0
        arr = s.split()
        
        for c in arr[-1]:
            charCount +=1

        return charCount