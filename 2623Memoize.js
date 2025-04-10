/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    let instructions = {}; // init cache
    return function(...args) {
        let a = JSON.stringify(args)
        if (a in instructions){ // if already in cache
            return instructions[a]; // return cached item
        }
        // add fn call to cache
        let res = fn(...args);
        instructions[a] = res; // store new cache entry
        return res; // return fn output
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */
