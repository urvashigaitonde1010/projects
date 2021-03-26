function UserAction() {
  // var xhttp = new XMLHttpRequest();
  // xhttp.open("GET", 'http://dummy.restapiexample.com/api/v1/employees', true);
  // // xhttp.setRequestHeader("Content-type", "application/json");
  // xhttp.send();
  // // var response = JSON.parse(xhttp.responseText);
  // console.log(xhttp.responseText)
  $.ajax({
    url: "http://127.0.0.1:8000/demo/",
    type: "GET",
    // data: 'ID=1&Name=John&Age=10', // or $('#myform').serializeArray()
    success: function(data) {
      console.log(data);
    }
  });
}

function showJuices(e) {
  if (e.target.id == "1dayBtn") {
    $("#juices1").slideUp("slow");
    $("#juices2").slideDown("slow");
  } else {
    $("#juices2").slideUp("slow");
    $("#juices1").slideDown("slow");
  }
  $("#subscribeBtn").prop("disabled", false);
}
$("#subscribeBtn").prop("disabled", false);
function subscribe(event) {
  event.preventDefault();
  console.log("Aa");
  var name = document.getElementById("name").value;
  var mobile = document.getElementById("mobile").value;
  var email = document.getElementById("email").value;
  var address = document.getElementById("address").value;
  if (email == "") {
    email = "None";
  }
  if (name == "" || mobile == "" || address == "") {
    alert("Please fill out mandatory fields.");
  } else {
    var sourceOfInfoElements = document.getElementsByName("sourceOfInfo");
    var sourceOfInfo = "";
    for (var i = 0; i < sourceOfInfoElements.length; i++) {
      if (sourceOfInfoElements[i].checked) {
        sourceOfInfo += sourceOfInfoElements[i].value;
      }
    }
    if (sourceOfInfo == "") {
      sourceOfInfo = "None";
    }
    var medical = document.getElementById("medical").value;
    if (medical == "") {
      medical = "None";
    }
    // var subscriptionDurationElements = document.getElementsByName("gridRadios");
    // var subscriptionDuration = "";
    // for (var i = 0; i < subscriptionDurationElements.length; i++) {
    //   if (subscriptionDurationElements[i].checked) {
    //     subscriptionDuration += subscriptionDurationElements[i].value;
    //   }
    // }

    // var juices = "";
    // var quantity = "1";
    // if (subscriptionDuration == "1") {
    //   var juiceElements = document.getElementsByName("juicesRadio");
    //   for (var i = 0; i < juiceElements.length; i++) {
    //     if (juiceElements[i].checked) {
    //       juices += juiceElements[i].value;
    //     }
    //   }
    // } else {
    //   for (var i = 1; i <= 4; i++) {
    //     if (document.getElementById("juice1_" + i).checked) {
    //       juices += document.getElementById("juice1_" + i).value + ", ";
    //     }
    //   }
    //   quantity = document.getElementById("quantity").value;
    // }

    // if (juices == "") {
    //   alert("You did not select any juices. Please select at least one.");
    // } else {
    //   var paymentOption = "";
    //   var paymentOptionElements = document.getElementsByName("payment");
    //   for (var i = 0; i < paymentOptionElements.length; i++) {
    //     if (paymentOptionElements[i].checked) {
    //       paymentOption += paymentOptionElements[i].value;
    //     }
    //   }

    postJson = {
      customer_name: "",
      email: "",
      mobile_no: "",
      address: "",
      //   subscriptionDuration: "",
      source_of_information: "",
      medical_condition: ""
      //   payment_method: "",
      //   juices: "",
      //   quantity: ""
    };

    postJson.customer_name = name;
    postJson.email = email;
    postJson.mobile_no = mobile;
    postJson.address = address;
    //   postJson.subscriptionDuration = subscriptionDuration;
    postJson.source_of_information = sourceOfInfo;
    postJson.medical_condition = medical;
    //   postJson.payment_method = paymentOption;
    //   postJson.juices = juices;
    //   postJson.quantity = quantity;

    // fetch('http://13.126.175.152:80/app/subscribe/', {
    //   method: 'POST',
    //   headers: {
    //     'Accept': 'application/json, text/plain, */*',
    //     'Content-Type': 'application/json',
    //     // 'Authorization':'Token ed73db9bf18f3c3067be926d5ab64cec9bcb9c5e'
    //   },
    //   body: postJson
    // }).then(res=>res.json())
    //   .then(res => console.log(res));
    console.log(postJson);
    $.ajax({
      type: "POST",
      //   url: "http://13.126.175.152:80/app/subscribe/",
      url: "http://127.0.0.1:8000/subscribe/",
      // csrfmiddlewaretoken: "{{ csrf_token }}",
      data: JSON.stringify(postJson),
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json"
      },
      success: function(data) {
        if (data == "Saved") {
          alert("Thank you for subscribing to hnh.");
          document.location.reload();
        }
        console.log(data);
      },
      error: function(XMLHttpRequest, textStatus, errorThrown) {
        alert(
          "some error " +
            String(errorThrown) +
            String(textStatus) +
            String(XMLHttpRequest.responseText)
        );
      }
    });
  }
}
// }
