package com.arhamjs.day1;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Day1Part1 {

    public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("./data/day1/input.txt"));
        int increases = 0;
        int previousNumber = scanner.nextInt();
        while (scanner.hasNextInt()) {
            int current = scanner.nextInt();
            if (current > previousNumber) {
                increases++;
            }
            previousNumber = current;
        }
        System.out.println(increases);
    }
}
