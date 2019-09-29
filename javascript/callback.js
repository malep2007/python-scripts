function addTwo(num) {
	return num+=2
}

function map(array, callback){
    let newArray = []
    array.forEach(element => {
        newArray.push(callback(element))
    });
    return newArray
}



function copyArrayAndManipulate(array, instruction){
    let output = []
    for(let i = 0; i < array.length; i++){
        output.push(instruction(array[i]))
    }
    return output
}

console.log(copyArrayAndManipulate([1,2,3], function(number){
    return number+=2;
}));
