class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> dictionary;
        for(int i = 0; i < nums.size(); i++){
            int complement = target-nums[i];
            if(dictionary.count(complement)){
                return {dictionary[complement], i};
            }
            dictionary[nums[i]] = i;
        }
        return {};
    }
};