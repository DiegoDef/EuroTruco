package objects.trucoPoints;

import objects.EuroTruco;
import objects.TrucoTeam;

public abstract class TrucoPoints {

    protected final EuroTruco euroTruco;
    private final Integer points;
    private TrucoTeam lastTeamAskedForTruco;

    public TrucoPoints(Integer points, EuroTruco euroTruco) {
        this.points = points;
        this.euroTruco = euroTruco;
    }

    public boolean askForTruco(TrucoTeam teamAskedForTruco) {
        if (teamAskedForTruco != this.lastTeamAskedForTruco && points < 12) {
            this.lastTeamAskedForTruco = teamAskedForTruco;

            TrucoPoints nextTrucoPoints = this.getNextTruco();
            euroTruco.setTrucoPoints(nextTrucoPoints);
            return true;
        }
        return false;
    }

    public abstract TrucoPoints getNextTruco();

    public Integer getPoints() {
        return this.points;
    }
}
