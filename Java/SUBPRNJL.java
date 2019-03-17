import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class SUBPRNJL {

    public static void main(String[] args) {

        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter printWriter = new PrintWriter(System.out);

        try {
            int t = Integer.parseInt(bufferedReader.readLine());
            int num, k;

            while (t != 0) {

                String input = bufferedReader.readLine();
                StringTokenizer tk = new StringTokenizer(input);

                num = Integer.parseInt(tk.nextToken());
                k = Integer.parseInt(tk.nextToken());

                ArrayList<Integer> array = new ArrayList<>();

                input = bufferedReader.readLine();
                tk = new StringTokenizer(input);

                while (tk.hasMoreTokens()) {
                    array.add(Integer.parseInt(tk.nextToken()));
                }

                printWriter.println(subArray(array, num, k));
                printWriter.flush();

                --t;
            }

        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    private static int subArray(ArrayList<Integer> a, int arrayLength, int k) {

        int count = 0;
        ArrayList<Tuple> taken = new ArrayList<>();

        for(int i = 0; i < arrayLength; i++) {

            StringBuilder s = new StringBuilder();

            for (int j = i; j < arrayLength; j++) {

                s.append(a.get(j)).append(" ");

                int l, r;

                if (s.toString().trim().contains(" ")) {
                    l = a.indexOf(Integer.parseInt(s.substring(0, s.indexOf(" "))));
                    r = a.indexOf(Integer.parseInt(s.toString().trim().substring(s.toString().trim().lastIndexOf(" ")+1)));
                } else {
                   r = l = a.indexOf(Integer.parseInt(s.toString().trim()));
                }

                if (!taken.contains(new Tuple<>(l, r))) {
                    ArrayList<Integer> arr = new ArrayList<>();

                    StringTokenizer tk = new StringTokenizer(s.toString());
                    while (tk.hasMoreTokens()) {
                        arr.add(Integer.parseInt(tk.nextToken()));
                    }

                    if(checkIfBeautiful(arr, k, a.indexOf(arr.get(0)), a.indexOf(arr.get(arr.size() - 1)))) {
                        ++count;
                    }

                    taken.add(new Tuple<>(l, r));
                }
            }
        }

        return count;
    }

    private static boolean checkIfBeautiful(ArrayList<Integer> arr, int k, int l, int r) {
        int m = (int) Math.ceil((double) k / (r - l + 1));

        int[] b = new int[arr.size()*m];

        int index = 0;
        for (int i = 0; i < m; ++i) {
            for (int i1 : arr) {
                b[index] = i1;
                ++index;
            }
        }

        Arrays.sort(b);
        int x = b[k-1];

        return arr.contains(x);
    }
}

class Tuple<X, Y> {
    private final X x;
    private final Y y;
    Tuple(X x, Y y) {
        this.x = x;
        this.y = y;
    }
}