class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        j=0
        
        #merged output
        merge=""

       # two pointer for 2 word
        while i<len(word1) and j<len(word2):

            #even places for word1 
            if len(merge)%2==0:
                merge+=word1[i]
                i+=1
            else:
                #odd places for word2
                 merge+=word2[j]
                 j+=1
            
            
        #append the rest of the letters   
        merge+=word1[i:]
        merge+=word2[j:]

        #return merged word.
        return merge

