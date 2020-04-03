$(document).ready(function() {
    $.ajax({
        type: "GET",
        url: "data/data.txt",
        dataType: "text",
        succes: function(data) {proccesData(data);}
    });
});

function proccesData(allData){
    var allDataLines = allData.split(/\r\n|\n/);
    var headers = allDataLines[0].split(',');
    var lines = [];

    for (var i=1; i<allDataLines.length; i++) {
        var data = allDataLines[i].split(',');
        if (data.length == headers.length) {

            var tarr = [];
            for (var j=0; j<headers.length; j++) {
                tarr.push(headers[j]+":"+data[j]);
            }
            lines.push(tarr);
        }
    }

}

// https://stackoverflow.com/questions/7431268/how-to-read-data-from-csv-file-using-javascript