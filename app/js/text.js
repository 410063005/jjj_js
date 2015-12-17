
function isY(ch) {
	return _in("aoeiuAOEIU", ch);
}

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