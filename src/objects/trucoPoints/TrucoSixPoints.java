package objects.trucoPoints;

import objects.EuroTruco;

public class TrucoSixPoints extends TrucoPoints {

    private TrucoPoints nextTrucoPoints;

    public TrucoSixPoints(EuroTruco euroTruco) {
        super(6, euroTruco);
    }

    @Override
    public TrucoPoints getNextTruco() {
        if(nextTrucoPoints == null) {
            this.nextTrucoPoints = new TrucoNinePoints(euroTruco);
        }
        return this.nextTrucoPoints;
    }
}
