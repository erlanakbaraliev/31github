package Task_1;

public class ArrayUtilStructure {
    public static int max(int[] arr) {
        if (arr.length == 0) {
            return 0;
        }

        int max_value = Integer.MIN_VALUE;
        for (int numb : arr) {
            if (numb > max_value) {
                max_value = numb;
            }
        }
        return max_value;
    }

    public static int max2(int[] arr) {
        if (arr.length == 0) {
            return 0;
        }

        int max_value = Integer.MIN_VALUE;
        for (int numb : arr) {
            max_value = numb > max_value? numb: max_value;
        }
        return max_value;
    }

    public static int max3(int[] arr) {
        if (arr.length == 0) {
            return 0;
        }

        int max_value = Integer.MIN_VALUE;
        for (int numb : arr) {
            max_value = Math.max(numb, max_value);
        }
        return max_value;
    }

    public static int[] minMax(int[] arr) {
        if (arr.length == 0) {
            int[] empty = {0, 0};
            return empty;
        }

        int min_value = Integer.MAX_VALUE;
        for (int numb : arr) {
            min_value = Math.min(numb, min_value);
        }

        int max_value = max(arr);

        int[] minMaxArr = new int[2];
        minMaxArr[0] = min_value;
        minMaxArr[1] = max_value;

        return minMaxArr;
    }
}
