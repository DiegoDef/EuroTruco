package objects;

import java.util.List;

public class AskForTrucoManager {

    private List<Integer> allTrucoPoints = List.of(12, 9, 6, 3);
    private Integer currentTrucoPoint = 1;
    private TrucoTeam lastTeamAskedTruco;

    public void askForTruco(TrucoTeam trucoTeam) {
        if (this.currentTrucoPoint == 12 || trucoTeam == this.lastTeamAskedTruco) {
            System.out.println("Não é possível pedir truco.");
            return;
        }

        if (this.otherTeamAcceptTruco(trucoTeam)) {
            this.setNewTrucoPointAfterTruco();
            this.lastTeamAskedTruco = trucoTeam;

            System.out.printf("Agora o jogo vale %d", this.currentTrucoPoint);
        } else {
            System.out.printf("O time %s venceu o truco!!!\n", trucoTeam);
        }
    }

    private boolean otherTeamAcceptTruco(TrucoTeam trucoTeam) {
        // to develop
        return true;
    }

    public void setNewTrucoPointAfterTruco() {
        Integer lastIndex = this.allTrucoPoints.size() - 1;
        this.currentTrucoPoint = this.allTrucoPoints.get(lastIndex);;
        // testar mais tarde se remove retorna o valor certo e se remove também um atributo
        List<Integer> allTrucoPointsCopy = this.allTrucoPoints;
        allTrucoPointsCopy.remove(lastIndex);
        this.allTrucoPoints = allTrucoPointsCopy;
    }

    public Integer getCurrentTrucoPoint() {
        return currentTrucoPoint;
    }

}
