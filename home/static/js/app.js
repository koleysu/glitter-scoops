// Restore existing cart from Local Storage
let cart = JSON.parse(localStorage.getItem("cart")) || {};
let total = 0;
let selectedProductId = "";
let selectedProduct = "";
let selectedVariantId = "";
let selectedSize = "";
let selectedPrice = 0;
let selectedImage = "";
let currentProduct = null;
let currentPrices = {};

// Update cart icon when Menu page loads
document.addEventListener("DOMContentLoaded", function () {
    updateCartCount();
});

function renderCart() {

    let totalItems = 0;
    debugger;
    for (let itemName in cart) {
        totalItems += cart[itemName].qty;
    }

    document.getElementById("cart-count").innerText = totalItems;

    // Existing code to display cart items
}

function increaseQty(name) {
    cart[name].qty += 1;
    renderCart();
}

function decreaseQty(name) {
    cart[name].qty -= 1;

    if (cart[name].qty <= 0) {
        delete cart[name];
    }

    renderCart();
}
function removeItem(button, price) {
    let item = button.parentElement;
    item.remove();

    total -= price;
    document.getElementById("total").innerText = total;
}

/*-----Open Model -----   */
let images = [];
let currentIndex = 0;

function openModal(name, price, imgList, desc) {
    document.getElementById("modal").style.display = "block";

    images = imgList;
    currentIndex = 0;

    document.getElementById("m-name").innerText = name;
    document.getElementById("m-price").innerText = "₹" + price;
    document.getElementById("m-desc").innerText = desc;

    renderSlider();
}

function renderSlider() {
    let img = document.getElementById("m-img");
    img.src = "/static/" + images[currentIndex];

    // Create dots
    let dotsContainer = document.getElementById("dots");
    dotsContainer.innerHTML = "";

    images.forEach((_, index) => {
        let dot = document.createElement("span");
        dot.className = "dot" + (index === currentIndex ? " active" : "");
        dot.onclick = () => {
            currentIndex = index;
            renderSlider();
        };
        dotsContainer.appendChild(dot);
    });
}

function nextImage() {
    currentIndex = (currentIndex + 1) % images.length;
    renderSlider();
}

function prevImage() {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    renderSlider();
}
function closeModal() {
    document.getElementById("modal").style.display = "none";
}
function updateCartCount() {

    let totalItems = 0;

    for (let itemName in cart) {
        totalItems += cart[itemName].qty;
    }

    document.getElementById("cart-count").innerText = totalItems;
}
//This function will be called from to Add To Cart function from the Menu
function addToCart(event, productId, name, size, price, image) {
   
    if (event) {
        event.stopPropagation();
    }

    price = Number(price);

    if (isNaN(price)) {
        console.error("Invalid price:", price);
      
        return;
    }

    // Create unique cart key using ID + size
    let cartKey = productId + "-" + size;

    if (cart[cartKey]) {

        cart[cartKey].qty += 1;

    } else {

        cart[cartKey] = {
            id: productId,
            name: name,
            size: size,
            price: price,
            image: image,
            qty: 1
        };
    }

    localStorage.setItem("cart", JSON.stringify(cart));

    updateCartCount();

    console.log("Added to cart:", cart[cartKey]);
}
function openDetailPopup(id, name, desc, price, image) {

    console.log("Product ID:", id);
    console.log("Product Name:", name);
    console.log("Description:", desc);
    console.log("Price:", price);
    console.log("Image:", image);

    // Store selected product information
    selectedProductId = id;
    selectedProduct = name;
    selectedPrice = Number(price) || 0;

    // Product name
    document.getElementById("m-name").innerText = name;

    // Product price
    document.getElementById("m-price").innerText =
        "₹" + selectedPrice;

    // Product description
    document.getElementById("m-desc").innerText =
        desc || "";

    // Product image
    document.getElementById("m-img").src = image;

    // Open modal
    document.getElementById("modal").style.display = "block";
}
function increaseQty(name) {

    cart[name].qty++;

    renderCart();
    updateCartCount();

}
function decreaseQty(name) {

    cart[name].qty--;

    if (cart[name].qty <= 0) {
        delete cart[name];
    }

    renderCart();
    updateCartCount();

}





