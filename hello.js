// www.weather.com/api
// location_latitude
// location_longitude

const fetch = require('express-fetch')

fetch('www.wether.com/api', {
    method: "post",
    body: 'a=1'
})
    .then(res => res.json())
    .then((json) => { 
        console.log(json)
    }).catch(err => console.log(err))
