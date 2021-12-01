import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;
import java.util.stream.Collectors;

public class Part1 {

    public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("input2.txt"));
        double time = scanner.nextInt();
        scanner.nextLine();
        List<Integer> ids = Arrays.stream(scanner.nextLine().split(",")).filter(s -> !s.equals("x")).map(Integer::parseInt).collect(Collectors.toList());
        Optional<Integer> highestNumber = ids.stream().max(Integer::compareTo);
        if (highestNumber.isPresent()) {
            Optional<Integer> highestModOptional = ids.stream().min(Comparator.comparingInt(o -> getEarliest(o, time)));
            double time2 = Math.ceil(time / highestModOptional.get()) * highestModOptional.get();
            double wait = time2 - time;
            System.out.println(highestModOptional.get() * wait);
        }
    }

    private static int getEarliest(int o, double time) {
        int num = 1;
        while (num * o < time) {
            num++;
        }
        return (int) (num * o - time);
    }
}
