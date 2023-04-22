const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    str = input[0];
    
    let ans = []
    
    for (i = 0; i < str.length; i++) {
        if (str[i] === str[i].toLowerCase()) {
            ans.push(str[i].toUpperCase());
        }
        else {
            ans.push(str[i].toLowerCase());
        }
    }
    console.log(ans.join(""))
});