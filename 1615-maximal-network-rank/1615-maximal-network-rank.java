//    0 1 2 3
// 0 [0 1 0 1] - 2
// 1 [1 0 1 1] - 3
// 2 [0 1 0 0] - 1
// 3 [1 1 0 0] - 2
class Solution {
    public int maximalNetworkRank(int n, int[][] roads) {
        int[][] adj = new int[n][n];
        
        for (int[] road : roads) {
            int ai = road[0];
            int bi = road[1];
            adj[ai][bi] = 1;
            adj[bi][ai] = 1;
        }

        // To store the number of roads connected to each city
        int[] cityConnections = new int[n];

        for (int i = 0; i < n; i++) {
            int sum = 0;
            for (int j = 0; j < n; j++) {
                sum += adj[i][j];
            }
            cityConnections[i] = sum;
        }

        int maxRank = 0;

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                // add roads of both cities and negate 1 (adj[i][j] will be 1 if connected) 
                //if both are connected since it's road connection is counted twice
                int rank = cityConnections[i] + cityConnections[j] - adj[i][j];
                maxRank = Math.max(maxRank, rank);
            }
        }

        return maxRank;
    }
}
