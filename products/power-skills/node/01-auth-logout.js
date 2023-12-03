const axios = require('axios');

axios
  .get('https://api-power-skills.neuroquest.ai/api/v1/auth/logout', {
     headers: { token:   process.env.NQ_TOKEN},
	 params: { email: process.env.NQ_USER },
  })
  .then((response) => {
    console.log(JSON.stringify(response.data, null, 2));
  })
  .catch((err) => console.log(err));

