var dirInput = document.body.querySelector('input[type="file"]');
dirInput.addEventListener('change', function(e){
    var imageContainer = document.body.querySelector('#imageContainer');
    for (const f of this.files){
        var reader = new FileReader();
        reader.onload = function (e) {
            renderDrawing(e);
        }
        reader.readAsDataURL(f);
    }
    getGroupOptions();
});

function renderDrawing(e){
    var drawingEl = makeDrawingInput(e.target.result, f);
    imageContainer.append(drawingEl);
}

function makeDrawingInput(fileData, fileObj){
    var drawingContainer = document.createElement('div');
    drawingContainer.classList.add('row');
    drawingContainer.classList.add('drawing');
    drawingContainer.id = fileObj.name;

    var imgContainer = document.createElement('div');
    imgContainer.classList.add('col-lg-4');
    // imgContainer.classList.add('col-sm-6');

    var drawing = document.createElement('img');
    drawing.setAttribute('src', fileData);

    imgContainer.append(drawing);
    drawingContainer.append(imgContainer);

    return drawingContainer;
}

$('#notebook-create-form').on('submit', function(evt){
    debugger;
});

function getGroupOptions(){
    $.get('/groups/all?format=json', function(data){
        var groups = JSON.parse(data.data);
        var drawings = $('.drawing');

        // make a checkbox for every group, for every drawing.
        // so that any particular drawing can be labelled as a particular group.
        drawings.each(function(i){
            var metaDataContainer = document.createElement('div');
            metaDataContainer.classList.add('col-lg-3');
            // metaDataContainer.classList.add('col-sm-6');

            metaDataContainer.classList.add('group-checkbox');
            metaDataContainer.id=this.id;
            for (const g of groups){
                var label = document.createElement('label');
                label.textContent = " " + g.pk;
                label.append(document.createElement('br'));
                var checkbox = document.createElement('input');
                checkbox.setAttribute('type', 'checkbox');
                checkbox.setAttribute('value', g.pk);
                metaDataContainer.append(checkbox);
                metaDataContainer.append(label);
            }
            this.append(metaDataContainer);
        });

    });
}
console.log('groups showing up :0');