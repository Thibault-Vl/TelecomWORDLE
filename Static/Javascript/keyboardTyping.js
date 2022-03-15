// Init base url value
const getUrl = window.location;
const baseUrl = getUrl .protocol + "//" + getUrl.host;
const queryString = window.location.search;

// Handle parameters
const urlParams = new URLSearchParams(queryString);
const wordLenght = parseInt(urlParams.get("wordlength"));

// Init usefully values
const alphabet = "azertyuiopqsdfghjklmwxcvbn";
let row = 0;
let column = 1;
let word = new Array(wordLenght);
const grid = document.getElementById("grid");
const firstLetter = $( "td:eq(0)" ).html()

// Init first letter of the word
word[0] = firstLetter.toLowerCase();

document.addEventListener("keydown", (ev) => {
    if (alphabet.includes(ev.key)) {
        if (column < wordLenght) {
            const tempTdCoordinate = row * wordLenght + column;
            $( `td:eq( ${tempTdCoordinate} )` ).html(ev.key.toUpperCase());
            word[column] = ev.key;
            column += 1;
        }
    } else if (ev.code === "Backspace") {
         if (column === 1) {
            const tempTdCoordinate = row * wordLenght + column;
            $( `td:eq( ${tempTdCoordinate} )` ).html(".");
            word[column] = "";
        } else {
            column -= 1;
            const tempTdCoordinate = row * wordLenght + column;
            $( `td:eq( ${tempTdCoordinate} )` ).html(".");
            word[column] = "";
        }
    } else if (ev.code === "Enter") {
        if (column === wordLenght && row < 5) {
            let tempWord = word.join("");
            $.ajax({
                type: "POST",
                url: baseUrl + "/tosmu",
                data: {"word": tempWord, "try": row + 1},
                success: async function (result) {
                    await setCss(result['css'], row)
                    if (result['statement']) {
                        // Reset word value to prepare for next try
                        word = new Array(wordLenght);
                        word[0] = firstLetter;
                        row += 1;
                        column = 1;
                        initRow(row);
                    }

                    if (result['winStatement']) {
                        confettiFalling();
                    }
                }
              });
        }
    }
})

function initRow(row) {
    $( `td:eq( ${row * wordLenght} )` ).html(firstLetter);

    for (let i = 1; i < wordLenght; i++) {
        const tempTdCoordinate = row * wordLenght + i;
        $( `td:eq( ${tempTdCoordinate} )` ).html(".");
    }
}