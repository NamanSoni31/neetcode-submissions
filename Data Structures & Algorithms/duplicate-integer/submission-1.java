class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++) {
            if (map.get(nums[i]) == null) { 
                map.put(nums[i], nums[i]);  //if its not in the map, add it to the map
            }
            else { 
                return true;  //if its in the map then return true
            }
        }
        return false;
    }
}