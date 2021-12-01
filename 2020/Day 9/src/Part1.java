import java.io.File;
import java.io.FileNotFoundException;
import java.math.BigInteger;
import java.util.*;

public class Part1 {

    private static final int PREAMBLE = 25;

    public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("input2.txt"));
        Set<BigInteger> computes = new HashSet<>();
        List<BigInteger> numbers = new ArrayList<>();
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            BigInteger number = new BigInteger(line);
            numbers.add(number);
            if (numbers.size() > PREAMBLE) {
                if (!computes.isEmpty() && !computes.contains(number)) {
                    System.out.println(number);
                    break;
                }
                computes = calculateComputes(numbers);
            }
        }
    }

    private static Set<BigInteger> calculateComputes(List<BigInteger> numbers) {
        Set<BigInteger> computes = new HashSet<>();
        for (int i = numbers.size() - 1; i >= numbers.size() - PREAMBLE; i--) {
            for (int j = numbers.size() - 1; j >= numbers.size() - PREAMBLE; j--) {
                if (i != j) {
                    computes.add(numbers.get(i).add(numbers.get(j)));
                }
            }
        }
        return computes;
    }
}
