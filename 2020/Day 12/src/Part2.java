import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Part2 {

    public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("input2.txt"));
        double shipX = 0;
        double shipY = 0;
        double waypointX = 10;
        double waypointY = 1;
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            char type = line.charAt(0);
            int magnitude = Integer.parseInt(line.substring(1));
            if (type == 'N') {
                waypointY += magnitude;
            } else if (type == 'S') {
                waypointY -= magnitude;
            } else if (type == 'E') {
                waypointX += magnitude;
            } else if (type == 'W') {
                waypointX -= magnitude;
            } else if (type == 'L' || type == 'R') {
                double temp = waypointY;
                double degrees = Math.toRadians(type == 'L' ? magnitude : -magnitude);
                double cos = Math.round(Math.cos(degrees));
                double sin = Math.round(Math.sin(degrees));
                waypointY = waypointY * cos + waypointX * sin;
                waypointX = -temp * sin + waypointX * cos;
            } else if (type == 'F') {
                shipX += waypointX * magnitude;
                shipY += waypointY * magnitude;
            }
        }
        System.out.println(manhattanDistance(shipX, shipY));
    }

    private static double manhattanDistance(double x, double y) {
        return Math.abs(x) + Math.abs(y);
    }
}
