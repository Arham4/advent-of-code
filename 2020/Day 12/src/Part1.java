import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Part1 {

    public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("input2.txt"));
        double x = 0;
        double y = 0;
        int degrees = 0;
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            char type = line.charAt(0);
            int magnitude = Integer.parseInt(line.substring(1));
            if (type == 'F') {
                x += Math.cos(Math.toRadians(degrees)) * magnitude;
                y += Math.sin(Math.toRadians(degrees)) * magnitude;
            } else if (type == 'R') {
                degrees -= magnitude;
            } else if (type == 'L') {
                degrees += magnitude;
            } else if (type == 'W') {
                x -= magnitude;
            } else if (type == 'E') {
                x += magnitude;
            } else if (type == 'S') {
                y -= magnitude;
            } else if (type == 'N') {
                y += magnitude;
            }
        }
        System.out.println(manhattanDistance(x, y));
    }

    private static double manhattanDistance(double x, double y) {
        return Math.abs(x) + Math.abs(y);
    }
}
