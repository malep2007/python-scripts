// Using closures as function factories to create different variations of the same function
function dwightJob(title) {
    return function(prefix ){
        return prefix + ' ' + title
    }
}

var sales = dwightJob('Salesman');
var manager = dwightJob('Manager')

// Uncomment this to test
// console.log(sales('Top'))
// console.log(manager('Assistant to Regional'))
// console.log(manager('Regional'));


// Namespacing private function: Using module pattern
/* 
    Javascript does not have the ability to declare private functions but with the module pattern 
    implementation through the use of closures we can try to mimic similar behaviours. 
    The module pattern takes advantage of IIFEs (immediately invoked function execution)
*/

var dwightSalary = (function(){
    var salary = 60000;
    function changeBy(amount){
        salary += amount;
    }
    return {
        raise: function(){
            changeBy(5000)
        },
        lower: function(){
            changeBy(-5000)
        },
        currentAmount: function(){
            return salary;
        }
    }
})();

console.log(dwightSalary.currentAmount());
dwightSalary.raise();
console.log(dwightSalary.currentAmount())
dwightSalary.lower();
dwightSalary.lower();
console.log(dwightSalary.currentAmount());

//Now try to access the changeBy() function

dwightSalary.changeBy(10000);
