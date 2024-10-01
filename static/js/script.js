// 搜尋按鈕 宣告變數
const searchButton = document.getElementById('search-button');
const searchInput = document.getElementById('search-input');

// 新增事件監聽器 被點擊時，就會觸發後面的函式
searchButton.addEventListener('click', () => { 
    // 事件處理函式 將原本隱藏的搜尋輸入框顯示出來
  searchInput.style.display = 'block';
  searchInput.focus();
});