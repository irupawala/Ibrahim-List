#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class KthLargest{
    public:
    int k;
    std::priority_queue <int, std::vector<int>, std::greater<int>> topkHeap;

    KthLargest(int K,std::vector<int> nums){

        k = K;
        for(int i=0;i<nums.size();i++){
            topkHeap.push(nums[i]);
        }

        while (topkHeap.size() > k){
            topkHeap.pop();
        }
    }

    // adds element in the heap
    int add(int val){
        topkHeap.push(val);
        if (topkHeap.size() > k){
            topkHeap.pop();

        }
        return ReturnKthLargest();
    }
    // returns kth largest element from topkHeap
    int ReturnKthLargest(){
        return topkHeap.top();
    }
};

int main(){
    std::vector<int> nums = {3, 6, 9, 10};
    std::vector<int> temp = {3, 6, 9, 10};
    //std::cout<<"Initial stream: "<< PrintList(nums) <<std::endl;
    KthLargest kthLarge(3, nums);
    std::vector<int> val = {4, 7, 10, 8, 15};
    std::cout<<std::endl;
    for (int i=0 ;i< val.size(); i++){
        std::cout<< "\tAdding a new number "<< val[i]<< " to the stream"<<std::endl;
        temp.push_back(val[i]);
        //std::cout<<"\t\tNumber stream: "<< PrintList(temp)<< std::endl;
        int kthLargest = kthLarge.add(val[i]);
        std::cout<<"\tKth largest element in the stream: "<< kthLargest<<std::endl;
        std::cout<<std::string(89,'-')<<std::endl;
    }
    return 0;
}
