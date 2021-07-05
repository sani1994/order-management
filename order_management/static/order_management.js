const productList = document.getElementsByClassName('dropdown-menu')
const addToCartBtn = document.getElementById('addToCart')
const productTable = document.getElementById('productTable')
const selectedProduct = document.getElementById('selectedProduct')
const quantity = document.getElementById('amount')
const totalPrice = document.getElementById('totalPrice')
const submitBtn = document.getElementById('submit-btn')
const csrf = document.getElementsByName("csrfmiddlewaretoken")
const url = window.location.href

function addToCart(trigger) {
   let productName = selectedProduct.options[selectedProduct.selectedIndex].text
   let productNewQuantity = quantity.value || 0
   let productPrice = selectedProduct.options[selectedProduct.selectedIndex].getAttribute('data-price')
   let productCode = selectedProduct.options[selectedProduct.selectedIndex].getAttribute('data-code')

   if (productTable.rows[productCode]) {
      let productQty = productTable.rows[productCode].cells[1].innerHTML
      let qty = parseInt(productQty)
      qty += parseInt(productNewQuantity)
      productTable.rows[productCode].cells[1].innerHTML = qty
      productTable.rows[productCode].cells[2].innerHTML = (qty * productPrice)
   } else {
      let productData = productTable.innerHTML
      productData += `<tr id="${productCode}"><td>${productName}</td><td>${productNewQuantity}</td><td>${productNewQuantity * productPrice}</td></tr>`
      productTable.innerHTML = productData
   }

}

function calculateTotal() {
   let total = 0
   for (let i = 1; i < productTable.rows.length - 1; i++) {
      total += parseInt(productTable.rows[i].cells[2].innerText)
   }
   document.getElementById('totalPrice').innerHTML = total
}

function submitOrder() {
   data = {}
   data['csrfmiddlewaretoken'] = csrf[0].value
   data['customer_name'] = document.getElementById('cName').value
   data['phone_number'] = document.getElementById('pNumber').value
   data['email'] = document.getElementById('email').value
   for (let i = 1; i < productTable.rows.length - 1; i++) {
      data[productTable.rows[i].id] = productTable.rows[i].cells[1].innerText
   }

   $.ajax({
      type: 'POST',
      url: `${url}/submit/`,
      data: data,
      dataType: 'json',
      success: (response) => {
         order_id = response.order_id
         window.location.href = `${url}/submit/${order_id}`
      },
      error: (error) => {
         console.log(error)
      }
   })
}

addToCartBtn.addEventListener('click', (e) => {
   e.preventDefault();
   addToCart($(this));
   calculateTotal();
})

submitBtn.addEventListener('click', (e) => {
   e.preventDefault();
   submitOrder();
})
