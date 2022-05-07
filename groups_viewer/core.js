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


var getFileText = async (localFile) => new Promise((resolve, reject) => {
    let fileReader = new FileReader();
    fileReader.readAsText(localFile);
    fileReader.onerror = (err) => null;
    fileReader.onload = () => resolve(fileReader.result.split(/\r\n|\n/).filter(n => n != ''));
  })

var getCsvFile = async () => {

    const getFileExtension = (file) => { return file.split('.')[file.split('.').length - 1] }
  
    let file = document.getElementById('file')
    if (file.files.length > 0) {
      let local_file = file.files[0]
  
      let local_file_extension = getFileExtension(local_file.name)
      // Check if the file is a csv file
      if (local_file_extension.toLowerCase() === 'csv') {
        return await getFileText(local_file);
        
      } else {
        alert(`YOU SHOULD HAVE BEEN INFORMED A CSV FILE, NOT A ${local_file_extension.toUpperCase()} FILE!`)
      }
    } else {
      alert('YOU HAVE TO INFORM A CSV FILE!')
    }
  }

var createCard = async () => {

    var file_content_lines = await getCsvFile()
    if (file_content_lines){
        let cards = []

        const card_colors = hslGenerator(file_content_lines.length, 90, 60)

        file_content_lines.forEach((file_content_line, index) => {
            let card = [
                `<div class="card">`,
                    `<span class="card-header" style="background-color: ${card_colors[index]};">GRUPO ${index}</span>`,
                `<div class="card-body" style="border-color: ${card_colors[index]}";>`,
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
        return cards
    }else{
       alert('INVALID FILE!') 
    }
    
}

var insertCards = async () => {
    const cards_section = document.getElementById('cards-section')
    
    cards_section.innerHTML = [
        `<h1>Grupos</h1><br/><br/>`,
        `<div class="cards-content" id="cards-section-content"></div>`
    ].join('')

    const cards_section_content = document.getElementById('cards-section-content')

    const cards = await createCard()

    cards.forEach( card => {
        cards_section_content.innerHTML += card;
    })

}