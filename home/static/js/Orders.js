function toggleDetails(id){

    let row = document.getElementById(id);

    if(row.style.display === "none" || row.style.display === ""){

        row.style.display = "table-row";

    }else{

        row.style.display = "none";

    }

}