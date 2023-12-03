const axios = require('axios');

axios
  .post('https://api-power-skills.neuroquest.ai/api/v1/auth/login', {
    email: process.env.NQ_USER,
    password: process.env.NQ_PASSWORD,
  })
  .then((response) => {
    console.log(JSON.stringify(response.data, null, 2));
  })
  .catch((err) => console.log(err));
