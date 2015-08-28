import java.util.Arrays;
public class SolutionDP {
/*
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
*/
    public boolean isInterleave(String s1, String s2, String s3) {
        if(s1.length() + s2.length() != s3.length()) return false;
        boolean dp[][] = new boolean[s2.length()+1][s1.length()+1];
        dp[0][0] = true;   // the case of "","",""
        //System.out.println(Arrays.deepToString(dp));
        //System.out.println(dp[0][1]);
        for(int i = 1; i<=s1.length();i++){
        	dp[0][i] = dp[0][i-1] == true && s1.charAt(i-1) == s3.charAt(i-1);
        }
        //System.out.println(Arrays.deepToString(dp));
        for(int j = 1; j<=s2.length();j++){
        	dp[j][0] = dp[j-1][0] == true && s2.charAt(j-1) == s3.charAt(j-1);
        }
        //System.out.println(Arrays.deepToString(dp));
        for(int j = 1; j<=s1.length(); j++){
        	for(int i = 1; i<=s2.length();i++){
        		if(dp[i-1][j]==true && s2.charAt(i-1) == s3.charAt(i+j-1)){
        			dp[i][j] = true;
        		}else if(dp[i][j-1] == true && s1.charAt(j-1) == s3.charAt(i+j-1)){
        			dp[i][j] = true;
        		}else{
        			dp[i][j] = false;
        		}
        	}
        }
        System.out.println(Arrays.deepToString(dp));
        return dp[s2.length()][s1.length()];
    }


    public static void main(String[] args){
    	SolutionDP sol = new SolutionDP();
    	//System.out.println(sol.isInterleave("aa","ab","aaba"));
    	System.out.println(sol.isInterleave("a","","a"));
    }
}