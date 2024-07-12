class Solution {
    /* Point (단순 구현)
    * 개인적으로 어려웠던 문제, 단순히 피타고라스를 이용하여 1사분면 좌표에서 r2이하의 x,y좌표에 대하여 해보았지만 시간 초과가 남.
    * 그래서 시간을 줄이기 위해서 삽질을 좀 했다. 그래도 풀지 못하여 질문 게시판을 참고 하였고 어떠한 분이 O(x^2)시간 복잡도 같이 보이지만,
    * 시간을 줄일 수 있는 방법을 적용한 풀이를 참고 하였고, 자료형도 신경써 주면서 풀었다.
    * 이 풀이의 핵심 아이디어는 1사분면에의 x축,y축에 있지 않은 점에 대하여 큰 원의 내부 점 좌표에서(테두리 포함) 작은 원의 내부 좌표 점들(테두리 제외)을
    * 빼주는 방식이고, 시간 복잡도를 줄이기 위하여 각각의 y좌표에 대하여 반복문을 통하여 가능한 점들을 찾아내는데 반복문의 이전에 구했던 원 내부로 가능한 y좌표를 다음 y좌표
    * 에 활용하여 시간을 줄이는 방식을 사용하였다. 그리고 이것에 더해 x축,y축에 있는 가능한 좌표들 까지 고려하면 최종 답을 구할 수 있다.
    * */
    public long solution(int r1, int r2) {
        long answer = 0;

        long answer1=0;
        long y=r1;
        for (int i = 1; i < r1; i++) {

            while((long)r1*r1<=y*y+(long)i*i)y--;
            answer1+=y;
        }
        answer1=answer1*4+(r1-1)*4;

        long answer2=0;

        y=r2;
        for (int i = 1; i < r2; i++) {

            while((long)r2*r2<y*y+(long)i*i)y--;
            answer2+=y;
        }
        answer2=answer2*4+r2*4;

        answer=answer2-answer1;

        return answer;
    }
}