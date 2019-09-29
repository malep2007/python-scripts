// Some javascript implementation of some problem
// take an array [1,1,3,4,1] return number not in right position

function correctOrder(inputValues){
  sorted = inputValues.sort();
  count = 0;
	for(let i = 0; i < inputValues.length; i++){
    if(inputValues[i] !== sorted[i]){
      count += 1;
    }
  }
  return count;
}

console.log(correctOrder([1,1,3,4,1]));
