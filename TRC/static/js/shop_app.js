const showPrice = ()=> {
    const foto = document.getElementsByClassName('.thumbnail');
    const price = document.getElementsByClassName('.price');


    foto.addEventListener("mouseover",()=> {
        console.log("This alert box was called with the onload event")
    });
}

showPrice();
