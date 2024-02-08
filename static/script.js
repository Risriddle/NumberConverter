// Function to set up event listeners
function setUpListeners() {
    var elements = document.getElementsByTagName('button');

}
var x,y,z
$('button').addClass('btn')
$('.convert').click(function() {
    // Assign the clicked button's id to variable x
    z = $(this).attr('id');
    myFunction()
    console.log('Selected button id:', z);
    // You can perform further actions with variable x here
}); 

$('.from').click(function() {
    // Assign the clicked button's id to variable x
    x = $(this).attr('id');
    console.log('Selected button id:', x);
    // You can perform further actions with variable x here
}); 

$('.to').click(function() {
    // Assign the clicked button's id to variable x
    y = $(this).attr('id');
    console.log('Selected button id:', y);
    // You can perform further actions with variable x here
}); 

// Function to be executed on button click
function myFunction() {
    
    var number = document.getElementById("num").value;
    console.log(number);

    // Send button ID to Flask server via fetch
    fetch('/home', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ from: x, to: y,number:number ,c:z})
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data !== null) {
                console.log(data);
                document.getElementById("output").innerText = data.msg;

            } else {
                console.log("Data is null");
            }
        })
        .catch(error => console.error('Error:', error));
}

// Event listener to reset the value of "number" variable on page load
document.addEventListener("DOMContentLoaded", function() {
    // Clear the value of "number" variable
    var number = document.getElementById("num").value = '';
    setUpListeners(); // Set up event listeners after resetting the value
});
