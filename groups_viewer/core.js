var showFileName = () => {
    const fileName = document.getElementById('file-name')
    let file = document.getElementById("file");
    if(file.files.length > 0){
        fileName.innerHTML = file.files[0].name;
    }
}

// hsl is a method how uses variable h as a chromatic circle
var hslGenerator = (numberColors, s = 0, l = 0) => {
    if(numberColors < 5){
        var circleRange = 70;
    }else if(numberColors < 9){
        var circleRange = 180;
    }else{
        var circleRange = 360;
    }
    var colors = [], c = 0, color = '', hRange = Math.floor(circleRange / numberColors), h = 0;
        while(c < numberColors){
            h = h + hRange <= circleRange ? h + hRange : circleRange;
            color = `hsl(${h}, ${s}%, ${l}%)`;
            colors.push(color);
            c++;
        }
    return colors;
}

var getCsvFile = () => {

    const getFileExtension = (file) => { return file.split('.')[file.split('.').length - 1] }

    let file = document.getElementById('file');
    if(file.files.length > 0){
        let fr = new FileReader();
        let local_file = file.files[0]

        let local_file_extension = getFileExtension(local_file.name)
        if(local_file_extension.toLowerCase() === 'csv'){
            fr.readAsText(local_file);
            
            console.log('Passei aqui')
            // If we use onloadend, we need to check the readyState.
            fr.onload = function() {
                let file_content = fr.result.split(',');
                console.log(file_content)
            }

        }else{
            alert(`YOU SHOULD HAVE BEEN INFORMED A CSV FILE, NOT A ${local_file_extension.toUpperCase()} FILE!`)
        }
    }else{
        alert('YOU HAVE TO INFORM A CSV FILE!')
    }
}