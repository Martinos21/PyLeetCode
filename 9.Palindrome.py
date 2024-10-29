def isPalindrome(self, x: int) -> bool:
        nonreversed_x = str(x)
        reversed_x = "".join(reversed(str(x))) 
	    
        if (nonreversed_x == reversed_x):
            return True