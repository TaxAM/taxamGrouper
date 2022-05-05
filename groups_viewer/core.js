var showFileName = () => {
    const fileName = document.getElementById('file-name')
    let file = document.getElementById("file")
    if(file.files.length > 0){
        fileName.innerHTML = file.files[0].name
    }
}

// hsl is a method how uses variable h as a chromatic circle
var hslGenerator = (numberColors, s = 0, l = 0) => {
    if(numberColors < 5){
        var circleRange = 70
    }else if(numberColors < 9){
        var circleRange = 180
    }else{
        var circleRange = 360
    }
    var colors = [], c = 0, color = '', hRange = Math.floor(circleRange / numberColors), h = 0
        while(c < numberColors){
            h = h + hRange <= circleRange ? h + hRange : circleRange
            color = `hsl(${h}, ${s}%, ${l}%)`
            colors.push(color)
            c++
        }
    return colors
}

var getCsvFile = () => {

    const getFileExtension = (file) => { return file.split('.')[file.split('.').length - 1] }

    let file = document.getElementById('file')
    if(file.files.length > 0){
        let fr = new FileReader()
        let local_file = file.files[0]

        let local_file_extension = getFileExtension(local_file.name)
        if(local_file_extension.toLowerCase() === 'csv'){
            fr.readAsText(local_file)
            let cards = []
            // If we use onloadend, we need to check the readyState.
            fr.onload = function() {
                const file_content_lines = fr.result.split(/\r\n|\n/).filter(n => n != '')
                // Try to return this file_content_lines to createCard
                createCard(file_content_lines)
            }

        }else{
            alert(`YOU SHOULD HAVE BEEN INFORMED A CSV FILE, NOT A ${local_file_extension.toUpperCase()} FILE!`)
        }
    }else{
        alert('YOU HAVE TO INFORM A CSV FILE!')
    }
}

var createCard = (file_content_lines) => {

    console.log(file_content_lines)

    file_content_lines.forEach(file_content_line => {
        let card = [
            `<div class="card">`,
                `<span class="card-header">Group</span>`,
            `<div class="card-body">`,
                `<ul>`,
        ]
        file_content_line.split(',').forEach(sample => {
            card.push(`<li>${sample}</li>`)
        })
        card.push(
            [
                        `</ul>`,
                    `</div>`,
                `</div>`,
            ].join('')
        )
        cards.push(card.join(''))
    })
    console.log(cards)
}