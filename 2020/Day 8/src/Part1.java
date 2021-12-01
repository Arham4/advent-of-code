import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Part1 {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("input1.txt"));
        List<String> instructions = new ArrayList<>();
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            instructions.add(line);
        }
        System.out.println(executeInstructions(instructions, 0, 0, new ArrayList<>()));
    }

    private static int executeInstructions(List<String> instructions, int accumulator, int i, List<Integer> visited) {
        if (visited.contains(i)) {
            return accumulator;
        }
        Map.Entry<String, Integer> instruction = parseInstruction(instructions.get(i));
        visited.add(i);
        if (instruction.getKey().equals("nop")) {
            return executeInstructions(instructions, accumulator, i + 1, visited);
        } else if (instruction.getKey().equals("acc")) {
            return executeInstructions(instructions, accumulator + instruction.getValue(), i + 1, visited);
        } else if (instruction.getKey().equals("jmp")) {
            return executeInstructions(instructions, accumulator, i + instruction.getValue(), visited);
        }
        return accumulator;
    }

    private static Map.Entry<String, Integer> parseInstruction(String raw) {
        String[] split = raw.split(" ");
        return new AbstractMap.SimpleEntry<>(split[0], Integer.parseInt(split[1].replace("+", "")));
    }
}
