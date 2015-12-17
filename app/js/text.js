// http://blog.jobbole.com/49762/ 逆转字符串——输入一个字符串，将其逆转并输出。
//console.log("test")

function reverse(input) {
	if (input == "" || input == undefined) {
		return "";
	}
	var output = "";
	for (var i = input.length; i > 0; i--) {
		output += input[i - 1];
	}
	return output;
}

console.log("abcdef" + " " + reverse("abcdef"));
console.log("" + " " + reverse(""));
console.log("abcdef9874565" + " " + reverse("abcdef9874565"));
console.log("abcdef9874565" == reverse(reverse("abcdef9874565")));

function dom_test() {
	var o = document.getElementById("original").value;
	var n = reverse(o)
	console.log("o=" + o + ",n=" + n);
	document.getElementById("reversed").value = n;
}