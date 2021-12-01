import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Part2 {

    public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("input3.txt"));
        List<Integer> adapterNumbers = new ArrayList<>();
        while (scanner.hasNextInt()) {
            adapterNumbers.add(scanner.nextInt());
        }
        boolean[] adapters = new boolean[Collections.max(adapterNumbers) + 1];
        for (Integer integer : adapterNumbers) {
            adapters[integer] = true;
        }
        long[] visited = new long[adapters.length + 3];
        visited[1] = adapters[1] ? 1 : 0;
        visited[2] = adapters[2] ? 1 : 0;
        visited[3] = adapters[3] ? 1 : 0;

        for (int i = 0; i < adapters.length; i++) {
            for (int j = 1; j <= 3; j++) {
                if (i - j > 0 && adapters[i]) {
                    visited[i] += visited[i - j];
                }
            }
        }
        for (int i = 0; i < visited.length - adapters.length; i++) {
            visited[adapters.length + i] += visited[2 * adapters.length - visited.length + i];
        }

        System.out.println(visited[adapters.length + 2]);
    }
}
