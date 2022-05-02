function showFileName(){
    const fileName = document.getElementById('file-name')
    let file = document.getElementById("file");
    if(file.files.length > 0){
        fileName.innerHTML = file.files[0].name;
    }
}