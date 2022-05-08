package objects.trucoPoints;

import objects.EuroTruco;

public class InitialPoints extends TrucoPoints {

    private TrucoPoints nextTrucoPoints;

    public InitialPoints(EuroTruco euroTruco) {
        super(1, euroTruco);
    }

    @Override
    public TrucoPoints getNextTruco() {
        if(nextTrucoPoints == null) {
            this.nextTrucoPoints = new TrucoThreePoints(euroTruco);
        }
        return this.nextTrucoPoints;
    }
}
