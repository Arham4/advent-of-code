import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Part1 {

    public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("input2.txt"));
        Map<String, List<String>> bagsContainingBag = new HashMap<>();
        while (scanner.hasNextLine()) {
            String[] line = scanner.nextLine().split(" contain ");
            List<String> contains = new ArrayList<>();
            Collections.addAll(contains, line[1].split(", "));
            for (String contain : contains) {
                String key = removeEnglish(omitNumber(contain));
                bagsContainingBag.putIfAbsent(key, new ArrayList<>());
                bagsContainingBag.get(key).add(removeEnglish(line[0]));
            }
        }
        System.out.println(getNumber(bagsContainingBag, new ArrayList<>(), "shiny gold bag"));
    }

    private static int getNumber(Map<String, List<String>> rules, List<String> visited, String key) {
        List<String> others = rules.get(key);
        if (others == null) {
            return 0;
        }
        for (String o : others) {
            String other = removeEnglish(o);
            if (!visited.contains(other)) {
                visited.add(other);
                getNumber(rules, visited, other);
            }
        }
        return visited.size();
    }

    private static String omitNumber(String str) {
        int index = 0;
        while (Character.isDigit(str.charAt(index++)));
        return str.substring(index);
    }

    private static String removeEnglish(String str) {
        return str.replace("bags", "bag").replace(".", "");
    }
}