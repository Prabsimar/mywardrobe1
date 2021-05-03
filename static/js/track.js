var head1 = document.getElementById("head1");
var head2 = document.getElementById("head2");
var head3 = document.getElementById("head3");


var f1 = firebase.database().ref().child("Variable").child("Lat") ;
var f2 = firebase.database().ref().child("Variable").child("Long") ;
var f3 = firebase.database().ref().child("Variable").child("Delivery") ;

f1.on('value',function(datasnapshot) {
	head1.innerText = datasnapshot.val();
})
f2.on('value',function(datasnapshot1) {
	head2.innerText = datasnapshot1.val();
})
f3.on('value',function(datasnapshot2) {
	head3.innerText = datasnapshot2.val();
})