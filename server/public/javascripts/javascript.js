

/************** declare every digital-out Switch by Element-ID ********************/
var elem_DO1 = document.getElementById("DO1");
var elem_DO2 = document.getElementById("DO2");
var elem_DO3 = document.getElementById("DO3");
var elem_DO4 = document.getElementById("DO4");
/**********************************************************************************/

/************** declare element for reloading overview-page ***********************/
var elem_DO_Reload = document.getElementById("DO_Reload");
/**********************************************************************************/

/************** declare every digital-in circle by Element-ID *********************/
var elem_DI1 = document.getElementById("DI1");
var elem_DI2 = document.getElementById("DI2");
var elem_DI3 = document.getElementById("DI3");
var elem_DI4 = document.getElementById("DI4");
var elem_DI5 = document.getElementById("DI5");
var elem_DI6 = document.getElementById("DI6");
var elem_DI7 = document.getElementById("DI7");
var elem_DI8 = document.getElementById("DI8");
/**********************************************************************************/

/************** declare elements for reading and writing the analog-out ***********/
var elem_AO1_value = document.getElementById("AO1_Value");
var elem_AO1_write = document.getElementById("AO1_Write");
/**********************************************************************************/

/************** eventlistener "click" for reacting on pressed digital-out switch **/
elem_DO1.addEventListener("click", DO1);
elem_DO2.addEventListener("click", DO2);
elem_DO3.addEventListener("click", DO3);
elem_DO4.addEventListener("click", DO4);
/**********************************************************************************/

/************** eventlistener "click" for return to overview-page *****************/
elem_DO_Reload.addEventListener("click", DO_Reload);
/**********************************************************************************/

/************** eventlistener "click" for writing the given analog-out value ******/
elem_AO1_write.addEventListener("click", AO1);
/**********************************************************************************/


/************** Reading the current value of the digital outputs and based on that, changing the color ******************/
async function DI_value(){
    //getting the current digital-input value and create an readabel 8-digit-binary array of it
    fetch('/api/v1/di/value');
    const response = await fetch('digital_in_value.json');
    console.log(response.toString());
    let DI_Value = await response.json();
    console.log("Nach await");
    let DI_Value_bin = DI_Value.toString(2).padStart(8,'0');
    console.log("Nach toString");
    let DI_Value_Array = DI_Value_bin.split("");
    console.log("Nach Split");
    let DI_Value_List = DI_Value_Array.reverse();
    console.log(DI_Value_List);
    
    //DI1
    if (DI_Value_List[0] == 1){
        elem_DI1.style.backgroundColor = "#6EC800";
    } else{
        elem_DI1.style.backgroundColor = "#DEDFE1";
    }
    //DI2
    if (DI_Value_List[1] == 1){
        elem_DI2.style.backgroundColor = "#6EC800";
    } else{
        elem_DI2.style.backgroundColor = "#DEDFE1";
    }
    //DI3
    if (DI_Value_List[2] == 1){
        elem_DI3.style.backgroundColor = "#6EC800";
    } else{
        elem_DI3.style.backgroundColor = "#DEDFE1";
    }
    //DI4
    if (DI_Value_List[3] == 1){
        elem_DI4.style.backgroundColor = "#6EC800";
    } else{
        elem_DI4.style.backgroundColor = "#DEDFE1";
    }
    //DI5
    if (DI_Value_List[4] == 1){
        elem_DI5.style.backgroundColor = "#6EC800";
    } else{
        elem_DI5.style.backgroundColor = "#DEDFE1";
    }
    //DI6
    if (DI_Value_List[5] == 1){
        elem_DI6.style.backgroundColor = "#6EC800";
    } else{
        elem_DI6.style.backgroundColor = "#DEDFE1";
    }
    //DI7
    if (DI_Value_List[6] == 1){
        elem_DI7.style.backgroundColor = "#6EC800";
    } else{
        elem_DI7.style.backgroundColor = "#DEDFE1";
    }
    //DI8
    if (DI_Value_List[7] == 1){
        elem_DI8.style.backgroundColor = "#6EC800";
    } else{
        elem_DI8.style.backgroundColor = "#DEDFE1";
    }
    
    //reload data every 500ms
    setTimeout(DI_value, 1000);
}
//running the DI_Value() -Function to return the current state of the digital inputs
DI_value();

/************************************************************************************************/

/************** Switch the digital outputs to true / false **************************************/
function DO1(){
    fetch('/api/v1/do/1', {
        mode : "no-cors",
        method : 'post'
    })
}
function DO2(){
    fetch('/api/v1/do/2', {
        mode : "no-cors",
        method : 'post'
    })
}
function DO3(){
    fetch('/api/v1/do/3', {
        mode : "no-cors",
        method : 'post'
    })
}
function DO4(){
    fetch('/api/v1/do/4', {
        mode : "no-cors",
        method : 'post'
    })
}
/********************************************************************************************************/

/****** When reloading the overview-page, DO-Switches are being reset. Therefore turn DO-Data to 0 ******/
function DO_Reload(){
    fetch('/api/v1/do/reload', {
        mode : "no-cors",
        method : 'post'
    })
}
/********************************************************************************************************/

/********** Writing AO1 Value to data (currently not working) *******************************************/
function AO1(){
    var AO1_value_to_write = elem_AO1_value.value;
    console.log(elem_AO1_value.value)
    fetch('analog_out_value.json', {
        mode : "no-cors",
        method : "post",
        headers : {
            "Content-Type": "application/json"
        },
        body : JSON.stringify(AO1_value_to_write)
    })
}
/******************************************************************************************************/