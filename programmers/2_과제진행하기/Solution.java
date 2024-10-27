import java.util.*;

class Solution {
    /* Point (구현 문제)
    * 문제 자체의 알고리즘은 어렵지 않았으나, 구현을 어떻게 하느냐에 따라 코드의 양이 달라졌다.
    * 처음에는 클래스를 만들어서 풀어 보고자 하였으나 풀긴 했지만 코드가 지저분 하다 느꼈고, 분기 처리도 명확하다기 보단 애매하게 풀고 시간이 해결해준 느낌이였어서,
    * 다시 줄일 수 있는 것들은 없나, 로직은 더 단순하게 할 수 없나 고민해보고 현재의 코드를 짜게 되었다.
    * */
    public String[] solution(String[][] plans) {
        String[] answer = {};

        Map<Integer,String> assignMap=new HashMap<>();
        List<int[]> planList =new ArrayList<>();

        for (int i = 0; i < plans.length; i++) {//plan을 (과제에 해당하는 index,현재시간을 분으로 환산, 지속시간) 형식으로 변환하였다.(구현의 편리를 위해)
            int hour=Integer.parseInt(plans[i][1].substring(0,2));
            int minu=Integer.parseInt(plans[i][1].substring(3,5));
            planList.add(new int[]{i, 60 * hour + minu, Integer.parseInt(plans[i][2])});
            assignMap.put(i, plans[i][0]);
        }

        Collections.sort(planList,(o1,o2)->{return o1[1]-o2[1];});//시간기준 오름차순 정렬 수행.

        Stack<int[]> stopped=new Stack<>();
        List<String> bucket=new ArrayList<>();

        for (int i = 0; i < planList.size()-1; i++) {//각각의 과제를 반복문으로 수행하면서, 과제를 하고 시간이 남으면 남는 시간에 대해 Stopped 과제들을 수행 할 수 있는 만큼 수행하는 식으로 로직을 구현하였다.
            int[] curItem=planList.get(i);
            int[] nextItem=planList.get(i+1);

            if (curItem[1] + curItem[2] > nextItem[1]) {
                stopped.add(new int[]{curItem[0],curItem[1]+curItem[2]-nextItem[1]});
            } else {

                bucket.add(assignMap.get(curItem[0]));
                int tmpTime=curItem[1]+curItem[2];

                while (!stopped.isEmpty() && tmpTime + stopped.peek()[1] <= nextItem[1]) {
                    int[] stopItem=stopped.pop();
                    tmpTime+=stopItem[1];
                    bucket.add(assignMap.get(stopItem[0]));
                }
                if (!stopped.isEmpty()) {//애초부터 Stopped 비어있거나, 위의 while문을 끝냈을 때는 그냥 쉬는 시간이라 생각하고 다음 과제 하러 가면 된다.
                    int[] stopItem=stopped.pop();
                    stopped.add(new int[]{stopItem[0],tmpTime+stopItem[1]-nextItem[1]});
                }
            }
        }
        bucket.add(assignMap.get(planList.get(planList.size()-1)[0]));//마지막 과제 고려.
        while(!stopped.isEmpty())bucket.add(assignMap.get(stopped.pop()[0]));//마지막까지 기회가 없어서 하지못한 Stopped 과제 고려.

        answer=new String[bucket.size()];
        for(int i=0;i<answer.length;i++)answer[i]=bucket.get(i);

        return answer;
    }
}