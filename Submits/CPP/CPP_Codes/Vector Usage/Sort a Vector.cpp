#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
    public:
    vector<int> threeSum(vector<int>& nums) {

        int len = nums.size();

        if (len < 3) {
            return {};
        }

        // sort the nums
        sort(nums.begin(), nums.end());
        
       return nums;

    }

};


int main()
{
    Solution S;
    vector<int> nums = {-1, 0, 1, 2, -1, -4};
    vector<int> sorted = S.threeSum(nums);

    for (int element : sorted) {
        cout << element << " ";
    }
    cout << endl;

    for (int i = 0; i < sorted.size(); i++) {
        cout << sorted[i] << " ";
    }
    cout << endl;
    
}