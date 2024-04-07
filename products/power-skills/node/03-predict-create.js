const axios = require('axios');

const data = {
  name: "Gabriela Ehlert",
  essay: "My name is Gabriela, I am 28 years old, and I am constantly seeking progress in my career in sales. From an early age, I developed a passion for challenges and a natural ability to connect with people. With an entrepreneurial spirit, I entered the world of sales determined to reach new professional heights. My infectious enthusiasm and my ability to quickly understand the needs of clients set me apart in the competitive landscape. From the beginning, I devoted time and effort to enhance my communication and negotiation skills. I participated in courses, workshops, and events related to sales, always in search of practical knowledge that I could apply in my professional daily life. I don't settle for theory alone; I put my learnings into practice proactively. I set challenging goals for myself and implemented innovative strategies to achieve them. My commitment to personal and professional success has led me to build strong relationships with clients and colleagues. Throughout my journey, I faced challenges with resilience, turning obstacles into learning opportunities. My positive mindset and willingness to embrace challenges distinguish me as a promising professional in the field of sales. I don't limit myself to daily sales targets; I aim to build lasting relationships and provide personalized solutions to my clients. My commitment to excellence and professional ethics inspire my team members. As I advance in my career, my name becomes synonymous with success in the sales field. My story reflects not only my individual determination but also the transformative power that passion and commitment have in the professional world. I am ready for the challenges the future holds, confident that each obstacle is an opportunity for growth.",
};

axios
  .post('https://api-power-skills.neuroquest.ai/api/v1/predict/create/by-text', data, {
    headers: { token: process.env.NQ_TOKEN },
  })
  .then((response) => {
    console.log(JSON.stringify(response.data, null, 2));
  })
  .catch((err) => console.log(err));
