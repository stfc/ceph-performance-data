const fs = require('fs')

fs.readdir('/static/data/', (err, files) => {
       files.forEach(file => {
              console.log(file);
       })
})

