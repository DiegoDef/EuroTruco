package objects.trucoPoints;

import objects.TrucoTeam;

public abstract class TrucoPoints {
    protected final Integer points;
    protected TrucoTeam lastTeamAskedForTruco;

    public TrucoPoints(Integer points) {
        this.points = points;
    }

    public void askForTruco(TrucoTeam teamAskedForTruco) {
        if (teamAskedForTruco != lastTeamAskedForTruco) {
            //aumentar truco
        }
        // o mesmo time que pediu truco pela ultima vez nao pode pedir de novo
    }

    public Integer getPoints() {
        return this.points;
    }
}
