package objects.trucoPoints;

import objects.TrucoTeam;

public class InitialPoints extends TrucoPoints {

    public InitialPoints() {
        super(1); // 1 == initialPoints
    }

    @Override
    public void askForTruco(TrucoTeam teamAskedForTruco) {
        // não há validação para quando ainda não houve pedido de truco, apenas atribuir próximo truco
    }
}
