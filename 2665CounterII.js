/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let editnum = init
    let store = init
    return {
        increment: function(){
            
            return ++editnum;
        },
        decrement: function(){
            return --editnum;
        },
        reset: function(){;
            editnum = store;
            return store;
        }
    }
};
