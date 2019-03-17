import java.io.*;
import java.util.Stack;
import java.util.StringTokenizer;

public class CHDIGER {

    public static void main (String[] args) {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter printWriter = new PrintWriter(System.out);

        try {
            int t = Integer.parseInt(bufferedReader.readLine());
            // 6874654654 4

            while (t != 0) {

                StringBuilder output = new StringBuilder();

                String input = bufferedReader.readLine();
                StringTokenizer tk = new StringTokenizer(input);

                String num = tk.nextToken();
                String d = tk.nextToken();

                if (findMin(Long.parseLong(num)) > Long.parseLong(d)) {
                    for (int i = 0; i<num.length(); i++) {
                        output.append(d);
                    }

                    printWriter.println(output);
                    printWriter.flush();
                } else {
                    StringBuilder temp = new StringBuilder(num);

                    for (int i=0; i<num.length(); i++) {
                        temp.append(d);
                    }

                    temp = minimizeNumber(temp.toString(), num.length());

                    printWriter.println(temp.toString());
                    printWriter.flush();
                }

                --t;
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static long findMin(long n){
        if(n < 10) return n;
        return Math.min(n%10, findMin(n/10));
    }

    private static StringBuilder minimizeNumber(String num, int k) {

        int len = num.length();

        if (len == k) {
            return new StringBuilder(num);
        }

        Stack<Character> stack = new Stack<>();
        int i =0;
        while(i<num.length()){
            //whenever meet a digit which is less than the previous digit, discard the previous one
            while(k>0 && !stack.isEmpty() && stack.peek()>num.charAt(i)){
                stack.pop();
                k--;
            }
            stack.push(num.charAt(i));
            i++;
        }

        // corner case like "1111"
        while(k>0){
            stack.pop();
            k--;
        }

        //construct the number from the stack
        StringBuilder sb = new StringBuilder();
        while(!stack.isEmpty())
            sb.append(stack.pop());
        sb.reverse();

        //remove all the 0 at the head
        while(sb.length()>1 && sb.charAt(0)=='0')
            sb.deleteCharAt(0);
        return sb;
    }
}
