import axios from 'axios'

export async function translateWithDeepl(text) {
  const res = await axios.post(
    'https://api-free.deepl.com/v2/translate',
    new URLSearchParams({
      auth_key: import.meta.env.VITE_DEEPL_API_KEY,
      text: text,
      target_lang: 'JA',
    }),
    {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
    },
  )

  return res.data.translations[0].text
}
