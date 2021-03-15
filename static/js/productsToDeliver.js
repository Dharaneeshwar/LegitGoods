var firebaseConfig = {
  apiKey: "AIzaSyA47T1dM4C7nZaczOEkt_O1KcazxIZsAaw",
  authDomain: "legit-goods.firebaseapp.com",
  databaseURL: "https://legit-goods.firebaseio.com",
  projectId: "legit-goods",
  storageBucket: "legit-goods.appspot.com",
  messagingSenderId: "948613007995",
  appId: "1:948613007995:web:fd801774c6eff66e71f0de",
};
console.log("success");
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
firebase.auth().onAuthStateChanged((firebaseUser) => {
  if (firebaseUser) {
    console.log("user : ", firebaseUser.uid);
    const uid = firebaseUser.uid;
    data = {
        'uid' : uid
    }
    $.ajax({
      type: "Get",
      url: window.location.origin + "/api/productsToDeliver/",
      data: data,
      success: function (value) {
        console.log(value[0]);
        list = document.getElementById('list');
        list.innerHTML = "";  
        if (value[0] == undefined){
          list.innerHTML += '<b class="my-5 text-center" style="padding-top:100px; padding-bottom: 90px;">No Products Sold</b>';  
        } else {
        for (ele of value){
          list.innerHTML += `<div class="list-group-item text-dark">
          <div class="d-flex w-100 justify-content-between">
              <h3 class="mb-1 text-primary">${ele.notification}</h3>
              <small></small>
          </div>
          <p class="my-1"><b>Product: </b>${ele.prod_title}</p>
          <p class="mb-1"><b>Quantity: </b>${ele.quantity}</p>
          <p class="mb-1"><b>Amount: </b> ${ele.amount}</p>
          <p class="mb-1"><b>Bought By: </b> ${ele.user_name}</p>
          <p class="mb-1"><b>Email: </b>${ele.user_email}</p>
          <p class="mb-1"><b>Address: </b>${ele.user_address}</p>
          <p class="mb-1"><b>State: </b>${ele.user_state}</p>
          <p class="mb-1"><b>ZipCode: </b>${ele.user_pin}</p>
          <p class="mb-1"><b>Country: </b>${ele.user_country}</p>
      </div>`;
      }
    }
      },
    });
  } else {
    console.log("not logged in");
    window.location = "../accounts/login/";
    const uid = null;
  }
});
