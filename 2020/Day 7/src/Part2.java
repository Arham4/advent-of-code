import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Part2 {

    public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("input1.txt"));
        Map<String, List<Map.Entry<String, Integer>>> bagsContainingBag = new HashMap<>();
        while (scanner.hasNextLine()) {
            String[] line = scanner.nextLine().split(" contain ");
            List<String> contains = new ArrayList<>();
            Collections.addAll(contains, line[1].split(", "));

            String key = removeEnglish(line[0]);
            for (String contain : contains) {
                Map.Entry<String, Integer> pair = getNumberPair(removeEnglish(contain));

                bagsContainingBag.putIfAbsent(key, new ArrayList<>());
                bagsContainingBag.get(key).add(pair);
            }
        }
        System.out.println(getNumber(bagsContainingBag, "shiny gold bag"));
    }

    private static int getNumber(Map<String, List<Map.Entry<String, Integer>>> rules, String key) {
        List<Map.Entry<String, Integer>> others = rules.get(key);
        if (others == null) {
            return 0;
        }
        int count = addList(others);
        for (Map.Entry<String, Integer> other : others) {
            count += other.getValue() * getNumber(rules, other.getKey());
        }
        return count;
    }

    private static int addList(List<Map.Entry<String, Integer>> others) {
        int count = 0;
        for (Map.Entry<String, Integer> other : others) {
            count += other.getValue();
        }
        return count;
    }

    private static Map.Entry<String, Integer> getNumberPair(String str) {
        int index = 0;
        while (Character.isDigit(str.charAt(index++)));
        String rawNumber = str.substring(0, index - 1);
        int count = 0;
        if (!rawNumber.isEmpty()) {
            count = Integer.parseInt(rawNumber);
        }
        return new AbstractMap.SimpleEntry<>(str.substring(index), count);
    }

    private static String removeEnglish(String str) {
        return str.replace("bags", "bag").replace(".", "");
    }
}