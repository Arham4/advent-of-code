import java.io.File;
import java.io.FileNotFoundException;
import java.math.BigInteger;
import java.util.*;
import java.util.stream.Collectors;

public class Part2 {

    public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("input2.txt"));
        List<BigInteger> ids = Arrays.stream(scanner.nextLine().split(",")).map(s -> s.equals("x") ? null : new BigInteger(s)).collect(Collectors.toList());

        BigInteger num = chineseRemainderTheorem(ids);
        System.out.println(num);
    }

    private static BigInteger chineseRemainderTheorem(List<BigInteger> ids) {
        BigInteger sum = BigInteger.ZERO;
        BigInteger n = ids.stream().reduce(BigInteger.ONE, (identity, acc) -> acc == null ? identity : identity.multiply(acc));
        for (int i = 0; i < ids.size(); i++) {
            if (ids.get(i) == null) {
                continue;
            }
            BigInteger bi = ids.get(i).subtract(BigInteger.valueOf(i));
            BigInteger ni = n.divide(ids.get(i));
            BigInteger xi = getX(ni.mod(ids.get(i)), ids.get(i));
            if (xi != null) {
                sum = sum.add(bi.multiply(ni).multiply(xi));
            }
        }
        return sum.mod(n);
    }

    private static BigInteger getX(BigInteger normalized, BigInteger mod) {
        BigInteger i = BigInteger.ONE;
        while (!i.multiply(normalized).mod(mod).equals(BigInteger.ONE)) {
            i = i.add(BigInteger.ONE);
        }
        return i;
    }
}
