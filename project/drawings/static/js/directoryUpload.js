var dirInput = document.body.querySelector('input[type="file"]');
dirInput.addEventListener('change', function(e){
    var imageContainer = document.body.querySelector('#imageContainer');
    for (const f of this.files){
        var reader = new FileReader();
        reader.onload = function (e) {

        }
        reader.readAsDataURL(f);
    }
});

function makeDrawingInput(fileObj){
    var drawing = document.createElement('img');
    drawing.setAttribute('src', e.target.result);
    drawing.addClass('drawing');
    imageContainer.append(drawing);
    
}