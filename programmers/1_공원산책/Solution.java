import java.util.HashMap;
import java.util.Map;

class Solution {
    /* Point (단순 구현)
    * 단순히 문제 잘 읽고 구현하면 되는데, 코드가 생각 보다 길어져서 줄이기 위한 방법을 생각해보았다.
    * E,W,S,N 방향들 각각을 조건문으로 처리하는 대신, dy,dx 배열과 hash를 이용하여 코드를 줄여보고자 했으며, 작은 부분에서
    * 코드를 줄일 수 있는 부분들을 생각하게 만든 문제 였고, 이게 내 최선인 것 같다.
    * */
    static int W,H;

    public int[] solution(String[] park, String[] routes) {
        int[] answer = {};


        int[] dy=new int[]{0,0,1,-1};//dy,dy배열과 해쉬 함수를 이용한 방향 별 좌표 처리.
        int[] dx=new int[]{1,-1,0,0};
        Map<Character,Integer> dirMap=new HashMap<>();
        dirMap.put('E',0);
        dirMap.put('W',1);
        dirMap.put('S',2);
        dirMap.put('N',3);

        H=park.length;
        W=park[0].length();

        int curY=0,curX=0;//시작 좌표 찾기.
        for (int i = 0; i < park.length; i++) {
            for (int j = 0; j < park[i].length(); j++) {
                if (park[i].charAt(j) == 'S') {
                    curY=i;
                    curX=j;
                }
            }
        }

        for (int i = 0; i < routes.length; i++) {//routes 들에 있는 요소들을 기준으로 가능하면 go, 아니면 생략하고 다음 과정 수행.
            int dir=dirMap.get(routes[i].charAt(0));
            int cnt=routes[i].charAt(2)-'0';
            int j=1;
            for (; j <= cnt; j++) {
                if(isIn(curY+dy[dir]*j,curX+dx[dir]*j)&&park[curY+dy[dir]*j].charAt(curX+dx[dir]*j)!='X')continue;
                else break;
            }
            if (j <= cnt) {
                continue;
            } else {
                curY+=dy[dir]*cnt;
                curX+=dx[dir]*cnt;
            }
        }

        answer=new int[]{curY,curX};

        return answer;
    }

    static boolean isIn(int y,int x) {//매개변수 점이 park 안에 있는지 없는지 판단하는 함수.
        return ((y>=0)&&(y<H)&&(x>=0)&&(x<W));
    }
}