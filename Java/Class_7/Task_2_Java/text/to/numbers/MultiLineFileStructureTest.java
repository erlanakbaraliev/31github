package Task_2.text.to.numbers;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
import java.io.IOException;

public class MultiLineFileStructureTest {
    @Test
    public void get_addNumbers_test() throws IOException {
        try {
            assertEquals(22, MultipleLineFile.addNumbers("text/file.txt", " "));
        } catch(IOException e) {
            System.out.println("IOException occured: " + e.getMessage());
        }
    }
}
