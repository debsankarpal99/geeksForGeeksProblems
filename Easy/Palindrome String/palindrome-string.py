#User function Template for python3
class Solution:
	def isPalindrome(self, S):
		n = len(S)
		s1 = S[n//2:n]
		s2 = S[n//2 + 1:n]
		if n % 2 == 0 :
		    if S[0:n//2] == s1[::-1]:
		        return 1
		    else : 
		        return 0
	    else :
	        if S[0:n//2] == s2[::-1]:
	            return 1
            else :  
                return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPalindrome(S)
		print(answer)

# } Driver Code Ends