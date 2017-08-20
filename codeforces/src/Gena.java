import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.io.IOException;
import java.util.StringTokenizer;

public class Gena{
public static void main(String[]args){
        MyScanner sc=new MyScanner();
        out=new PrintWriter(new BufferedOutputStream(System.out));

        // Start writing your solution here. -------------------------------------

      int n      = Integer.parseInt(sc.nextLine());        // read input as integer
      int num = 1, cnt  = 0;

      String[] line = sc.nextLine().split(" ");
      boolean inspect= true;

      for(int i = 0; i < n; i++) {
        if (line[i].charAt(0) == '0')
        {
          num = cnt = 0;
          break;
        }
        if (inspect) {
          int ones = 0;
          String k     = line[i];       // read input as long
          for(int j = 0; j < line[i].length(); j++) {
            if (k.charAt(j) != '1' && k.charAt(j) != '0') {
              num = Integer.parseInt(k);
              inspect = false;
            }
            else if (k.charAt(j) == 1){
              ones += 1;
              if (ones == 2) {
                num = Integer.parseInt(k);
                inspect = false;
              }
            }
          }
        }
        else {
          cnt += line[i].length() - 1;
        }
      }

      out.print(num);                    // print via PrintWriter
      for(int i = 0; i < cnt; i++){
        out.print('0');
      }

        // Stop writing your solution here. -------------------------------------
        out.close();
        }


//-----------PrintWriter for faster output---------------------------------
public static PrintWriter out;

//-----------MyScanner class for faster input----------
public static class MyScanner {
  BufferedReader br;
  StringTokenizer st;

  public MyScanner() {
    br = new BufferedReader(new InputStreamReader(System.in));
  }

  String next() {
    while (st == null || !st.hasMoreElements()) {
      try {
        st = new StringTokenizer(br.readLine());
      } catch (IOException e) {
        e.printStackTrace();
      }
    }
    return st.nextToken();
  }

  int nextInt() {
    return Integer.parseInt(next());
  }

  long nextLong() {
    return Long.parseLong(next());
  }

  double nextDouble() {
    return Double.parseDouble(next());
  }

  String nextLine() {
    String str = "";
    try {
      str = br.readLine();
    } catch (IOException e) {
      e.printStackTrace();
    }
    return str;
  }

}
//--------------------------------------------------------
}