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
max_number = 10;
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
      url: window.location.origin + "/api/getCartinfo/",
      success: function (value) {
        status = value.data.status;
        max_number = value.data.max_number;
        console.log(status);
        if (!value.data.product_available){
          console.log("not available");
          cart_area.innerHTML = "";
          cart_area.innerHTML = `<h2>Sold Out</h2>
          <h4 class="text-muted mb-4">This item is currently out of stock.</h4>`
        }
        else if (status == 'true') {
            options = generateOptions();
            cart = JSON.parse(value.data.cart)[0].fields;
            quantity = cart.quantity;
            console.log(quantity,'hi');
            cart_area.innerHTML = "";
            cart_area.innerHTML = `<div class="d-flex">
          <button class="btn btn-outline-danger px-5 mt-3" onclick="removefromcart()">
              Remove from Cart<i class="fas fa-cart-arrow-down ml-2" style="font-size: 18px"></i>
          </button>
      </div>
      <p style="font-size: 20px; margin-top: 20px">
          Quantity :

          <select class="btn btn-white border border-dark ml-2" name="quantity" id="quantity" onchange="quantitychange()">
              ${options}
          </select>
      </p>`;
      document.getElementById('quantity').value = quantity;
        } else {
          options = generateOptions();
          cart_area.innerHTML = "";
          cart_area.innerHTML = `<div class="d-flex">
          <button class="btn btn-primary px-5 mt-3" onclick="addtocart()">
          Add To Cart<i class="fas fa-cart-plus ml-2 text-light" style="font-size: 18px"></i>
          </button>
          </div>
          <p style="font-size: 20px; margin-top: 20px">
              Quantity :
    
              <select class="btn btn-white border border-dark ml-2" name="quantity" id="quantity" onchange="quantitychange()">
                  ${options}
              </select>
          </p>
          </div>
          `;
        }
      },
    });
  } else {
    console.log("not logged in");
    window.location = "../../accounts/login/";
    uid = null;
  }
});

var product_show = document.getElementById("product_show");

function addtocart() {
    console.log("quant",document.getElementById('quantity').value);
    data = {
        quantity:document.getElementById('quantity').value,
        product_id:product_id,
        uid:uid
    }
    $.ajax({
        type: "GET",
        data: data,
        url: window.location.origin + "/api/addToCart/",
        success: function (value) {
          console.log(value);
          cart_area.innerHTML = "";
          cart_area.innerHTML = `<div class="d-flex">
          <button class="btn btn-outline-danger px-5 mt-3" onclick="removefromcart()">
                  Remove from Cart<i class="fas fa-cart-arrow-down ml-2" style="font-size: 18px"></i>
              </button>
      </div>
      <p style="font-size: 20px; margin-top: 20px">
          Quantity :

          <select class="btn btn-white border border-dark ml-2" name="quantity" id="quantity" onchange="quantitychange()">
              <option value="1">1</option>
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
      </p>`
        document.getElementById('quantity').value = data.quantity;
        },
      });
}

function removefromcart() {
    data = {
        quantity:quantity_ele.value,
        product_id:product_id,
        uid:uid
    }
    $.ajax({
        type: "GET",
        data: data,
        url: window.location.origin + "/api/removeFromCart/",
        success: function (value) {
          console.log(value);
          cart_area.innerHTML = "";
          cart_area.innerHTML = `<div class="d-flex">
          <button class="btn btn-primary px-5 mt-3" onclick="addtocart()">
                  Add To Cart<i class="fas fa-cart-plus ml-2 text-light" style="font-size: 18px"></i>
            </button>
      </div>
      <p style="font-size: 20px; margin-top: 20px">
          Quantity :

          <select class="btn btn-white border border-dark ml-2" value="${data.quantity}" name="quantity" id="quantity" onchange="quantitychange()">
              <option value="1">1</option>
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
      </p>`;
        },
      });
}

// TODO on quantity change

function quantitychange(){
  data = {
    quantity:document.getElementById('quantity').value,
    product_id:product_id,
    uid:uid 
  }
  $.ajax({
    type: "GET",
    data: data,
    url: window.location.origin + "/api/updateQuantity/",
    success: function (value) {
      console.log(value);
    },
  });
}


function generateOptions() {
  options = '';
  console.log("max",max_number);
  limit  = max_number<10?max_number:10;
  console.log(limit);
  for (i=0;i<limit;i++){
    console.log("hi");
    options = options.concat(`<option value="${i+1}">${i+1}</option>`);
  }
  console.log("options",options);
  return options;
}