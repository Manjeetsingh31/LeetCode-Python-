class Solution {
    public List<Integer> findMissingElements(int[] nums) {
      List<Integer> res = new ArrayList<>();
      int max = Integer.MIN_VALUE;
      int min = Integer.MAX_VALUE;
      HashSet<Integer> set = new HashSet<>();
      for(int num:nums){
        max = Math.max(num,max);
        min = Math.min(num,min);
        set.add(num);
      } 
      for(int i=min;i<=max;i++){
        if(!set.contains(i)){
            res.add(i);
        }
      }
      return res;
    }
}