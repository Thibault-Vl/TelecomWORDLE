const sleepyTime = 400;

async function setCss(data, row) {
    for (let key in data) {
        const tempTdCoordinate = row * 5 + parseInt(key);
        const tempSound = new Audio("/Static/Sound/" + data[key] + ".wav")
        await tempSound.play()
        $( `td:eq( ${tempTdCoordinate} )` ).addClass(data[key]);
        await sleep(sleepyTime);
    }
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}