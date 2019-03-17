import java.io.*;

public class JAIN {

    public static void main(String[] args) {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter printWriter = new PrintWriter(System.out);

        try {
            int t = Integer.parseInt(bufferedReader.readLine());

            while (t != 0) {
                int n = Integer.parseInt(bufferedReader.readLine());
                String[] arrayList = new String[n];

                for (int i=0; i<n; i++) {
                    arrayList[i] = bufferedReader.readLine();
                }

                String[] intArray = convertToInteger(arrayList);

                int total_pairs = countPair(intArray);

                printWriter.println(total_pairs);
                printWriter.flush();

                --t;
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static int countPair(String[] arr) {
        int[] cnt = new int[32];

        for (String s : arr) {
            int mask = 0;
            for (int j = 0; j < s.length(); j++) {
                mask |= (1 << (s.charAt(j) - '0'));
            }
            cnt[mask]++;
        }

        int ans = 0;
        for (int m1 = 0; m1 <= 31; m1++) {
            for (int m2 = 0; m2 <= 31; m2++) {
                if ((m1 | m2) == 31) {
                    ans += ((m1 == m2) ?
                            (cnt[m1] * (cnt[m1] - 1)) :
                            (cnt[m1] * cnt[m2]));
                }
            }
        }

        return ans/2;
    }

    private static String[] convertToInteger(String[] arrayList) {

        String[] arr = new String[arrayList.length];

        for (int i=0; i < arrayList.length; i++) {

            StringBuilder s = new StringBuilder();

            for (int j=0; j<arrayList[i].length(); j++) {
                if (arrayList[i].charAt(j) == 'a') {
                    s.append("0");
                } else if (arrayList[i].charAt(j) == 'e') {
                    s.append("1");
                } else if (arrayList[i].charAt(j) == 'i') {
                    s.append("2");
                } else if (arrayList[i].charAt(j) == 'o') {
                    s.append("3");
                } else {
                    s.append("4");
                }
            }

            arr[i] = s.toString();
        }

        return arr;
    }

}
