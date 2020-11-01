// Your web app's Firebase configuration
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
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
firebase.auth().onAuthStateChanged((firebaseUser) => {
  if (firebaseUser) {
    console.log("user : ", firebaseUser.uid);
    uid = firebaseUser.uid;
  } else {
    console.log("not logged in");
    window.location = "./accounts/login/";
    uid = null;
  }
});

var product_show = document.getElementById("product_show");

function getCSRFToken() {
  var cookieValue = null;
  if (document.cookie && document.cookie != "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      if (cookie.substring(0, 10) == "csrftoken" + "=") {
        cookieValue = decodeURIComponent(cookie.substring(10));
        break;
      }
    }
  }
  return cookieValue;
}
var data = {
  // csrfmiddlewaretoken: getCSRFToken(),
}

$.ajax({
  type: "Get",
  url: window.location.origin+"/api/allproduct/",
  data: data,
  success: function (value) {
    all_products = JSON.parse(value);
    product_show.innerHTML = "";
    for (product_dict of all_products){
      product = product_dict.fields;
      console.log(product);
      if (!product.inStock){
        inStock = "<Button class='btn btn-danger btn-sm'>Not in Stock</Button>";
      }
      else{
        inStock = "";
      }
      if (product.stars > 0){
      var rating = `<span class="d-flex bg-success text-light px-2 rating">${product.stars} <i
      class="fas fa-star rating-star my-auto ml-1" style="font-size: 12px;"></i></span>
<span class="ml-1 text-muted">(${product.num_rating})</span>`;
    } else {
      var rating = `<span class="text-dark">Be the first one to Rate this product.</span>`;
    }
      product_show.innerHTML += `<a href="./product/${product_dict.pk+"-"+product.title}" class="my-2" style="text-decoration: none;">
      <div class="card item" style="width: 18rem;">
          <img src="./media/${product.product_image}"
              class="card-img-top p-2 pt-4" alt="...">
          <div class="card-body">
              ${inStock}
              <h5 class="card-title">${product.title}</h5>
              <p class="text-muted ">${product.subtitle}</p>
              <div class="d-flex align-middle ">
                  ${rating}
              </div>
              <p class="mt-3" style="color: black; font-weight: 500;">₹${product.selling_price} <span
                      class="text-muted original-price">₹${product.marked_price}</span></p>
          </div>
      </div>
  </a>`
    }
  },
});

function goto() {
  // console.log("./accounts/profile/"+uid);
  window.location = `./accounts/profile/${uid}`;
}