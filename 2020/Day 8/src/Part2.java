import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Part2 {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("input2.txt"));
        List<String> instructions = new ArrayList<>();
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            instructions.add(line);
        }
        System.out.println(executeInstructions(instructions, 0, 0, new ArrayList<>(), new ArrayList<>(), new HashMap<>()));
    }

    private static int executeInstructions(List<String> instructions, int accumulator, int i, List<Integer> visited, List<Integer> exhausted, Map<Integer, Integer> accumulatorCache) {
        if (i >= instructions.size()) {
            return accumulator;
        }
        if (visited.contains(i)) {
            for (int i1 = visited.size() - 1; i1 >= 0; i1--) {
                int index = visited.get(i1);
                Map.Entry<String, Integer> instruction = parseInstruction(instructions.get(index));
                boolean isNop = instruction.getKey().equals("nop");
                boolean isJmp = instruction.getKey().equals("jmp");
                if (!exhausted.contains(index) && (isNop || isJmp)) {
                    exhausted.add(index);
                    if (isNop) {
                        return executeInstructions(instructions, accumulatorCache.get(index), index + instruction.getValue(), visited, exhausted, accumulatorCache);
                    } else {
                        return executeInstructions(instructions, accumulatorCache.get(index), index + 1, visited, exhausted, accumulatorCache);
                    }
                }
            }
            return accumulator;
        }
        Map.Entry<String, Integer> instruction = parseInstruction(instructions.get(i));
        visited.add(i);
        accumulatorCache.put(i, accumulator);
        if (instruction.getKey().equals("acc")) {
            return executeInstructions(instructions, accumulator + instruction.getValue(), i + 1, new ArrayList<>(visited), exhausted, accumulatorCache);
        } else if (instruction.getKey().equals("nop")) {
            return executeInstructions(instructions, accumulator, i + 1, new ArrayList<>(visited), exhausted, accumulatorCache);
        } else if (instruction.getKey().equals("jmp")) {
            return executeInstructions(instructions, accumulator, i + instruction.getValue(), new ArrayList<>(visited), exhausted, accumulatorCache);
        }
        return accumulator;
    }

    private static Map.Entry<String, Integer> parseInstruction(String raw) {
        String[] split = raw.split(" ");
        return new AbstractMap.SimpleEntry<>(split[0], Integer.parseInt(split[1].replace("+", "")));
    }
}
