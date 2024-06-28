import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {

    /* Point (플로이드 워셜 이용)
    * 처음에는 위상정렬을 이용하여 풀릴 수 있을 것처럼 생겨서 고민해 보았지만 풀리지 않았다. 그래서 다른 사람들의 생각들을 참고하여 dfs, 플로이드 워셜 등의 방법으로 고민해 보았고,
    * 플로이드 워셜을 적용하여, 각각의 사람들이 1.직접적으로 이기는 것 뿐만 아니라, 2. 승리 방향 그래프를 타고 도달 할 수 있다면 이길 수 있는 것을 알아내었고, 이를 통하여 각각의
    * 사람들이 몇명을 이길 수 있어 최소 n등이 될 수 있다는 것을 구할 수 있게 되었다. 이를 정렬하여 최소 n등을 할 수 있는 사람의 앞에 최소 n-1등 이상 할 수 있는 사람들의 수가 n-1명 이여야
    * 그 사람의 등수를 확정 할 수 있다는 것을 알게 되었고 이를 적용하여 정답을 구하게 되었다.
    * */

    static int INF=1987654321;
    static int[][] matrix=new int[101][101];

    public int solution(int n, int[][] results) {
        int answer = 0;

        for (int i = 1; i <= n; i++) {//플로이드 워셜 매트릭스 초기화.
            for (int j = 1; j <= n; j++) {
                if(i==j)matrix[i][j]=0;
                else matrix[i][j]=INF;
            }
        }
        for (int i = 0; i < results.length; i++)matrix[results[i][0]][results[i][1]]=1;//플로이드 워셜 매트릭스 값 업데이트.

        for (int k = 1; k <= n; k++) {//플로이드 워셜 알고리즘 적용.
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    if(matrix[i][k]!=INF&&matrix[k][j]!=INF&&matrix[i][j]>matrix[i][k]+matrix[k][j])matrix[i][j]=matrix[i][k]+matrix[k][j];
                }
            }
        }

        List<Integer> bucket=new ArrayList<>();

        for (int i = 1; i <= n; i++) {//각 사람들이 방향 그래프를 통하여 도달 가능한, 즉 이길 수 있는 사람들의 수를 계산하여 최소 등수 계산.
            int cnt=0;
            for (int j = 1; j <= n; j++) {
                if(j!=i&&matrix[i][j]!=INF)cnt++;
            }
            bucket.add(n-cnt);
        }

        Collections.sort(bucket);

        for (int i = 0; i < bucket.size(); i++) {//최소 n등을 하는 사람이라면 앞에 최소 n-1 이상하는 사람이 n-1 명이여야 등수를 확정할 수 있는 것을 이용.
            int j=i-1;
            while(j>=0&&bucket.get(j)==bucket.get(i))j--;
            if(j+1==bucket.get(i)-1)answer++;
        }

        return answer;
    }
}