
function isY(ch) {
	return _in("aoeiuAOEIU", ch);
}

// http://blog.jobbole.com/49762/ 文本编辑器
var editor = {
	
	last_content: "",
	
	dom_editor_listener: function(ele) {
		console.log(this.last_content);
		console.log(ele.value);
		
		
		
		this.last_content = ele.value;
	}
};

// http://blog.jobbole.com/49762/ 判断是否为回文

function isPalindrome(word) {
	if (word.length % 2 == 0) {
		return false;
	}
	for (var i = 0, j = word.length - 1; i < j; i++, j--) {
		if (word[i] != word[j]) {
			return false;
		}
	}
	return true;
}

function dom_is_palindrome() {
	var o = document.getElementById("original").value;
	var n = isPalindrome(o);
	console.log(o + " is palindrome?" + n);
	document.getElementById("details").innerHTML = o + " is palindrome? " + n;
}

console.log("abc is palindrome? " + isPalindrome("abc"));
console.log("aba is palindrome? " + isPalindrome("aba"));

// http://blog.jobbole.com/49762/ 统计元音字母
function statAoeiu(word) {
	var sum = 0;
	var details = {}
	for (var i = 0; i < word.length; i++) {
		var ch = word[i];
		if (isY(ch)) {
			sum++;
			if (ch in details) {
				details[ch] += 1;
			} else {
				details[ch] = 1;
			}
		}
	}
	return {'sum': sum, 'details': details};
}

function dom_stat_aoeiu() {
	var o = document.getElementById("original").value;
	var n = statAoeiu(o);
	console.log("o=" + o + ",n=" + n.sum);
	document.getElementById("reversed").value = "sum=" + n.sum;
	document.getElementById("details").innerHTML = JSON.stringify(n.details);
}

console.log(statAoeiu("javascript"));
console.log(statAoeiu("indexOf"));

// http://blog.jobbole.com/49762/ 拉丁猪文字游戏
function latinPig(word) {
	var index = -1;
	var first = "";
	for (var i = 0; i < word.length; i++) {
		var ch = word[i];
		if (!isY(ch)) {// 辅音
			index = i;
			first = ch;
			break;
		}
	}
	
	if (index >= 0) {
		var newWord = "";
		for (var i = 0; i < word.length; i++) {
			if (i == index) {
				continue;
			} else {
				newWord += word[i];
			}
		}
		return newWord + "-" + first + "ay";
	}
	return word;
}

function dom_latin_pig() {
	var o = document.getElementById("original").value;
	var n = latinPig(o);
	console.log("o=" + o + ",n=" + n);
	document.getElementById("reversed").value = n;
}

console.log(latinPig("banana"));
console.log(latinPig("away"));

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