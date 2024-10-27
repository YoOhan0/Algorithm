class Solution {
    /* Point (댠순 구현)
    * 놀이기구 가격에 타본 횟수를 고려하여 총 필요한 금액을 계산해서 가지고 있는 돈 보다 크면 그 금액, 아니면 0을 반환한다.
    * 금액이 클 수도 있는 것을 고려하여 중간에 사용하는 변수를 long 형으로 사용해 주어야 한다.
    * */
    public long solution(int price, int money, int count) {
        long answer = -1;

        long cost=0;
        for(int i=1;i<=count;i++)cost+=i*price;

        if(cost-money<=0)answer=0;
        else answer=cost-money;

        return answer;
    }
}