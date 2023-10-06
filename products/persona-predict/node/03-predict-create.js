const axios = require('axios');

const data = {
  name: 'John Green',
  essay: "The CEO role required adaptability and a commitment to staying at the forefront of industry trends. As I reflect on my journey, I'm proud of the legacy I leave behind. It's not just about the financial success of the company but the positive impact we made on our employees, customers, and the communities we served. Leading with integrity and ethics remained at the core of our mission. In due time, I made the decision to pass on the torch to the next generation of leaders. Succession planning and grooming future CEOs became a priority. It was a bittersweet moment, but I knew it was time to embrace new challenges and opportunities. Becoming a CEO was the culmination of a lifelong journey marked by dedication, perseverance, and a commitment to excellence. My story serves as a testament to the idea that, with passion, education, and unwavering determination, anyone can rise to the highest levels of corporate leadership. The path may be challenging, but the rewards are immeasurable, not only in terms of professional achievement but also in the enduring impact one can make on the world.",
};

axios
  .post('https://api-persona-predict.neuroquest.ai/api/v1/predict/create', data, {
    headers: { token: process.env.NQ_TOKEN },
  })
  .then((response) => {
    console.log(JSON.stringify(response.data, null, 2));
  })
  .catch((err) => console.log(err));
