Given a single string s, the task is to check if it is a palindrome sentence or not.
A palindrome sentence is a sequence of characters, such as word, phrase, or series of symbols that reads the same backward as forward after converting all uppercase letters to lowercase and removing all non-alphanumeric characters (including spaces and punctuation).

  


class Solution {

    public boolean sentencePalindrome(String s) {
        // code here
        String str = s.toLowerCase();
        String revStr = new StringBuilder(str).reverse().toString();
        
        int i=0, j=0, n=s.length();
        while(i<n && j<n) {
            Boolean res1 = isAlphaNumeric(str.charAt(i));
            Boolean res2 = isAlphaNumeric(revStr.charAt(j));
            
            if(res1 == false) {
                i++;
            }
            else if(res2 == false) {
                j++;
            }
            else if(str.charAt(i) == revStr.charAt(j)) {
                i++;
                j++;
            }
            else {
                return false;
            }
            
        }
        return true;
    }
    public boolean isAlphaNumeric(char ch) {
        if(!(ch>='A' && ch<='Z') && !(ch>='a' && ch<='z') && !(ch>='0' && ch<='9')) {
            return false;
        }
        else {
            return true;
        }
    }
    
}
