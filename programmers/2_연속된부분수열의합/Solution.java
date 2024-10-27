import java.util.*;

class Solution {
    /* Point (단순 구현)
    * start -> 총합을 구할 때 여기서부터 시작, end -> 총합을 구할때 이거 전에 까지 더함.
    * 처음에는 start,end 둘다 0에서 시작해서 sum을 0부터 시작한다.
    * 아이디어는 start의 경우의 수(0,1,2,...)별로 end 를 옮겨가면서 k를 만들 수 있는지 판단 할 것이다.
    * 이때 start가 0->1이 되면, 그 시점의 sum도 sequence[0]만큼 줄어들 것이고, 이 이후 start 1일 경우에는 sum이 k보다 크냐,적냐에 따라 k를
    * 찾는 과정을 분기 시켜 주어야 한다.
    * */

    public int[] solution(int[] sequence, int k) {
        int[] answer = {};

        List<int[]> li=new ArrayList<>();//부분 수열의 합이 k를 만족 시킬 수 있는 시작Index,끝Index를 저장 할 리스트.

        int start=0,end=0,sum=0,len=sequence.length;
        while (start < len && end <= len) {

            if (sum < k) {//현재 합이 k보다 작으면, 끝index를 늘려가면서 k보다 같거나 클때까지 이동시키고 이때 k가 된다면 그 시작,끝index를 리스트에 저장.
                while(sum<k&&end<len)sum+=sequence[end++];
            } else if (sum > k) {//현재 합이 k보다 크면 끝index를 줄여가며 k보다 같거나 작을때 까지 이동시키고 이때 k가 된다면 그 시작,끝index를 리스트에 저장.
                while(sum>k&&end>=start)sum-=sequence[--end];
            }

            if(sum==k)li.add(new int[]{start,end});
            sum-=sequence[start++];//시작 index를 다음으로 옮겨서(sum도 시작index의 이전 값 만큼 줄임) 가능한 다른 경우의 수 세기.
        }

        Collections.sort(li,(o1,o2)->{return ((o1[1]-o1[0])==(o2[1]-o2[0]) ? o1[0]-o2[0] : (o1[1]-o1[0])-(o2[1]-o2[0]));});//조건에서 가장 짧은 것을 구하고,같다면 시작index가 작은 것을 구하라고 한것을 고려.

        answer=li.get(0);
        answer[1]-=1;

        return answer;
    }
}