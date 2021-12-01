import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Part1 {

    public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("input2.txt"));
        String mask = parseMask(scanner.nextLine());
        Map<Integer, Long> addresses = new HashMap<>();
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            if (line.startsWith("mask")) {
                mask = parseMask(line);
            } else {
                String[] split = line.replace("mem[", "").replace("] = ", ",").split(",");
                int index = Integer.parseInt(split[0]);
                long num = Long.parseLong(split[1]);
                addresses.put(index, applyMask(mask, num));
            }
        }
        System.out.println(addresses.values().stream().reduce(0L, Long::sum));
    }

    private static String parseMask(String line) {
        return line.replace("mask = ", "");
    }

    private static long applyMask(String mask, long num) {
        StringBuilder rawLong = new StringBuilder(fillWithLeftZeros(Long.toBinaryString(num), 36));
        for (int i = 0; i < mask.length(); i++) {
            if (mask.charAt(i) == '0') {
                rawLong.setCharAt(i, '0');
            } else if (mask.charAt(i) == '1') {
                rawLong.setCharAt(i, '1');
            }
        }
        return Long.parseLong(rawLong.toString(), 2);
    }

    private static String fillWithLeftZeros(String binary, int length) {
        StringBuilder builder = new StringBuilder(binary);
        for (int i = 0; i < length - binary.length(); i++) {
            builder.insert(0, "0");
        }
        return builder.toString();
    }
}
