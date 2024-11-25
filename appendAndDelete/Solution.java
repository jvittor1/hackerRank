import java.io.*;

class Result {

    /*
     * Complete the 'appendAndDelete' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts following parameters:
     *  1. STRING s
     *  2. STRING t
     *  3. INTEGER k
     */

    public static String appendAndDelete(String s, String t, int k) {
    // Write your code here
        int lenToCompare = 0;

        for(int i = 0; i < t.length(); i++){
            if(i < s.length() && s.charAt(i) == t.charAt(i)){
                lenToCompare++;
            }else{
                break;
            }
        }

        int minOperations = s.length() + t.length() - 2 * lenToCompare;

        if(minOperations > k){
            return "No";
        }

        if((k - minOperations) % 2 == 0 || k >= s.length() + t.length()){
            return "Yes";
        }

        return "No";


    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = bufferedReader.readLine();

        String t = bufferedReader.readLine();

        int k = Integer.parseInt(bufferedReader.readLine().trim());

        String result = Result.appendAndDelete(s, t, k);

        bufferedWriter.write(result);
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
