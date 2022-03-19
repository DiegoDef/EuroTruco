import objects.EuroTruco;
import objects.Player;

import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

import static utils.Validation.getValidAmountOfPlayersToPlayTruco;
import static utils.Validation.getValidName;

public class PlayEuroTruco {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("""
                ============= Seja Bem-Vindo(a) ao =============
                ============= Euro Truco Simulator® ===========

                """);

        System.out.print("A partida poderá ter 2 ou 4 jogadores no total. \n" +
                           "Antes de começar, informe a quantidade de participantes (2 ou 4): ");
        int amountPlayers = getValidAmountOfPlayersToPlayTruco(sc);

        Set<Player> players = createPlayers(amountPlayers);
        players.forEach(System.out::println);

        System.out.println("""
                As CARtas de todos os jogadores foram gravadas em .txt na pasta 'cartas' com o nome de cada um dos jogadores.
                Cada jogador deve ter acesso apenas ao seu arquivo.
                A cada rodada o arquivo é atualizado com as novas CARtas.
                A partida vai começar, peguem suas CARtas e prepare-se para a batalha!""");

        EuroTruco euroTruco = new EuroTruco(players);
        euroTruco.play(sc);

        sc.close();
    }

    public static Set<Player> createPlayers(int amountPlayers) {
        Scanner sc = new Scanner(System.in);
        Set<Player> players = new HashSet<>();

        for (int count=0; count < amountPlayers; count ++) {
            System.out.printf("Informe o nome do(a) jogador(a) número %d: \n", (count + 1));

            String name = getValidName(sc);
            players.add(new Player(name));
        }

        return players;
    }
}
