var updatebtns=document.getElementsByClassName('update-cart')
for(var i=0;i<updatebtns.length;i++){
    updatebtns[i].addEventListener('click',function(){
        var productId=this.dataset.product;
        var action=this.dataset.action;
        console.log('productId:',productId,'action:',action);

        console.log('User:',user)
        if(user==='AnonymousUser'){
            console.log("Nt logged in")
        }
        else{
            updateUserOrder(productId,action);
        }
    })
}


function updateUserOrder(productId,action){
    console.log("added to cart");

    var url='/update_item'

    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId':productId,'action':action})
    })

    .then((response)=>response.json())
    .then((data)=>{
        console.log('data:',data);
        location.reload()

    })
    

}