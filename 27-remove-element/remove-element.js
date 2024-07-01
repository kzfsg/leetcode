/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    k = nums.length
    for (let i = nums.length - 1; i > -1; i--) {
        if (nums[i] == val) {
            k -= 1
            nums.splice(i,1)
        }
    }
    return k
};

// 1. iterate through nums from the back
// 2. if element is equivalent to val, remove
// 3. return k