function openMysteryPopup(item) {

    console.log("Complete Item:", item);
    console.log("ID:", item.id);
    console.log("Name:", item.name);
    console.log("Category:", item.category);
    console.log("Image:", item.image);
    console.log("Variants:", item.variants);

    // ---------------------------------
    // Store Product
    // ---------------------------------

    currentProduct = item;

    selectedProduct = item.name;
    selectedProductId = item.id;
    selectedImage = item.image;


    // ---------------------------------
    // Product Information
    // ---------------------------------

    document.getElementById("scoop-title").innerText =
        item.name;

    document.getElementById("scoop-desc").innerText =
        item.desc || item.description || "";

    document.getElementById("scoop-product-id").value =
        item.id;


    // ---------------------------------
    // Product Image Element
    // ---------------------------------

    const productImage =
        document.getElementById("scoop-image");


    // ---------------------------------
    // Function to Set Image
    // ---------------------------------

    function setProductImage(imagePath) {

        if (!imagePath) {
            imagePath = item.image;
        }

        // Remove /static/ if it already exists
        imagePath = imagePath.replace(/^\/static\//, "");

        productImage.src =
            "/static/" + imagePath;

        console.log(
            "Image Changed To:",
            productImage.src
        );
    }


    // ---------------------------------
    // Generate Size / Variant Options
    // ---------------------------------

    const sizeContainer =
        document.getElementById("size-options");

    sizeContainer.innerHTML = "";


    if (item.variants && item.variants.length > 0) {

        document.getElementById("size-heading").style.display =
            "block";


        // ---------------------------------
        // Create Radio Buttons
        // ---------------------------------

        item.variants.forEach(function (variant, index) {

            console.log(
                "Variant:",
                variant
            );

            console.log(
                "Variant Image:",
                variant.image
            );


            const label =
                document.createElement("label");

            label.className =
                "size-option";


            label.innerHTML = `
                <input
                    type="radio"
                    name="scoopSize"
                    value="${variant.size}"
                    data-variant-id="${variant.id}"
                    data-price="${variant.price}"
                    data-image="${variant.image || item.image}"
                    ${index === 0 ? "checked" : ""}
                >

                <span>
                    ${variant.size}<br>
                    ₹${variant.price}
                </span>
            `;


            sizeContainer.appendChild(label);

        });


        // ---------------------------------
        // First Variant
        // ---------------------------------

        const firstVariant =
            item.variants[0];


        selectedSize =
            firstVariant.size;

        selectedPrice =
            Number(firstVariant.price);

        selectedVariantId =
            firstVariant.id;

        selectedImage =
            firstVariant.image || item.image;


        // ---------------------------------
        // Display First Variant Image
        // ---------------------------------

        setProductImage(
            selectedImage
        );


        // ---------------------------------
        // Display First Variant Price
        // ---------------------------------

        document.getElementById(
            "selected-price"
        ).innerText =
            "₹" + selectedPrice;


        // ---------------------------------
        // Radio Button Change Event
        // ---------------------------------

        const radios =
            sizeContainer.querySelectorAll(
                "input[name='scoopSize']"
            );


        radios.forEach(function (radio) {

            radio.addEventListener(
                "change",
                function () {

                    // -----------------------------
                    // Selected Size
                    // -----------------------------

                    selectedSize =
                        this.value;


                    // -----------------------------
                    // Selected Price
                    // -----------------------------

                    selectedPrice =
                        Number(
                            this.dataset.price
                        );


                    // -----------------------------
                    // Selected Variant ID
                    // -----------------------------

                    selectedVariantId =
                        this.dataset.variantId;


                    // -----------------------------
                    // Selected Image
                    // -----------------------------

                    selectedImage =
                        this.dataset.image;


                    // -----------------------------
                    // Update Price
                    // -----------------------------

                    document.getElementById(
                        "selected-price"
                    ).innerText =
                        "₹" + selectedPrice;


                    // -----------------------------
                    // ⭐ Change Image
                    // -----------------------------

                    setProductImage(
                        selectedImage
                    );


                    // -----------------------------
                    // Debug
                    // -----------------------------

                    console.log(
                        "Selected Size:",
                        selectedSize
                    );

                    console.log(
                        "Selected Price:",
                        selectedPrice
                    );

                    console.log(
                        "Selected Variant ID:",
                        selectedVariantId
                    );

                    console.log(
                        "Selected Image:",
                        selectedImage
                    );

                }
            );

        });

    }

    else {

        // ---------------------------------
        // Product Without Variants
        // ---------------------------------

        document.getElementById(
            "size-heading"
        ).style.display =
            "none";


        selectedSize =
            "Standard";

        selectedPrice =
            Number(item.price || 0);

        selectedVariantId =
            null;

        selectedImage =
            item.image;


        // ---------------------------------
        // Display Price
        // ---------------------------------

        document.getElementById(
            "selected-price"
        ).innerText =
            "₹" + selectedPrice;


        // ---------------------------------
        // Display Product Image
        // ---------------------------------

        setProductImage(
            selectedImage
        );

    }


    // ---------------------------------
    // Open Popup
    // ---------------------------------

    document.getElementById(
        "scoopModal"
    ).style.display =
        "flex";
}
function openMysteryPopup_back(item) {

   
    console.log("ID:", item.id);
    console.log("Name:", item.name);
    console.log("Category:", item.category);
    console.log("Image:", item.image);
    console.log("Variants:", item.variants);

    selectedProduct = item.name;
    selectedProductId = item.id;
    
    document.getElementById("scoop-title").innerHTML =
        item.name;

    document.getElementById("scoop-desc").innerHTML =
        item.desc || item.description || "";

    document.getElementById("scoop-image").src =
        "/static/" + item.image;

    document.getElementById("scoopModal").style.display = "flex";
}

function openHairCandyPopup(){

selectedProduct="Hair Candy Scoop";

document.getElementById("scoop-title").innerHTML="Hair Candy Scoop";

document.getElementById("scoop-desc").innerHTML=
"A Scoop full of Hair Bands";

document.getElementById("scoop-image").src=
"/static/images/HairCandy.jpg";

document.getElementById("scoopModal").style.display="flex";

}
function openMysteryCupPopup(){

    selectedProduct = "Mystery Cup";
   
    currentPrices = {
        Small:99,
        Large:299
    };

    document.getElementById("scoop-title").innerHTML =
        "Mystery Cup";

    document.getElementById("scoop-desc").innerHTML =
        "A Cup Full of Mystery.";

    document.getElementById("scoop-image").src =
        "/static/images/MystryCup.jpg";

    document.getElementById("small-option").style.display = "inline-block";
    document.getElementById("medium-option").style.display = "none";
    document.getElementById("large-option").style.display = "inline-block";

    document.getElementById("small-price").innerHTML = "Small<br>₹99";
    document.getElementById("large-price").innerHTML = "Large<br>₹299";

    document.querySelector("input[value='Small']").checked = true;

   // selectSize("Small");

    document.getElementById("scoopModal").style.display = "flex";


}
function closeScoopPopup(){

document.getElementById("scoopModal").style.display="none";

}

function selectSize(size,price){

selectedSize=size;

selectedPrice=price;

document.getElementById("selected-price").innerHTML=price;

}
function selectSize(size) {

    selectedSize = size;

    selectedVariantId = currentPrices[size].id;

    selectedPrice = currentPrices[size].price;

    document.getElementById("selected-price").innerHTML =
        "₹" + selectedPrice;
}

function addSelectedScoop(){


addToCartPopUp(
    event,
    selectedProductId,
    selectedProduct,
    selectedSize,
    selectedPrice,
    document.getElementById("scoop-image").src
);

closeScoopPopup();

}
//This is from Add To Cart Button click call

function addToCartPopUp(
    event,
    productId,
    name,
    size,
    price,
    image
) {

    if (event) {
        event.stopPropagation();
    }

    price = Number(price);

    if (isNaN(price)) {
        console.error("Invalid price:", price);
        return;
    }

    // Unique key = Product ID + Variant Size
    const cartKey = productId + "-" + size;

    if (cart[cartKey]) {

        cart[cartKey].qty += 1;

    } else {

        cart[cartKey] = {
            id: productId,
            name: name,
            size: size,
            price: price,
            image: image,
            qty: 1
        };
    }

    localStorage.setItem(
        "cart",
        JSON.stringify(cart)
    );

    updateCartCount();

    console.log("Cart:", cart);
}

window.onclick = function(event) {
    let modal = document.getElementById("modal");
    if (event.target == modal) {
        modal.style.display = "none";
    }
};
