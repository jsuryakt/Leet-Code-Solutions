class Solution {
    public int minRefuelStops(int target, int startFuel, int[][] stations) {
        // currFuel+stationFuel+currDistance
        // currFuel = 60-10 = 50
        // stationFuel = 30
        // currDistance = 20
        // maxPossible = 100
        PriorityQueue<Integer> fuelDump = new PriorityQueue<>(Collections.reverseOrder());
        int stationCount = 0;
        int currDistance = startFuel;
        for(int[] station: stations){
            // System.out.println(currDistance);
            int stationAt = station[0];
            int stationFuel = station[1];
            
            while(currDistance<stationAt) {
                if(fuelDump.size()==0) {
                    return -1;
                }
                
                currDistance += fuelDump.poll();
                stationCount++;
            }
            
            fuelDump.add(stationFuel);
        }
        while(currDistance < target) {
            if(fuelDump.size()==0) {
                return -1;
            }
            currDistance += fuelDump.poll();
            stationCount++;
        }
        return stationCount;
        
    }
}