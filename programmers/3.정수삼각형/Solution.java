class Solution {

    /* Point (동적 계획법)
    * 동적 계획법을 이용하여 삼각형의 각 층 과 각 대상들까지를 고려하는 이차원 dp를 만든다.
    * 그리고 각 단계에서는 현재 대상으로 올 수 있는 이전 단계 dp층 중에 큰 것과 현재 단계의 대상 값을 저장하여 dp를 만들어 간다.
    * 모든 단계를 수행 후 맨 마지막 층의 대상들의 dp값 중에 제일 큰 값이 이 삼각형에서 만들 수 있는 가장 큰 경로라고 생각 할 수 있다.
    * */

    static int[][] dp = new int[500][500];

    public int solution(int[][] triangle) {
        int answer = 0;

        dp[0][0]=triangle[0][0];//dp 초기화
        for (int i = 1; i < triangle.length; i++) {

            for (int j = 0; j < triangle[i].length; j++) {
                if (j == 0) {//dp를 수행할 때, 각 층의 처음 대상들은 바로 위의 dp만 고려 가능.
                    dp[i][j] = dp[i - 1][j]+triangle[i][j];
                } else if (j == triangle[i].length-1) dp[i][j] = dp[i - 1][j - 1]+triangle[i][j];//각 층의 마지막 대상들은 바로 위의 dp만 고려 가능.
                else {//현재 대상으로 올 수 있는 이전 층 dp들 중에 큰 값과 현재 대상 값을 더하여 dp를 생성.
                    dp[i][j] = dp[i - 1][j - 1] > dp[i - 1][j] ? dp[i - 1][j - 1] + triangle[i][j] : dp[i - 1][j] + triangle[i][j];
                }
            }
        }

        int max=0;
        for (int i = 0;i< dp[triangle.length - 1].length; i++) {//마지막 층의 모든 대상의 dp 값들 중에 가장 큰 값 추출.
            if(dp[triangle.length-1][i]>max)max=dp[triangle.length-1][i];
        }

        answer=max;

        return answer;
    }
}