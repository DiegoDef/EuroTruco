package objects;

import objects.trucoPoints.TrucoPoints;
import objects.trucoPoints.InitialPoints;

import java.util.Scanner;
import java.util.Set;

public class EuroTruco {
    private final Set<Player> players;
    private Integer teamPoints1 = 0;
    private Integer teamPoints2 = 0;
    private TrucoPoints trucoPoints = new InitialPoints();

    public EuroTruco(Set<Player> players) {
        this.players = players;
    }

    public void play(Scanner sc) {

    }

    public void addPointsToTeam1() {
        this.teamPoints1++;
    }

    public void addPointsToTeam2() {
        this.teamPoints2++;
    }
}
