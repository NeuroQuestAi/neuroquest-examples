const axios = require('axios');

axios
  .post('https://api-persona-predict.neuroquest.ai/api/v2/auth/login', {
    email: process.env.NQ_EMAIL,
    password: process.env.NQ_PASSWORD,
  })
  .then((response) => {
    console.log(JSON.stringify(response.data, null, 2));
  })
  .catch((err) => console.log(err));
