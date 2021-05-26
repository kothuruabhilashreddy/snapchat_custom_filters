const tuner = document.getElementById("tuner");
arrangeAll();

function arrangeAll(){

    tuner.innerHTML = `
        <div id="eyes"> </div>
        <div id = "nose"></div>
        <div id="ear"></div>
    `;
    var eyes = document.getElementById("eyes");
    var nose = document.getElementById("nose");
    var ear=document.getElementById("ear");
    arrangeEyes(eyes);
    arrangenose(nose);
    arrangeear(ear);
}

function arrangeEyes(eyes){
    arr = []
    imag = ["https://raw.githubusercontent.com/kothuruabhilashreddy/snapchat_custom_filters/main/images/eyes/1.jpg",
            "https://raw.githubusercontent.com/kothuruabhilashreddy/snapchat_custom_filters/main/images/eyes/2.jpg",
            "https://raw.githubusercontent.com/kothuruabhilashreddy/snapchat_custom_filters/main/images/eyes/3.jpg",
            "https://raw.githubusercontent.com/kothuruabhilashreddy/snapchat_custom_filters/main/images/eyes/4.jpg",
            "https://raw.githubusercontent.com/kothuruabhilashreddy/snapchat_custom_filters/main/images/eyes/5.jpg",
            "https://raw.githubusercontent.com/kothuruabhilashreddy/snapchat_custom_filters/main/images/eyes/6.jpg",
            "https://raw.githubusercontent.com/kothuruabhilashreddy/snapchat_custom_filters/main/images/eyes/7.jpg",
            "https://raw.githubusercontent.com/kothuruabhilashreddy/snapchat_custom_filters/main/images/eyes/8.jpg",
            "https://raw.githubusercontent.com/kothuruabhilashreddy/snapchat_custom_filters/main/images/spects/1.jpg",
            "https://raw.githubusercontent.com/kothuruabhilashreddy/snapchat_custom_filters/main/images/spects/2.jpg",
            "https://raw.githubusercontent.com/kothuruabhilashreddy/snapchat_custom_filters/main/images/spects/3.jpg",
            "https://raw.githubusercontent.com/kothuruabhilashreddy/snapchat_custom_filters/main/images/spects/4.jpg",
            "https://raw.githubusercontent.com/kothuruabhilashreddy/snapchat_custom_filters/main/images/spects/5.jpg"
            ];
    
    for(var i=0;i<imag.length;i++){
        arr.push(
        {    
            img : imag[i]
        });
        
    }
    eyes.innerHTML =  arr.map( (value) => { 
        return  `
        <label>
        <input type="radio"  name= "eye" value = ${value.img}>
        <img src = ${value.img} width=100 height=80>
        </label>`
    } ).join('');
}

function arrangenose(nose){
    arr=[]
    imag = ["https://raw.githubusercontent.com/kothuruabhilashreddy/snapchat_custom_filters/main/images/nose/1.jpg",
            "https://raw.githubusercontent.com/kothuruabhilashreddy/snapchat_custom_filters/main/images/nose/2.jpg",
            "https://raw.githubusercontent.com/kothuruabhilashreddy/snapchat_custom_filters/main/images/nose/3.jpg",
            "https://raw.githubusercontent.com/kothuruabhilashreddy/snapchat_custom_filters/main/images/nose/4.jpg",
            "https://raw.githubusercontent.com/kothuruabhilashreddy/snapchat_custom_filters/main/images/nose/5.jpg",
            "https://raw.githubusercontent.com/kothuruabhilashreddy/snapchat_custom_filters/main/images/nose/6.jpg",
            "https://raw.githubusercontent.com/kothuruabhilashreddy/snapchat_custom_filters/main/images/nose/7.jpg",
            "https://raw.githubusercontent.com/kothuruabhilashreddy/snapchat_custom_filters/main/images/nose/8.jpg",
            "https://raw.githubusercontent.com/kothuruabhilashreddy/snapchat_custom_filters/main/images/nose/9.jpg",
            "https://raw.githubusercontent.com/kothuruabhilashreddy/snapchat_custom_filters/main/images/nose/10.jpg"

            ];  
    for(var i=0;i<imag.length;i++){
        arr.push(
        {    
            img : imag[i]
        });     
    }
    nose.innerHTML =  arr.map( (value) => { 
        return  `
        <label>
        <input type="radio"  name="nose" value = ${value.img}>
        <img src = ${value.img} width=100 height=80>
        </label>`
    } ).join('');
}

function arrangeear(ear){
    arr = []
    imag = ["https://raw.githubusercontent.com/kothuruabhilashreddy/snapchat_custom_filters/main/images/ears/1.jpg",
            "https://raw.githubusercontent.com/kothuruabhilashreddy/snapchat_custom_filters/main/images/ears/2.jpg",
            "https://raw.githubusercontent.com/kothuruabhilashreddy/snapchat_custom_filters/main/images/ears/3.jpg",
            "https://raw.githubusercontent.com/kothuruabhilashreddy/snapchat_custom_filters/main/images/ears/4.jpg",
            "https://raw.githubusercontent.com/kothuruabhilashreddy/snapchat_custom_filters/main/images/ears/5.jpg",
            "https://raw.githubusercontent.com/kothuruabhilashreddy/snapchat_custom_filters/main/images/ears/6.jpg",
            "https://raw.githubusercontent.com/kothuruabhilashreddy/snapchat_custom_filters/main/images/ears/7.jpg",
            "https://raw.githubusercontent.com/kothuruabhilashreddy/snapchat_custom_filters/main/images/ears/8.jpg",
            "https://raw.githubusercontent.com/kothuruabhilashreddy/snapchat_custom_filters/main/images/ears/9.jpg",
            "https://raw.githubusercontent.com/kothuruabhilashreddy/snapchat_custom_filters/main/images/ears/10.jpg",
            ];
    
    for(var i=0;i<imag.length;i++){
        arr.push(
        {    
            img : imag[i]
        });
        
    }
    ear.innerHTML =  arr.map( (value) => { 
        return  `
        <label>
        <input type="radio"  name= "ear" value = ${value.img}>
        <img src = ${value.img} width=100 height=80>
        </label>`
    } ).join('');
}