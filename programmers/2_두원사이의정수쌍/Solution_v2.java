class Solution {
    /* Point (단순 구현)
    * 찾아보니 더 단순한 풀이가 있어서 어떻게 풀었는지 생각해보고 구현해보았다.
    * x값을 기준으로 반복문 처리하고, 각각의 x에서 r2 원에 있는 최대 y와 r1원에 있는 최소 y를 floor, ceil 처리하여 최대y-최소y+1를 해주고 모두 더해주면 된다.
    * 그리고 축들에 있는 점들을 따로 더해주면 답을 구할 수 있다. 이 풀이는 시간 복잡도가 O(n)밖에 되지 않아 좋은 풀이라고 생각한다.
    * */
    public long solution(int r1, int r2) {
        long answer = 0;

        for (int i = 1; i < r2; i++) {

            if (i < r1) {
                long maxY = (long) Math.floor(Math.sqrt(Math.pow(r2, 2) - Math.pow(i, 2)));
                long minY = (long) Math.ceil(Math.sqrt(Math.pow(r1, 2) - Math.pow(i, 2)));
                answer += maxY - minY + 1;
            } else {
                answer+=(long)Math.floor(Math.sqrt(Math.pow(r2,2)-Math.pow(i,2)));
            }

        }
        answer*=4;
        answer+=(r2-r1+1)*4;


        return answer;
    }
}