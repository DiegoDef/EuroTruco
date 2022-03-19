package objects.trucoPoints;

public abstract class AbstractTrucoPoints {
    protected final Integer points;

    public AbstractTrucoPoints(Integer points) {
        this.points = points;
    }

    public Integer getPoints() {
        return this.points;
    }
}
