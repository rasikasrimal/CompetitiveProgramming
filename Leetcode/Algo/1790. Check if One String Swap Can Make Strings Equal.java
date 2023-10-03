class Solution {
    public boolean areAlmostEqual(String s1, String s2) {
        int n = s1.length();
        int diffCount = 0;
        int[] diffIndices = new int[2];
        
        for (int i = 0; i < n; i++) {
            if (s1.charAt(i) != s2.charAt(i)) {
                if (diffCount == 2) {
                    return false;
                }
                diffIndices[diffCount++] = i;
            }
        }
        
        if (diffCount == 0) {
            return true;
        }
        if (diffCount == 2) {
            return s1.charAt(diffIndices[0]) == s2.charAt(diffIndices[1]) &&
                   s1.charAt(diffIndices[1]) == s2.charAt(diffIndices[0]);
        }
        return false;
    }
}

/*
class Solution {
    public boolean areAlmostEqual(String s1, String s2) {
        int swap_count = 0;
        
        for( int i = 0; i < s1.length(); i++) {
            if( s1.charAt(i) == s2.charAt(i) ) {
                swap_count++;
            }

            int similar = countSimilarCharacters(s1, s2);

            if ( similar == s1.length()) {
                if ( swap_count == s1.length() || swap_count == s1.length() - 2) {
                    return true;
                }
            }
        }
        return false;
    }

    public int countSimilarCharacters(String s1, String s2) {
        int similar = 0;
        int i = 0;
        int j = 0;
        while (i < s1.length() && j < s2.length()) {
            if (s1.charAt(i) == s2.charAt(j)) {
                similar++;
                i++;
                j++;
            } else if (s1.charAt(i) < s2.charAt(j)) {
                i++;
            } else {
                j++;
            }
        }
        return similar;
    }
}*/
