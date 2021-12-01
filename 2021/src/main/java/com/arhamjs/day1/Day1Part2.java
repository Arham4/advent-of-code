package com.arhamjs.day1;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Day1Part2 {

    public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("./data/day1/input.txt"));
        int increases = 0;
        List<Integer> previousNumbers = new ArrayList<>(List.of(scanner.nextInt(), scanner.nextInt(), scanner.nextInt()));
        while (scanner.hasNextInt()) {
            int previousSum = previousNumbers.stream().reduce(0, Integer::sum);
            previousNumbers.remove(0);
            previousNumbers.add(scanner.nextInt());
            int currentSum = previousNumbers.stream().reduce(0, Integer::sum);
            if (currentSum > previousSum) {
                increases++;
            }
        }
        System.out.println(increases);
    }
}
