#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <utility>
#include <queue>

#define MAX_VAL 1987654321

using namespace std;

int N, T;
vector<pair<int, int>> graph[1000];
int dist[1000], p[1000];
bool visit[1000];

struct Comp
{
	bool operator()(pair<int, int>& a, pair<int, int>& b)
	{
		return a.second > b.second;
	}
};
int main()
{
	cin >> N >> T;

	int a, b, c;
	for (int i = 0;i < T;i++)
	{
		cin >> a >> b >> c;
		graph[a - 1].push_back({ b - 1,c });
		graph[b - 1].push_back({ a - 1,c });
	}

	priority_queue<pair<int, int>, vector<pair<int, int>>, Comp> pq;

	for (int i = 0;i < N;i++)dist[i] = MAX_VAL;
	dist[0] = 0;

	pq.push({ 0,0 });

	while (!pq.empty())
	{
		pair<int, int> cur = pq.top();
		pq.pop();

		if (visit[cur.first])continue;
		else visit[cur.first] = true;

		for (int i = 0;i < graph[cur.first].size();i++)
		{
			pair<int, int> next = graph[cur.first][i];

			if (!visit[next.first] && dist[cur.first] + next.second < dist[next.first])
			{
				dist[next.first] = dist[cur.first] + next.second;
				p[next.first] = cur.first;
				pq.push({ next.first,dist[next.first] });
			}
		}
	}
	int ot = dist[N - 1];

	vector<pair<int, int>> bucket;

	int tmp = N - 1;
	while (p[tmp] != tmp)
	{
		bucket.push_back({ tmp,p[tmp] });
		tmp = p[tmp];
	}

	/*for (int i = 0;i < bucket.size();i++)
		printf("<%d, %d>\n", bucket[i].first, bucket[i].second);*/

	int ans = 0;
	for (int tc = 0;tc < bucket.size();tc++)
	{
		for (int j = 0;j < N;j++)
		{
			dist[j] = MAX_VAL;
			visit[j] = false;
		}

		dist[0] = 0;

		pq.push({ 0,0 });

		while (!pq.empty())
		{
			pair<int, int> cur = pq.top();
			pq.pop();

			if (visit[cur.first])continue;
			else visit[cur.first] = true;

			for (int i = 0;i < graph[cur.first].size();i++)
			{
				pair<int, int> next = graph[cur.first][i];

				if (cur.first == bucket[tc].first && next.first == bucket[tc].second)
					continue;
				if (cur.first == bucket[tc].second && next.first == bucket[tc].first)
					continue;

				if (!visit[next.first] && dist[cur.first] + next.second < dist[next.first])
				{
					dist[next.first] = dist[cur.first] + next.second;
					p[next.first] = cur.first;
					pq.push({ next.first,dist[next.first] });
				}
			}
		}
		ans = max(ans, dist[N - 1]);
	}
	if (ans == MAX_VAL)
		cout << -1;
	else
		cout << ans - ot;

	return 0;
}