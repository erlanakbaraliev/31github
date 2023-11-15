package Task_2.text;
import Task_2.text.to.numbers.MultipleLineFile;
import java.io.IOException;


public class Main {
    public static void main(String[] args) {
        try {
            int result = MultipleLineFile.addNumbers("Task_2/text/file.txt", " ");
            System.out.println(result);
        } catch (IOException e) {
            System.out.println(e);
        }
    }
}
