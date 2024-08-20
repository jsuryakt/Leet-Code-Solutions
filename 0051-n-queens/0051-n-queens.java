class Solution {
    // TC - (n*n!)
    // SC
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> ans = new ArrayList(n);
        String[][] board = new String[n][n];
        for (int i=0; i<n; i++) {
            String[] row = new String[n];
            Arrays.fill(row, ".");
            board[i] = row;
        }
        recursionHelper(n, 0, board, ans);
        return ans;
    }

    public void recursionHelper(int n, int col, String[][] board, List<List<String>> ans) {
        if (col == n) {
            List<String> list = new ArrayList<>();
            for (String[] array : board) {
                StringBuilder r = new StringBuilder();
                for (String place : array) {
                    r.append(place);
                }
                list.add(r.toString());
            }
            ans.add(list);
            return;
        }
        for (int row=0; row<n; row++) {
            if (isValidPosition(row, col, board)) {
                board[row][col] = "Q";
                recursionHelper(n, col+1, board, ans);
                board[row][col] = ".";
            }
        }
        // row wise check
        // for (int col=0; col<n; col++) {
        //     if (isValidPosition(row, col, board)) {
        //         board[row][col] = "Q";
        //         recursionHelper(n, row+1, board, ans);
        //         board[row][col] = ".";
        //     }
        // }
    }

    public boolean isValidPosition(int row, int col, String[][] board) {
        // check left row
        for (int j = col; j >= 0; j--) {
            if (board[row][j].equals("Q")) {
                return false;
            }
        }

        // check top-left diagonal
        for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j].equals("Q")) {
                return false;
            }
        }

        // check bottom-left diagonal
        for (int i = row, j = col; i < board.length && j >= 0; i++, j--) {
            if (board[i][j].equals("Q")) {
                return false;
            }
        }

        // for row wise check
        // // check upper cols
        // for (int i = row; i >= 0; i--) {
        //     if (board[i][col].equals("Q")) {
        //         return false;
        //     }
        // }

        // // check top-left diagonal
        // for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
        //     if (board[i][j].equals("Q")) {
        //         return false;
        //     }
        // }

        // // check top-right diagonal
        // for (int i = row, j = col; i >= 0 && j < board.length; i--, j++) {
        //     if (board[i][j].equals("Q")) {
        //         return false;
        //     }
        // }
        return true;
    }
}