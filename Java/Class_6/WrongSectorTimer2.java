package Task_2.race.car;

public class WrongSectorTimer2 {
    private int[] sectorTimes;

    public int[] getSectorTimes() {
        return sectorTimes;
    }

    public void setSectorTimes(int[] sectorTimes) {
        this.sectorTimes = sectorTimes;
    }

    public WrongSectorTimer2(int[] sectorTimes) {
        this.setSectorTimes(sectorTimes);
    }

    public int getLapTime(int idx) {
        return this.getSectorTimes()[idx];
    }

    public int getSectorTime(int idx) {
        return this.getSectorTimes()[idx];
    }
}
