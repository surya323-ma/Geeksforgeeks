Given a string s consisting of lowercase English letters and an integer k, your task is to remove exactly k characters from the string. The resulting string must be the largest possible in lexicographical  order, while maintain the relative order of the remaining characters.
#code here py3
class Solution:
    def maxSubseq(self, s: str, k: int) -> str:
        result = []

        for ch in s:
            while result and result[-1] < ch and k > 0:
                result.pop()
                k -= 1
            result.append(ch)

        # If we still need to remove characters, remove from the end
        while k > 0:
            result.pop()
            k -= 1

        return ''.join(result)
#code here c+++
class Solution {
  public:
    string maxSubseq(string& s, int k) {
        int n = s.length();
        string result = "";
        
        for(int i=0; i<n; i++) {
            while(!result.empty() > 0 && result.back() < s[i] && k > 0) {
                result.pop_back();
                k--;
            }
            result += s[i];
        }
        
        while(k) {
            result.pop_back();
            k--;
        }
        
        return result;
    }
};
