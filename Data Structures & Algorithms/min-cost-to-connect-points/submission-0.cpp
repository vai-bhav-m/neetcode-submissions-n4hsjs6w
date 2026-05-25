class Solution {
public:
// priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq
    map<int,vector<pair<int,int>>> create_full_tree(vector<vector<int>> points) {
        map<int, vector<pair<int,int>>> adj_list;
        for (size_t i=0; i<points.size(); i++) {
            for (size_t j=0; j<points.size(); j++) {
                if (i!=j) {
                    int man_dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]);
                    adj_list[i].push_back({man_dist, j});
                }
            }
        }
        return adj_list;   
    }

    int minCostConnectPoints(vector<vector<int>>& points) {
        map<int,vector<pair<int,int>>> adj_list = create_full_tree(points);
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> frontier;
        set<int> visited;
        int cost = 0;
        frontier.push({0,0});
        while (visited.size() < points.size()){
            pair<int, int> curr = frontier.top();
            frontier.pop();
            if (visited.count(curr.second)) continue;
            visited.insert(curr.second);
            cost += curr.first;
            for (auto next: adj_list[curr.second]) frontier.push(next);
        }
        return cost;
    }
};
