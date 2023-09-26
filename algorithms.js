//////////////////////////////////Grid Travel/////////////////////////////////////

// const gridTraveler = (m, n, memo={}) => {
//     const key = m + ',' + n;
//     if (key in memo) return memo[key];
//     if (m === 1 && n === 1) return 1;
//     if (m === 0 || n === 0) return 0;

//     memo[key] = gridTraveler(m-1, n) + gridTraveler(m, n-1)
//     return memo[key];
// };

// console.log(gridTraveler(5,10));
///////////////////////////////Fibonacci////////////////////////////////////////
// const fib = (n, memo={}) => {
//     const key = n;
//     if (key in memo){
//         return memo[key]
//     }
//     if (n <= 2){
//         return 1
//     }
//     memo[key] = fib(n-1, memo) + fib(n-2, memo)
//     return (fib(n-1, memo) + fib(n-2, memo))
// }
///////////////////////////////Bubble Sort////////////////////////////////////////
// console.log(fib(25));
// const bubbleSort = (arr, n) => {
//     var i, j, temp;
//     var swapped;
//     for (i=0; i<n-1; i++){
//         swapped = false;
//         for (j=0; j<n-i-1; j++){
//             if(arr[j] > arr[j+1]){
//                 temp = arr[j];
//                 arr[j] = arr[j+1];
//                 arr[j+1] = temp;
//                 swapped = true;
//             }
//         }Find the largest three elements in an array
//         if(swapped == false){
//             break;
//         }
//     }
// }
// var arr = [65,41,27,77,82,12] 
// var n = arr.length;
// bubbleSort(arr, n);


// for (var i=0; i<n; i++){
//     console.log(arr[i])
// }
////////////////////////////////// Largest number /////////////////////////////////////

// const numbers = [65,41,27,[
//                     53,13,90,10,
//                         [109,1,23],
//                 ],77,15,97,5];
// // console.log(Math.max(...numbers));
// const flatten = (values) => values.reduce(
//     (acc, item, index, array) => acc.concat(
//         Array.isArray(item) ? flatten(item) : item
//     ), []
// )
// const largestNumber = (values) => {
//     let highest = values[0];
//     for (var i = 0; i < values.length; i++){
//         if(values[i] > highest){
//             highest = values[i]
//         }
//     }
//     return highest;
// }
// console.log(flatten(numbers))
// console.log(largestNumber(flatten(numbers)))

////////////////////////////////// Missing number /////////////////////////////////////
// const missingNumber = (arr) => {
//     let missArray = [];
//     let minNumber = Math.min(...arr);
//     let maxNumber = Math.max(...arr);

//     for(let i=minNumber; i<maxNumber; i++){
//         if(arr.indexOf(i) < 0){
//             missArray.push(i);
//         }
//     }
//     return missArray;
// }
// const numbers = [51,52,53,56,57,58];
// console.log( missingNumber(numbers));

////////////////////////////////// Repeating number /////////////////////////////////////
// const repeatingArray = (arr) => {
//     let number = [];
//     for (let i=0; i<arr.length; i++){
//         for(j=i+1; j<arr.length; j++){
//             if (arr[i] === arr[j]){
//                 number.push(arr[i]);
//             }
//         }
//     }
//     return number;
// }

// const numbers = [50,52,53,56,68,58,52];
// console.log( repeatingArray(numbers));
////////////////////////////////// Split string /////////////////////////////////////
const abbrevName = (str) => {
    var split_names = str.trim().split(" ");
    return (split_names[0] + " " + split_names[1].charAt(0) + ".")
}

console.log(abbrevName('Robin Singh'))

