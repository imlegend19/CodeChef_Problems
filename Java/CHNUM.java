import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class CHNUM {

    public static void main(String[] args) {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter printWriter = new PrintWriter(System.out);

        int num;
        ArrayList<Integer> score = new ArrayList<>();

        try {
            int t = Integer.parseInt(bufferedReader.readLine());
            int temp;

            while (t != 0) {
                num = Integer.parseInt(bufferedReader.readLine());
                String score_string = bufferedReader.readLine();
                int negative_length = 0;

                StringTokenizer tokenizer = new StringTokenizer(score_string);
                while (num != 0) {
                    temp = Integer.parseInt(tokenizer.nextToken());
                    score.add(temp);
                    if (temp < 0) {
                        negative_length++;
                    }
                    --num;
                }

                if (negative_length == 0) {
                    printWriter.println(score.size() + " " + score.size());
                    printWriter.flush();
                } else {
                    printWriter.println((score.size() - negative_length) + " " + negative_length);
                    printWriter.flush();
                }

                score.clear();
                --t;
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
