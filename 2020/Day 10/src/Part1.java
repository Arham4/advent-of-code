import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Part1 {

    public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("input3.txt"));
        List<Integer> list = new ArrayList<>();
        while (scanner.hasNextInt()) {
            list.add(scanner.nextInt());
        }
        boolean[] adapters = new boolean[Collections.max(list) + 1];
        for (Integer integer : list) {
            adapters[integer] = true;
        }
        Map.Entry<Integer, Integer> pair = recurse(adapters,0, 0, 0);
        System.out.println(pair.getKey() * pair.getValue());
    }

    private static Map.Entry<Integer, Integer> recurse(boolean[] adapters, int currentJolts, int oneJolts, int threeJolts) {
        if (currentJolts == adapters.length + 2) {
            return new AbstractMap.SimpleEntry<>(oneJolts, threeJolts);
        }
        if (currentJolts == adapters.length - 1) {
            return recurse(adapters, currentJolts + 3, oneJolts, threeJolts + 1);
        }
        if (adapters[currentJolts + 1]) {
            return recurse(adapters, currentJolts + 1, oneJolts + 1, threeJolts);
        } else if (adapters[currentJolts + 2]) {
            return recurse(adapters, currentJolts + 2, oneJolts, threeJolts);
        } else if (adapters[currentJolts + 3]) {
            return recurse(adapters, currentJolts + 3, oneJolts, threeJolts + 1);
        }
        return null;
    }
}
