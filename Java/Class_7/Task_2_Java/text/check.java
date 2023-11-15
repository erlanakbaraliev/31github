import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class check {
    public static void main(String[] args) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("writer.txt")))
        {
            String input = "23";
            if (isInteger(input)) {
                writer.write(input);
            }
        } catch (IOException e) {
            System.out.println("IOExceptin occured: " + e);
        }
    }

    public static boolean isInteger(String input) {
        try {
            Integer.parseInt(input);
            return true;
        } catch(NumberFormatException e) {
            return false;
        }
    }
}
