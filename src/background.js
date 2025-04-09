// 初期化時に `chrome.storage` から `dakenCount` を取得（なければ 0 にする）
chrome.runtime.onInstalled.addListener(() => {
  chrome.storage.local.get(['dakenCount'], (result) => {
    if (result.dakenCount === undefined) {
      chrome.storage.local.set({ dakenCount: 0 })
    }
  })
})

// `content.js` からメッセージを受け取って `dakenCount` を更新
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === 'KEY_PRESS') {
    chrome.storage.local.get(['dakenCount'], (result) => {
      let count = result.dakenCount || 0
      count++
      chrome.storage.local.set({ dakenCount: count }, () => {
        console.log('更新された打鍵数:', count)
        sendResponse({ status: 'ok', dakenCount: count })
      })
    })
    return true // `sendResponse()` を非同期で使うため `true` を返す
  }
})
