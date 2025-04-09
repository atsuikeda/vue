document.addEventListener('keydown', async () => {
  let result = await chrome.storage.local.get(['dakenCount'])
  console.log(result)
  let count = result.dakenCount || 0
  count++

  await chrome.storage.local.set({ dakenCount: count })

  console.log('キー押した！カウント:', count)
})
