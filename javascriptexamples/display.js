function phonenumberValidate(){
	var Phonenumber=document.getElementById('Phonenumber').value;
	var PhonenumberId=document.getElementById('PhonenumberId')
	if(Phonenumber.length==8 || Phonenumber.length==10)
	{
		PhonenumberId.textContent="valid"
		PhonenumberId.style.color="green"
	}
	else
	{
		PhonenumberId.textContent="Invalid number"
		PhonenumberId.style.color="red"
	}
}
