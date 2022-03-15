const sleepyTime = 400;

async function setCss(data, row) {
    let soundData = {
        "bad-place": new Howl({
          src: ["/Static/Sound/bad-place.wav"],
          volume: 1.0}),
        "good-place": new Howl({
          src: ["/Static/Sound/good-place.wav"],
          volume: 1.0}),
        "not-found": new Howl({
          src: ["/Static/Sound/not-found.wav"],
          volume: 1.0})
    };
    for (let key in data) {
        const tempTdCoordinate = row * wordLenght + parseInt(key);
        await soundData[data[key]].play();
        $( `td:eq( ${tempTdCoordinate} )` ).addClass(data[key]);
        await sleep(sleepyTime);
    }
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}