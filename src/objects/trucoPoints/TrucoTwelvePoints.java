package objects.trucoPoints;

import objects.EuroTruco;

public class TrucoTwelvePoints extends TrucoPoints {

    public TrucoTwelvePoints(EuroTruco euroTruco) {
        super(12, euroTruco);
    }

    @Override
    public TrucoPoints getNextTruco() {
        // implementar exception
       return this;
    }
}
