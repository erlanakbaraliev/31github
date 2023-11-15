package Task_1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import static org.junit.jupiter.api.Assertions.assertEquals;
import Task_1.ArrayUtilStructure;


public class ArrayUtilStructureTest {
    @Test
    public void maxLength0() {
        int[] empty_arr = {};
        assertEquals(0, ArrayUtilStructure.max(empty_arr));
        assertEquals(0, ArrayUtilStructure.max2(empty_arr));
        assertEquals(0, ArrayUtilStructure.max3(empty_arr));
    }

    @Test
    public void maxLength1() {
        int[] arr = {-21};
        assertEquals(arr[0], ArrayUtilStructure.max(arr));
        assertEquals(arr[0], ArrayUtilStructure.max2(arr));
        assertEquals(arr[0], ArrayUtilStructure.max3(arr));
    }

    @ParameterizedTest
    @CsvSource({
        "1, 2, 2",
        "5, 10, 10"
    })

    public void maxLength2(int min, int max, int expected) {
        int[] arr1 = {min, max};
        assertEquals(expected, ArrayUtilStructure.max(arr1));
        assertEquals(expected, ArrayUtilStructure.max(arr1));
    }

    @Test
    public void minMaxLengthN() {
        int[] arr = {21, -33};
        //assertEquals(expected, input);
        assertEquals(new int[]{-33,21}, ArrayUtilStructure.minMax(arr));
    }
}
