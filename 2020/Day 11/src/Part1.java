import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Part1 {

    private static final int[][] OFFSETS = {
            {0, 1},
            {0, -1},
            {1, 0},
            {-1, 0},
            {1, 1},
            {1, -1},
            {-1, 1},
            {-1, -1}
    };

    public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("input2.txt"));
        List<String> gridRaw = new ArrayList<>();
        while (scanner.hasNextLine()) {
            gridRaw.add(scanner.nextLine());
        }
        char[][] grid = new char[gridRaw.size()][gridRaw.get(0).length()];
        for (int y = 0; y < gridRaw.size(); y++) {
            for (int x = 0; x < grid[y].length; x++) {
                grid[y][x] = gridRaw.get(y).charAt(x);
            }
        }
        Queue<Change> changes = new ArrayDeque<>();
        do {
            applyChanges(grid, changes);
            stabilize(grid, changes);
        } while (!changes.isEmpty());
        int occupied = 0;
        for (char[] row : grid) {
            for (char col : row) {
                if (col == '#') {
                    occupied += 1;
                }
            }
        }
        System.out.println(occupied);
    }

    private static void applyChanges(char[][] grid, Queue<Change> changes) {
        while (!changes.isEmpty()) {
            Change change = changes.poll();
            grid[change.y][change.x] = change.to;
        }
    }

    private static void stabilize(char[][] grid, Queue<Change> changes) {
        for (int y = 0; y < grid.length; y++) {
            for (int x = 0; x < grid[y].length; x++) {
                if (grid[y][x] == 'L' && countAdjacentOccupied(grid, y, x) == 0) {
                    changes.add(Change.to(y, x, '#'));
                } else if (grid[y][x] == '#' && countAdjacentOccupied(grid, y, x) >= 4) {
                    changes.add(Change.to(y, x, 'L'));
                }
            }
        }
    }

    private static int countAdjacentOccupied(char[][] grid, int y, int x) {
        int occupied = 0;
        for (int[] offset : OFFSETS) {
            try {
                if (grid[y + offset[1]][x + offset[0]] == '#') {
                    occupied += 1;
                }
            } catch (Exception e) { }
        }
        return occupied;
    }

    private static class Change {
        private final int y;
        private final int x;
        private final char to;

        private static Change to(int y, int x, char to) {
            return new Change(y, x, to);
        }

        private Change(int y, int x, char to) {
            this.y = y;
            this.x = x;
            this.to = to;
        }
    }
}
