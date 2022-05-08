package objects.trucoPoints;

import objects.EuroTruco;

public class TrucoNinePoints extends TrucoPoints {

    private TrucoPoints nextTrucoPoints;

    public TrucoNinePoints(EuroTruco euroTruco) {
        super(9, euroTruco);
    }

    @Override
    public TrucoPoints getNextTruco() {
        if(nextTrucoPoints == null) {
            this.nextTrucoPoints = new TrucoTwelvePoints(euroTruco);
        }
        return this.nextTrucoPoints;
    }
}
