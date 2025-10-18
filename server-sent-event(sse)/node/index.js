const app = require('express')();

app.get('/', (req, res) => res.send("hello!"));

app.listen(8080)

console.log("listening no 8080")

