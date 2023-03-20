#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());
        int n = nums.size();
        for (int i = 0; i < n - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue; // avoid duplicates
            int j = i + 1, k = n - 1;
            while (j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                if (sum == 0) {
                    res.push_back({nums[i], nums[j], nums[k]});
                    while (j < k && nums[j] == nums[j+1]) j += 1; // avoid duplicates
                    while (j < k && nums[k-1] == nums[k]) k -= 1; // avoid duplicates
                    j += 1;
                    k -= 1;
                } else if (sum < 0) {
                    j += 1 ;
                } else {
                    k -= 1 ;
                }
            }
        }
        return res;
    }
};


int main()
{
    Solution S;
    vector<int> nums = {-1, 0, 1, 2, -1, -4};
    vector<vector<int>> three_sum = S.threeSum(nums);
    for (const auto s : three_sum) {
        for (const auto elem : s) {
            cout << elem << " ";
        }
        cout << endl;
    }
    return 0;
}
