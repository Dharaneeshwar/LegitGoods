// Your web app's Firebase configuration
var cart_area = document.getElementById("cart_area");
var quantity_ele = document.getElementById("quantity");
var firebaseConfig = {
  apiKey: "AIzaSyA47T1dM4C7nZaczOEkt_O1KcazxIZsAaw",
  authDomain: "legit-goods.firebaseapp.com",
  databaseURL: "https://legit-goods.firebaseio.com",
  projectId: "legit-goods",
  storageBucket: "legit-goods.appspot.com",
  messagingSenderId: "948613007995",
  appId: "1:948613007995:web:fd801774c6eff66e71f0de",
};
var uid = "";
total = 0.0;
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
firebase.auth().onAuthStateChanged((firebaseUser) => {
  if (firebaseUser) {
    console.log("user : ", firebaseUser.uid);
    uid = firebaseUser.uid;
    $.ajax({
      type: "GET",
      data: {
        uid: uid,
        product_id: product_id,
      },
      url: window.location.origin + "/api/getCartProdcuts/",
      success: function (value) {
        cartItems = document.getElementById("cartItems");
        cartItems.innerHTML = "";
        for (ele of value){
            // console.log(ele);
            cartItems.innerHTML += `<div class="row mt-5 justify-content-between border-bottom py-3">
            <div class="col-3">
                <img src="../../static/media/${ele.image}" alt="" height="200px">
            </div>
            <div class="col-6">
                <a class="text-primary" style="font-size: 22px; font-weight: 500;" onclick="openprod()">
                    ${ele.title}
                </a> <br>
                <p class="text-muted mt-2" style="font-size: 20px; font-weight: 500;">${ele.subtitle}</p>
                <p style="font-size: 20px;">Price : <b>₹${ele.price}</b></p>
                <p style="font-size: 20px; margin-top: 20px">
                    Quantity :

                    <select class="btn btn-white border border-dark ml-2" onchange="quantitychange(${ele.id},${ele.price})" name="quantity-${ele.id}" id="quantity-${ele.id}">
                        <option value="0">0 (delete)</option>
                        <option value="1" selected>1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                        <option value="5">5</option>
                        <option value="6">6</option>
                        <option value="7">7</option>
                        <option value="8">8</option>
                        <option value="9">9</option>
                        <option value="10">10</option>
                    </select>
                </p>

            </div>
            <div class="col-1">
                <p id="price-${ele.id}" style="font-size: 20px; font-weight: bold;">₹${ele.quantity*ele.price}</p>
            </div>
        </div>`;
        document.getElementById('quantity-'+ele.id).value = ele.quantity;
        console.log('quan',ele.quantity);
        console.log(ele.title,'quantity-'+ele.id,ele.quantity,document.getElementById('quantity-'+ele.id).value);
        total += ele.quantity*ele.price;
        // BUG last ele only sets quantity
        }
        console.log('after loop : quantity-5 - ',document.getElementById('quantity-5').value);
        document.getElementById('subtotal').innerText = " ₹"+total;
      },
    });
  } else {
    console.log("not logged in");
    window.location = "../../accounts/login/";
    uid = null;
  }
});

function quantitychange(id,price){
    data = {
      quantity:document.getElementById('quantity-'+id).value,
      product_id:id,
      uid:uid 
    }
    document.getElementById('price-'+id).innerHTML = '₹'+data.quantity*price
    $.ajax({
      type: "GET",
      data: data,
      url: window.location.origin + "/api/updateQuantity/",
      success: function (value) {
        console.log(value);
      },
    });
  }

function openprod() {
    
}  

