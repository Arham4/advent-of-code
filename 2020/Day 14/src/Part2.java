import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.function.Consumer;
import java.util.function.Function;

public class Part2 {

    public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("input2.txt"));
        String mask = parseMask(scanner.nextLine());
        Map<Long, Long> addresses = new HashMap<>();
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            if (line.startsWith("mask")) {
                mask = parseMask(line);
            } else {
                String[] split = line.replace("mem[", "").split("] = ");
                String indexMask = getMaskedBinary(Long.toBinaryString(Long.parseLong(split[0])), mask);
                long num = Long.parseLong(split[1]);

                applyMaskedIndices(addresses, indexMask, num);
            }
        }
        System.out.println(addresses.values().stream().reduce(0L, Long::sum));
    }

    private static void applyMaskedIndices(Map<Long, Long> addresses, String indexMask, long num) {
        applyMaskedIndices(addresses, indexMask, num, 0);
    }

    private static void applyMaskedIndices(Map<Long, Long> addresses, String indexMask, long num, int index) {
        if (index >= indexMask.length()) {
            addresses.put(Long.parseLong(indexMask, 2), num);
            return;
        }
        if (indexMask.charAt(index) == 'X') {
            Consumer<String> next = b -> applyMaskedIndices(addresses, stringWithReplacedIndex(indexMask, index, b), num, index + 1);
            next.accept("0");
            next.accept("1");
        } else {
            applyMaskedIndices(addresses, indexMask, num, index + 1);
        }
    }

    private static String stringWithReplacedIndex(String str, int index, String replaceWith) {
        return str.substring(0, index) + replaceWith + str.substring(index + 1);
    }

    private static String parseMask(String line) {
        return line.replace("mask = ", "");
    }

    private static String getMaskedBinary(String binaryIn, String mask) {
        StringBuilder binary = new StringBuilder(fillWithLeftZeros(binaryIn, 36));
        for (int i = 0; i < mask.length(); i++) {
            if (mask.charAt(i) == 'X') {
                binary.setCharAt(i, 'X');
            } else if (mask.charAt(i) == '1') {
                binary.setCharAt(i, '1');
            }
        }
        return binary.toString();
    }

    private static String fillWithLeftZeros(String binary, int length) {
        StringBuilder builder = new StringBuilder(binary);
        for (int i = 0; i < length - binary.length(); i++) {
            builder.insert(0, "0");
        }
        return builder.toString();
    }
}
