import java.io.File;
import java.util.Scanner;
import java.io.InputStream;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintStream;
// import java.io.FileNotFoundException;

public class atoi {

	public static void main(String[] args) {
    File fin = new File("//Users//anhbui//Google Drive//CompPrgming//input.txt");
    File fout = new File("output.txt");
    InputStream inputStream = new FileInputStream(fin);
    // OutputStream outputStream = new FileOutputStream(fout);
    System.setIn(inputStream);
    System.setOut(new PrintStream(fout));
    Scanner in = new Scanner(System.in);
    // BufferedWriter out = new BufferedWriter(new OutputStreamWriter(outputStream));
    String s = in.nextLine();
    System.out.println(s);
    // fout.write(s);
    // fout.close();
	}
}
