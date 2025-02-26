#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
using namespace std;

int N, M;
int map[300][300];
bool visit[300][300];

using ll = long long;

struct Info {
    int y, x, h;

    bool operator<(const Info& a) const
    {
        return h > a.h;
    }
};

bool isIn(int y, int x);

int main() {
   
    cin >> M >> N; // N : row, M : col

    for (int i = 0;i < N;i++)
        for (int j = 0;j < M;j++)
            cin >> map[i][j];
  
    priority_queue<Info> pq;

    for (int i = 1;i < M - 1;i++)
    {
        pq.push({ 0,i,map[0][i] });
        visit[0][i] = true;

        pq.push({ N - 1,i,map[N - 1][i] });
        visit[N - 1][i] = true;
    }
    
    for (int i = 0;i < N;i++)
    {
        pq.push({ i,0,map[i][0] });
        visit[i][0] = true;

        pq.push({ i,M - 1, map[i][M - 1] });
        visit[i][M - 1] = true;
    }

    /*while (!pq.empty())
    {
        Info cur = pq.top();
        pq.pop();

        printf("y : %d, x : %d, h : %d\n", cur.y, cur.x, cur.h);
    }*/


    int dy[4] = { 0,0,-1,1 };
    int dx[4] = { -1,1,0,0 };

    ll ans = 0;
    while (!pq.empty())
    {
        Info cur = pq.top(); pq.pop();

        for (int i = 0;i < 4;i++)
        {
            int ny = cur.y + dy[i];
            int nx = cur.x + dx[i];

            if (isIn(ny, nx) && !visit[ny][nx])
            {
                if (cur.h >= map[ny][nx])
                {
                    ans += (cur.h - map[ny][nx]);               
                    pq.push({ ny,nx,cur.h });
                }
                else
                    pq.push({ ny,nx,map[ny][nx] });
                visit[ny][nx] = true;
            }
        }
    }

    cout << ans;

    return 0;
}
bool isIn(int y, int x)
{
    return (y >= 0) && (y < N) && (x >= 0) && (x < M);
}