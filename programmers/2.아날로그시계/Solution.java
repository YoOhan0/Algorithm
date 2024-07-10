class Solution {

    /* Point (단순 구현)
    1초 움직일 때 초침은 시계의 1/60 움직임 -> 60*12
    1초 움직일 때 분침은 시계의 1/60*60 움직임 -> 12
    1초 움직일 때 시침은 시계의 1/60*60*12 움직임 -> 1

    시계를 한바퀴 돌 때의 거리를 3600*12 라 하자.(거리가 3600*12를 넘으면 나머지 연산을 적용해주자!)

    <h1, m1, s1>
    총 초 계산 -> h1*3600+m1*60+s1
    <h2, m2, s2>
    총 초 계산 -> h2*3600+m2*60+s2

    이 후 총 초 - 이 전 총 초 = 우리가 관심 있는 시간 영역(총 초)
    1초당 아까 구한 비례관계로 움직이고, 해당 초만큼 초침,분침,시침을 원형을 고려해 이동 시킨다

    <시작 시,분,초침 위치 계산>
    초침-> 총 초 * 60*12 % 3600*12
    분침 -> 총 초 * 12 % 3600*12
    시침 -> 총 초 %3600*12

    -> while 문으로 시작 시,분,초침 부터 시작해서 위에서 구한 초 만큼 진행하고, 그 과정에서
    초침이 분침,시침을 넘는지 판단하고 이를 카운트하여 정답을 구한다!

    (초침이 분침,시침을 넘는지는 시계의 길이가 3600*12 이고, 원형인 점을 고려해야 한다. 이를 염두에
    두고 중첩 조건문을 적용하여, 넘는 경우의 상황에 대해서 카운트 해주고, 초침이 동시에 분침,시침과 겹치는 경우는
    1번을 카운트 할 수 있도록 잘 짜주어야 한다.)
    */
    public int solution(int h1, int m1, int s1, int h2, int m2, int s2) {
        int answer = 0;

        int startSecSum=h1*3600+m1*60+s1;
        int endSecSum=h2*3600+m2*60+s2;

        int s=(startSecSum*60*12)%(3600*12);
        int m=(startSecSum*12)%(3600*12);
        int h=startSecSum%(3600*12);

        int flagM=endSecSum-startSecSum;//총 진행할 초(sec)

        if (s == m && s == h) {//아무 것도 하지 않아도 겹치는 경우 고려.
            answer++;
        } else {
            if(s==m)answer++;
            if(s==h)answer++;
        }

        int t=0;
        while (t < flagM) {//중첩 조건문을 사용하여, 초침이 분침,시침을 넘는 경우의 수를 카운트.

            int nextS=(s+60*12)%(3600*12);
            int nextM=(m+12)%(3600*12);
            int nextH=(h+1)%(3600*12);

            boolean sExceed= (s+60*12)/(3600*12)==1 ? true : false;//단순히 이전 초침의 크기가 분침보다 커진 것으로는 원형이라는 조건 때문에 정확히 구할 수 없음! 그래서 침이 다시 처음으로 넘어갔는지 여부를 활용하였다.
            boolean mExceed= (m + 12) / (3600 * 12) == 1 ? true : false;
            boolean hExceed= (h+1)/(3600*12)==1 ? true: false;

            if(nextS==nextM&&nextM==nextH)answer++;//초침이 동시에 분침과 시침 겹치는 경우를 고려.
            else if (sExceed) {//초침이 다시 처음으로 돌아갈 경우.
                if (s < m) {
                    if (!mExceed) answer++;
                    else if (nextS >= nextM) answer++;
                } else if(nextS>=nextM)answer++;

                if (s < h) {
                    if(!hExceed)answer++;
                    else if(nextS>=nextH)answer++;
                }else if(nextS>=nextH)answer++;

            } else {//초침이 다시 처음으로 돌아가지 않는 경우.
                if((s<m)&&(nextS>=nextM))answer++;
                if((s<h)&&(nextS>=nextH))answer++;
            }

            s=nextS;
            m=nextM;
            h=nextH;

            t++;
        }

        return answer;
    }
}