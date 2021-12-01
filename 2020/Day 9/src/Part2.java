import java.io.File;
import java.io.FileNotFoundException;
import java.math.BigInteger;
import java.util.*;

public class Part2 {

    private static final int PREAMBLE = 25;

    public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("input2.txt"));
        Map<BigInteger, List<BigInteger>> possibleNumbersStartingFrom = new LinkedHashMap<>();
        Set<BigInteger> computes = new HashSet<>();
        List<BigInteger> numbers = new ArrayList<>();
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            BigInteger number = new BigInteger(line);
            numbers.add(number);
            if (numbers.size() > PREAMBLE) {
                if (!computes.isEmpty() && !computes.contains(number)) {
                    Map.Entry<BigInteger, Integer> start = findBeginningOfChain(possibleNumbersStartingFrom, number);
                    if (start != null) {
                        int startIndex = numbers.indexOf(start.getKey());
                        List<BigInteger> chain = numbers.subList(startIndex, startIndex + start.getValue());
                        BigInteger max = chain.stream().max(BigInteger::compareTo).get();
                        BigInteger min = chain.stream().min(BigInteger::compareTo).get();
                        System.out.println(max.add(min));
                    }
                    break;
                }
                computes = calculateComputes(numbers);
            }
            addLink(possibleNumbersStartingFrom, number);
        }
    }

    private static void addLink(Map<BigInteger, List<BigInteger>> possibleNumbersStartingFrom, BigInteger number) {
        possibleNumbersStartingFrom.values().forEach(list -> list.add(number.add(list.get(list.size() - 1))));
        possibleNumbersStartingFrom.put(number, new ArrayList<>());
        possibleNumbersStartingFrom.get(number).add(number);
    }

    private static Map.Entry<BigInteger, Integer> findBeginningOfChain(Map<BigInteger, List<BigInteger>> possibleNumbersStartingFrom, BigInteger number) {
        for (Map.Entry<BigInteger, List<BigInteger>> entry : possibleNumbersStartingFrom.entrySet()) {
            if (entry.getValue().contains(number)) {
                return new AbstractMap.SimpleEntry<>(entry.getKey(), entry.getValue().indexOf(number));
            }
        }
        return null;
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
