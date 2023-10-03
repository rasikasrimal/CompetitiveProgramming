class Solution {
    public String reverseWords(String s) {
        String[] words = s.split(" ");
        String revString = "";

        for (int i = 0; i < words.length; i++){
            String word = words[i];
            String revWord = "";

            for (int j = word.length() -1; j >= 0; j--){
                revWord = revWord + word.charAt(j);
            }

            revString = revString + revWord + " ";
        }
        return revString.trim();
    }
}
