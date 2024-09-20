import java.util.*;

class Solution {
    public int solution(int n) {
        int answer = 0;
        
        String n3="";
        while (n>0) {
            n3=String.valueOf(n%3)+n3;
            n=n/3;
        }
        //System.out.println(n3);
        //.charAt(i)
        for(int i=0; i<n3.length(); i++){
            answer+=(Math.pow(3,i))*Integer.parseInt(String.valueOf(n3.charAt(i)));
        }
        
        return answer;
    }
}