MAX = 26
def atleastK(freq, k):
    for i in range(MAX):
        if (freq[i]!= 0 and freq[i] < k):
            return False;
        return True;
def setZero(freq):
    for i in range(MAX):
        freq[i] = 0;
def findlength(string, n, k):
    maxLen = 0;
    freq= [0]* MAX;
    for i in range(n):
        setZero(freq);
        for j in range(i, n):
            freq[ord(string[j]) -ord('a')] += 1;
            if (atleastK(freq, k)):
                maxLen=max(maxLen,j-i+1);
                return maxLen;
if _name_ == "__main__":
    string = "aaabb";
    k = 3;
    n=len(string)
    print (findlength(string, n, k));
