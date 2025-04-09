/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    let temp = []
    for (let i = 0; i < arr.length; i++){
        let res = fn(arr[i], i)
        temp.push(res);
    }
    return temp
};
