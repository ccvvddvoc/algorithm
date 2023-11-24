import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Array {
    public static void main(String[] args) {
        // 1. 배열 선언 및 초기화
        int[] scores = {95, 100, 87, 91};
        scores[2] = 90;

        System.out.println(scores);
        for (int i=0; i<scores.length; i++) {
            System.out.println(scores[i]);
        }
        // 2. 배열 메소드 
        String cars[] = {"hyundai", "bmw", "benz", "toyota"};
        List<String> car_list = Arrays.asList(cars); // 고정 배열
        System.out.println(car_list);
        System.out.println(car_list.get(1)); 

        Arrays.sort(cars);
        System.out.println(Arrays.asList(cars));

        Arrays.sort(cars, Collections.reverseOrder());
        System.out.println(Arrays.asList(cars));

        Arrays.sort(cars, 0, 2);
        System.out.println(Arrays.asList(cars));

        String cars_copied1[] = Arrays.copyOf(cars, cars.length);
        System.out.println(Arrays.asList(cars_copied1));

        String cars_copied2[] = Arrays.copyOfRange(cars,0,2);
        System.out.println(Arrays.asList(cars_copied2));

        // 3. 3차원 배열
        int[][][] allScores = {
            {{1,2,3}, {4,5,6}, {7,8,9}},
            {{10,11,12}, {13,14,15}, {16,17,18}},
            {{19,20,21}, {22,23,24}, {25,26,27}} 
        };
        System.out.println(allScores[1][2][0]);
        
    }
}
