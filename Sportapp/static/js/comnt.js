function myFunction() {
    var x = document.getElementById("subscription_form");
    if (x.style.display === "block") {
      x.style.display = "none";
    } else {
      x.style.display = "block";
    }
  }
  
  document.getElementById("subscribe").addEventListener("click", comment);
   function comment(){
    var div = document.getElementById("txtOutput");
    var txtName = document.getElementById("txtName").value;
    var today = new Date()
        if (txtName === ""){
        div.style.display= "none";
        }else{
    div.style.display = "block";
    document.getElementById("txtOutput").innerHTML +=  "<p>"+ today.getMinutes() + "m ago"+ "<br /><br />" + txtName + "</p><br />";
        document.getElementById("txtName").value='';
        }
      
   }