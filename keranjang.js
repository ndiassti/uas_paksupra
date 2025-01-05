const cartIcon = document.getElementById("cart-icon");
const cartPopup = document.getElementById("cart-popup");
const cartItemsList = document.getElementById("cart-items");
const cartCount = document.getElementById("cart-count");
const cartTotal = document.getElementById("cart-total");
const checkoutButton = document.getElementById("checkout-button");

let cart = [];

function addToCart(itemName, itemPrice) {
    cart.push({ name: itemName, price: itemPrice });
    updateCart();
}

function updateCart() {
    cartCount.textContent = cart.length;
    cartItemsList.innerHTML = "";
    let total = 0;
    cart.forEach(item => {
        total += item.price;
        const li = document.createElement("li");
        li.innerHTML = `${item.name} - Rp ${item.price.toLocaleString()} <button onclick="removeItem('${item.name}')">Hapus</button>`;
        cartItemsList.appendChild(li);
    });
    cartTotal.textContent = `Rp ${total.toLocaleString()}`;
}

function removeItem(itemName) {
    cart = cart.filter(item => item.name !== itemName);
    updateCart();
}

cartIcon.addEventListener("click", () => {
    cartPopup.style.display = cartPopup.style.display === "none" ? "block" : "none";
});

checkoutButton.addEventListener("click", () => {
    if (cart.length === 0) return alert("Keranjang kosong!");
    alert("Checkout berhasil!");
    cart = [];
    updateCart();
    cartPopup.style.display = "none";
});