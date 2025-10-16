function helloNalios() {
    const codes = [
        72, 101, 108, 108, 111, 44, 32, 78, 97, 108, 105, 111, 115, 32, 33
    ];
    let result = codes.map(c => String.fromCharCode(c)).join('');
    console.log(result);
}


helloNalios();