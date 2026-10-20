class Solution {
    public boolean isAnagram(String s, String t) {

        if (s.length() != t.length()){
            return false;
        }

        Map<Character,Integer> Smap = new HashMap<>();
        Map<Character,Integer> Tmap = new HashMap<>();

        char[] SA = s.toCharArray();
        char[] TA = t.toCharArray();
        for(int i = 0; i < s.length(); i++){
            Smap.put(SA[i], Smap.getOrDefault(SA[i], 0) + 1);
            Tmap.put(TA[i], Tmap.getOrDefault(TA[i], 0) + 1);
        }

        return Smap.equals(Tmap);

    }
}
