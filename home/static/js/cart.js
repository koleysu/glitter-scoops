let cart = JSON.parse(localStorage.getItem("cart")) || {};
let total = 0;

renderCart();

function renderCart() {

    let html = "";
    let grandTotal = 0;

    for (let itemName in cart) {

        let item = cart[itemName];

        let itemTotal = item.price * item.qty;

        grandTotal += itemTotal;

        html += `
        <div class="cart-row">

            <img src="${item.image}" class="cart-image">

            <div class="cart-details">

                <h3>${item.name}</h3>

                <p>Price : ₹${item.price}</p>

            </div>

            <div class="quantity-box">

                <button onclick="decreaseQty('${itemName}')">−</button>

                <span>${item.qty}</span>

                <button onclick="increaseQty('${itemName}')">+</button>

            </div>

            <div class="item-total">

                ₹${itemTotal}

            </div>

            <button class="remove-btn"
                onclick="removeItem('${itemName}')">

                ❌

            </button>

        </div>
        `;
    }

    document.getElementById("cart-container").innerHTML = html;
    document.getElementById("grand-total").innerText = grandTotal;

    localStorage.setItem("cart", JSON.stringify(cart));
}

function increaseQty(itemName){

    cart[itemName].qty++;

    renderCart();

}

function decreaseQty(itemName){

    cart[itemName].qty--;

    if(cart[itemName].qty <= 0){

        delete cart[itemName];

    }

    renderCart();

}

function removeItem(itemName){

    delete cart[itemName];

    renderCart();

}
function updateCartCount() {

    let totalItems = 0;

    for (let itemName in cart) {

        totalItems += Number(cart[itemName].qty);

    }

    const cartCount =
        document.getElementById("cart-count");

    if (cartCount) {

        cartCount.innerText = totalItems;

    }
}
function continueShopping() {

    // Get the current cart
    let existingCart = localStorage.getItem("cart");

    // If cart does not exist, create an empty cart
    if (!existingCart) {        
		 localStorage.setItem("cart", JSON.stringify(existingCart));
    }

    // Navigate to Menu
    window.location.href = "/menu/";
}