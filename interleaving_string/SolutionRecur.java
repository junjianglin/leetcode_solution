public class SolutionRecur {
    public boolean isInterleave(String s1, String s2, String s3) {
        if((s1+s2).equals(s3) || (s2+s1).equals(s3)){
            return true;
        }
        if(s1.length()+s2.length() != s3.length()){
            return false;
        }else if(s1.length()<1 || s2.length()<1){
            return false;
        }else{
            return helper(s1,s2,s3,0,0,0);
        }
    }
    
    public boolean helper(String s1, String s2, String s3, int p1, int p2, int p3){
        System.out.println(p1+","+p2+","+p3);

        if(p3 == s3.length()){
            return true;
        }
        if(p1 == s1.length()){
            if(s2.substring(p2).equals(s3.substring(p3))){
                 return true;
            }else {
                return false;
            }
        }
        if(p2 == s2.length()){
            if(s1.substring(p1).equals(s3.substring(p3))){
                return true;
            }else {
                return false;
            }
        }

        if(s1.charAt(p1)==s3.charAt(p3)&&s2.charAt(p2)==s3.charAt(p3)){
            return helper(s1,s2,s3,p1+1,p2,p3+1) || helper(s1,s2,s3,p1,p2+1,p3+1);
        }else if(s1.charAt(p1)==s3.charAt(p3)){
            return helper(s1,s2,s3,p1+1,p2,p3+1);
        }else if(s2.charAt(p2)==s3.charAt(p3)){
            return helper(s1,s2,s3,p1,p2+1,p3+1);
        }else{
            return false;
        }
    }

    public static void main(String[] args){
        SolutionRecur sol = new SolutionRecur();
        System.out.println(sol.isInterleave("bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa", "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab", "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"));
    }
}