package objects.trucoPoints;

import objects.EuroTruco;

public class TrucoThreePoints extends TrucoPoints {

    private TrucoPoints nextTrucoPoints;

    public TrucoThreePoints(EuroTruco euroTruco) {
        super(3, euroTruco);
    }

    @Override
    public TrucoPoints getNextTruco() {
        if(nextTrucoPoints == null) {
            this.nextTrucoPoints = new TrucoSixPoints(euroTruco);
        }
        return this.nextTrucoPoints;
    }
}
