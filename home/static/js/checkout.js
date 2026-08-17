let cart =
JSON.parse(localStorage.getItem("cart")) || {};

let total = 0;

for (let item in cart) {

    total += cart[item].price * cart[item].qty;

}

document.getElementById("grand-total").innerHTML = total;