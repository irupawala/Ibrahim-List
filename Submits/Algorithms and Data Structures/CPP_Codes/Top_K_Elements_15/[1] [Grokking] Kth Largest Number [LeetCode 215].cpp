#include <iostream>
#include <vector>
#include <queue>
#include <list>

using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int>> minHeap;

        for (int i=0; i<nums.size(); i++) {
            if (minHeap.size() < k) {
                minHeap.push(nums[i]);
            }
            else if (nums[i] > minHeap.top()){
                minHeap.pop();
                minHeap.push(nums[i]);
            }
        }

        return minHeap.top();
    }
};

int main()
{

    Solution S;
    vector<int> nums_1 = {3,2,1,5,6,4};
    cout << "First Input " << S.findKthLargest(nums_1, 2) << endl;

    vector<int> nums_2 = {3,2,3,1,2,4,5,5,6, 7, 8, 9};
    cout << "Second Input " << S.findKthLargest(nums_2, 4) << endl;    
}