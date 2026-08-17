function continueShopping() {

    // ==========================================
    // 1. Clear Shopping Cart
    // ==========================================

    localStorage.removeItem("cart");


    // ==========================================
    // 2. Clear Cart Count
    // ==========================================

    const cartCount = document.getElementById("cart-count");

    if (cartCount) {
        cartCount.innerText = "0";
    }


    // ==========================================
    // 3. Optional: Clear Checkout Cart Data
    // ==========================================

    const cartData = document.getElementById("cart_data");

    if (cartData) {
        cartData.value = "{}";
    }


    // ==========================================
    // 4. Move to Main Menu
    // ==========================================

    window.location.href = "/";

}