const num1 = +prompt("შეიყვანეთ პირველი რიცხვი");
const num2 = +prompt("შეიყვანეთ მეორე რიცხვი");
const operation = prompt("აირჩიეთ ოპერაცია: +, -, *, /");

let result;

if (operation === "+") {
  result = num1 + num2;
} else if (operation === "-") {
  result = num1 - num2;
} else if (operation === "*") {
  result = num1 * num2;
} else if (operation === "/") {
  if (num2 !== 0) {
    result = num1 / num2;
  } else {
    alert("ნულზე გაყოფა არ შეიძლება!");
  }
} else {
  alert("არასწორი ოპერაცია");
}

if (result !== undefined) {
  alert("შედეგი არის: " + result);
}
