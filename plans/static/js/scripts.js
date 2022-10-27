let dm;
if (localStorage.getItem("darkmode") == "true") {
    dm = true;
} else {
    dm = false;
}

let list = ['Herbstferien', 'Weihnachtsferien', 'Winterferien', 'Osterferien', 'Pfingstferien']
list.forEach(element => {
    nodelists = document.getElementsByName(element);
    let i = 0;
    nodelists.forEach(nodelist => {
        parent = nodelist.parentElement;
        parent.classList.add("bg-green");
        parent.classList.add("text-white");
    })
});

rows = document.getElementsByTagName('tr');
function darkmode() {
    if (dm == true) {
        dm = false
    } else {
        dm = true
    }
    localStorage.removeItem("darkmode");
    localStorage.setItem("darkmode", dm);
    
    header = document.getElementById("header");
    footer = document.getElementById("footer");
    table = document.getElementById("table");
    body = document.getElementById("body");
    
    header.classList.toggle("bg-grey-800");
    footer.classList.toggle("bg-grey-800");
    body.classList.toggle("bg-grey-600");
    table.classList.toggle("text-white");
    let i = 1;
    for (let row of rows) {
        i++
        if (i % 2 === 0) {
            if (!row.classList.contains('bg-green')) {
                row.classList.toggle("bg-grey-500");
                table.classList.toggle("text-white");
            }
        }
    }
}

if (localStorage.getItem("darkmode") == "true") {
    header.classList.add("bg-grey-800");
    footer.classList.add("bg-grey-800");
    body.classList.add("bg-grey-600");
    table.classList.add("text-white");
    let i = 1;
    for (let row of rows) {
        i++
        if (i % 2 === 0) {
            if (!row.classList.contains('bg-green')) {
                row.classList.add("bg-grey-500");
                table.classList.add("text-white");
            }
        }
    }
} else {
    header.classList.remove("bg-grey-800");
    footer.classList.remove("bg-grey-800");
    body.classList.remove("bg-grey-600");
    table.classList.remove("text-white");
    let i = 1;
    for (let row of rows) {
        i++
        if (i % 2 === 0) {
            if (!row.classList.contains('bg-green')) {
                row.classList.remove("bg-grey-500");
                table.classList.remove("text-white");
            }
        }
    }
}