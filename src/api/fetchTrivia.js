import axios from 'axios'

export async function fetchTrivia() {
  const res = await axios.get('https://uselessfacts.jsph.pl/api/v2/facts/random?language=JA')
  return res.data.text
}
