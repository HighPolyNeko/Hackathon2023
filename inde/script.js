function toggleOrder(button) {
    let orderAmount = button.nextElementSibling;
    if (orderAmount.style.display === "none" || orderAmount.style.display === "") {
        button.style.display = "none";
        orderAmount.style.display = "block";
    }
}

function increment(button) {
    let amount = button.previousElementSibling;
    amount.innerText = parseInt(amount.innerText) + 1;
}

function decrement(button) {
    let amount = button.nextElementSibling;
    if (parseInt(amount.innerText) > 0) {
        amount.innerText = parseInt(amount.innerText) - 1;
        if (parseInt(amount.innerText) === 0) {
            let addBtn = button.parentElement.previousElementSibling;
            addBtn.style.display = "block";
            button.parentElement.style.display = "none";
        }
    }
}