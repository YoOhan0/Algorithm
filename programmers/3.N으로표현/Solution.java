import java.util.ArrayList;
import java.util.List;

class Solution {
    /* Point (동적 계획법)
    * 이 문제 특이하게 이차원의 리스트 형식으로 dp를 구성하는 문제로써, 각각의 dp단계에서 N개로 사칙연산을 활용해 만들 수 있는 모든 경우의 수를 구하는 식으로 이루어 진다.
    * 각각의 단계에서 연산의 맨 오른쪽에 올 수 있는 피연산자의 경우(N을 5개 이용할 경우 1~5개를 사용한 피연산자가 올 수 있다.)를 기준으로 dp단계를 수행하는데, 예를 들어
    * 오른쪽에 NNN으로 이루진 수가 오고 현재 dp의 단계가 5단계라면, 왼쪽 항은 이전 2단계때 구한 dp를 이용하고 사칙연산을 고려하여 만들 수 있는 수를 모두 구하면 해당 dp단계에서
    * 나올 수 있는 수들이 된다. 이 수들을 모두 정답 수와 비교하여 같은 것이 있다면 해당 단계(즉, N 사용 갯수)가 정답이라고 할 수 있다.
    * */


    static List<List<Integer>> dp=new ArrayList<>();
    static int[] NList=new int[9];

    public int solution(int N, int number) {
        int answer = -1;

        for(int i=0;i<=8;i++)dp.add(new ArrayList<>());//2차원 리스트 dp 설정.
        dp.get(0).add(0);//dp에서 N단계일 때, 연산 없이 만들 수 있는 수를 위해 추가.

        int mul=0;
        for (int i = 0; i < 9; i++) {//NList의 각각의 인덱스에는 인덱스 숫자 만큼의 N으로 이루어진 숫자가 저장되어 있다.
            NList[i]=N*mul;
            mul*=10;
            mul+=1;
        }

        for (int i = 1; i <= 8; i++) {//dp의 각 단계를 의미.

            for (int j = 0; j < i; j++) {//각각의 dp단계는 맨 오른쪽에 올 수 있는 피연산자를 기준으로 세부적으로 수행된다.

                for (int k = 0; k < dp.get(j).size(); k++) {// 왼쪽항(j개의 N을 사용한 이전에 구한 dp) 사칙연산(+,-,*,/) 오른쪽 항(i-j개의 N으로 이루어진 숫자) 로 해당 단계에서 만들 수 있는 모든 수를 고려.

                    if(dp.get(j).get(k)+NList[i-j]!=0)dp.get(i).add(dp.get(j).get(k)+NList[i-j]);//연산 결과가 0이 된다면 이후 단계에서 이용될 때 의미가 없고 시간만 늘리므로, 조건문을 통해 제거.
                    if(dp.get(j).get(k)-NList[i-j]!=0)dp.get(i).add(dp.get(j).get(k)-NList[i-j]);
                    dp.get(i).add(dp.get(j).get(k)*NList[i-j]);
                    if(dp.get(j).get(k)/NList[i-j]!=0)dp.get(i).add(dp.get(j).get(k)/NList[i-j]);
                }

            }

            for (int j = 0; j < dp.get(i).size(); j++) {//해당 단계에서 원하는 수가 나온다면 해당 단계를 정답으로 리턴.
                if(dp.get(i).get(j)==number)return i;
            }

        }

        return answer;
    }
}