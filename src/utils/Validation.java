package utils;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Validation {

    public static int getValidAmountOfPlayersToPlayTruco(Scanner sc) {
        int amountPlayers = 0;

        try {
            amountPlayers = sc.nextInt();
            if (amountPlayers != 2 && amountPlayers != 4) {
                throw new InputMismatchException();
            }
        } catch (InputMismatchException e) {
            System.out.println("\nEntrada inválida, a quantidade de participantes deve ser de 2 ou 4.");
            System.out.println("informe a quantidade de participantes: ");
            getValidAmountOfPlayersToPlayTruco(sc);
        }

        return amountPlayers;

    }

    public static String getValidName(Scanner sc) {
        String name = "";

        try {
            name = sc.nextLine();
        } catch (InputMismatchException e) {
            System.out.print("\nEntrada inválida, informe um nome válido: ");
            getValidName(sc);
        }

        return name;
    }
}
