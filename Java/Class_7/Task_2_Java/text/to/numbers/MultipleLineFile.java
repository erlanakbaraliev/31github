package Task_2.text.to.numbers;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.BufferedWriter;


public class MultipleLineFile {
    public static int addNumbers(String filename, String seperator) throws IOException {
        try (BufferedReader file = new BufferedReader(new FileReader(filename))) {
            BufferedWriter str_file = new BufferedWriter(new FileWriter("Task_2/text/to/numbers/str_file.txt"));
                String line;
                int sum_line = 0;

                while ((line = file.readLine()) != null){
                    if (line.isEmpty()) {
                        throw new IllegalArgumentException("Empty file");
                    }
                    String[] pars = line.split(" ");
                    for (String elem: pars) {
                        if (isInteger(elem)) {
                            sum_line += Integer.parseInt(elem);
                        }
                        else {
                            System.out.println(elem);
                            str_file.write(elem);
                        }
                    }
                }
                return sum_line;
        } catch (FileNotFoundException e) {
            throw new FileNotFoundException("File Not Found");
        }
    }
    public static boolean isInteger(String input) {
        try {
            Integer.parseInt(input);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }
}
