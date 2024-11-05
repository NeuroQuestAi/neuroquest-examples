const axios = require('axios');

axios
  .get('https://api-persona-predict.neuroquest.ai/api/v2/auth/logout', {
     headers: {token: process.env.NQ_TOKEN},
     params: {email: process.env.NQ_EMAIL},
  })
  .then((response) => {
    console.log(JSON.stringify(response.data, null, 2));
  })
  .catch((err) => console.log(err));

