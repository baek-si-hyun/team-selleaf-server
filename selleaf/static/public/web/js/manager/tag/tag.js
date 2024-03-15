let page = 1
let keyword = ''

// 받아온 댓글들의 정보를 뿌려주는 함수
const allNum = document.querySelector(".all-num")
const listContent = document.querySelector(".list-content")
const pageCountWrap = document.querySelector(".page-count-wrap")

const createHTML = (() => {
    const showList = async (tags) => {
        let text = ``;
        console.log(tags)
        // let pageInfo = replies.pop()
        // allNum.innerText = pageInfo.totalCount

        // if (replies.length === 0){
        //     text += `
        //         <div class="nothing">
        //             <img src="/static/public/web/images/manager/nothing.png" class="nothing"/>
        //             <p class="nothing">해당 내역이 없습니다.</p>
        //         </div>
        //     `
        // } else{
        //     for (let reply of replies){
        //         text += `
        //             <li class="list-content">
        //                 <input name="reply-member-id" type="hidden" value="${reply.reply_member_id}">
        //                 <input name="reply-created" type="hidden" value="${reply.reply_created}">
        //                 <input name="reply_id" type="hidden" value="${reply.reply_id}">
        //                 <input name="target" type="checkbox" class="checkbox-input" />
        //                 <div class="reply-writer">
        //                     <p class="writer-name">${reply.reply_member_name}</p>
        //                 </div>
        //                 <div class="target-type">
        //                     <p class="type-name">${reply.target_type}</p>
        //                 </div>
        //                 <div class="target-title">
        //                     <div class="list-title-wrap">
        //                         <div class="list-title-container">
        //                             <div class="list-title-inner">
        //                                 <div class="title-name">
        //                                     <p class="title-name">${reply.target_title}</p>
        //                                 </div>
        //                             </div>
        //                         </div>
        //                     </div>
        //                 </div>
        //                 <div class="reply-content">
        //                     <div class="list-content-wrap">
        //                         <div class="list-content-container">
        //                             <div class="list-content-inner">
        //                                 <div class="content-name">
        //                                     <p class="content-name">${reply.reply_content}</p>
        //                                 </div>
        //                             </div>
        //                         </div>
        //                     </div>
        //                 </div>
        //                 <div class="created-date">
        //                     <p class="created-date-num">${reply.reply_created.slice(0,4)}.${reply.reply_created.slice(5,7)}.${reply.reply_created.slice(8,10)}</p>
        //                 </div>
        //             </li>
        //         `
        //     }
        // }
        // listContent.innerHTML = text;
        // showPagination(pageInfo)
        // checkboxEvent()
    }

    // 전달받은 페이지 관련 정보를 통해 페이지네이션 버튼을 만들어주는 함수
    const showPagination = (pageInfo) => {
        const totalCount = pageInfo.totalCount;
        const startPage = pageInfo.startPage;
        const endPage = pageInfo.endPage;
        const currentPage = pageInfo.page;
        const realEnd = pageInfo.realEnd;
        let text = ``;
        if (totalCount === 0) {
            text = ``;
        } else{
            if (currentPage !== 1) {
                text = `
                    <button class="page-count-prev" aria-label="page turning button" type="button">
                        <svg class="page-count" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd" clip-rule="evenodd" d="M15.58 3.27c.504.405.563 1.115.13 1.587L9.168 12l6.543 7.143a1.076 1.076 0 0 1-.13 1.586 1.26 1.26 0 0 1-1.695-.122L6 12l7.885-8.607a1.26 1.26 0 0 1 1.695-.122Z"></path>
                        </svg>
                    </button>
                `;
            }
            for (let i = startPage; i <= endPage; i++) {
                text += `
                    <button class="page-count-num ${currentPage === i ? 'page-count-num-choice' : ''}" aria-label="page number button" type="button">
                        <span class="page-count-num">${i}</span>
                    </button>
            `
            }
            if (currentPage !== realEnd) {
                text += `
                    <button class="page-count-next" aria-label="page turning button" type="button">
                        <svg class="page-count" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd" clip-rule="evenodd" d="M8.42 20.73a1.076 1.076 0 0 1-.13-1.587L14.832 12 8.289 4.857a1.076 1.076 0 0 1 .13-1.586 1.26 1.26 0 0 1 1.696.122L18 12l-7.885 8.607a1.26 1.26 0 0 1-1.695.122Z"></path>
                        </svg>
                    </button>
                `;
            }
        }
        pageCountWrap.innerHTML = text
        if (text !== ``) {
            addPaginationEvent(pageInfo)
        }
    }

    return {showList: showList}
})()

manageTag.getTags(keyword, page, createHTML.showList)

// // 삭제 버튼 누르면 뜨는 모달창
// document.addEventListener("DOMContentLoaded", function () {
//   const deleteButtons = document.querySelectorAll(".delete-button");
//   const modalWrap = document.querySelector(".delete-modal-wrap");
//
//   console.log(deleteButtons);
//
//   deleteButtons.forEach(function (deleteButton) {
//     deleteButton.addEventListener("click", (e) => {
//       modalWrap.style.display = "flex";
//     });
//   });
//
//   const cancelButton = document.querySelector(".modal-cancel button");
//   const confirmButton = document.querySelector(".modal-confirm button");
//
//   cancelButton.addEventListener("click", (e) => {
//     modalWrap.style.display = "none";
//   });
//
//   confirmButton.addEventListener("click", (e) => {
//     modalWrap.style.display = "none";
//   });
// });
//
// //아래 게시물 창 버튼
// const paginationBtn = document.querySelectorAll(".page-count-num");
// const paginationBox = document.querySelector(".page");
//
// paginationBox.addEventListener("click", (e) => {
//   let pageBtn = e.target.closest("button.page-count-num");
//   if (pageBtn) {
//     paginationBtn.forEach((item) => {
//       item.classList.contains("page-count-num") &&
//         item.classList.remove("page-count-num-choice");
//     });
//     pageBtn.classList.add("page-count-num-choice");
//   }
// });
//
// // 검색창 눌렀을때 검색바에 아웃라인주기
// const searchBar = document.querySelector("label.search-bar");
//
// document.addEventListener("click", (e) => {
//   if (e.target.closest("label.search-bar")) {
//     searchBar.classList.add("search-bar-checked");
//     return;
//   }
//   searchBar.classList.remove("search-bar-checked");
// });
//
// const inputField = document.querySelector(".search-bar input");
// const cancelButton = document.querySelector(".search-bar .cancel-logo");
// const searchButton = document.querySelector(".search-bar .search-logo");
//
// // 입력 필드에 입력 내용이 변경될 때마다 실행될 함수를 정의합니다.
// function handleInputChange() {
//   const inputValue = inputField.value.trim(); // 입력 내용을 가져옵니다.
//
//   // 입력 내용이 있을 때
//   if (inputValue !== "") {
//     cancelButton.style.display = "flex"; // cancel-logo를 보여줍니다.
//     searchButton.style.display = "none"; // search-logo를 숨깁니다.
//   } else {
//     // 입력 내용이 없을 때
//     cancelButton.style.display = "none"; // cancel-logo를 숨깁니다.
//     searchButton.style.display = "flex"; // search-logo를 보여줍니다.
//   }
// }
//
// // cancel-logo를 클릭했을 때 실행될 함수를 정의합니다.
// function handleCancelClick() {
//   inputField.value = ""; // 입력 필드 내용을 지웁니다.
//   cancelButton.style.display = "none"; // cancel-logo를 숨깁니다.
//   searchButton.style.display = "flex"; // search-logo를 보여줍니다.
// }
//
// // 입력 필드에 이벤트 리스너를 추가합니다.
// inputField.addEventListener("input", handleInputChange);
//
// // cancel-logo에 클릭 이벤트 리스너를 추가합니다.
// cancelButton.addEventListener("click", handleCancelClick);
//
// // 체크박스 js
// const allCheck = document.querySelector(".all-check");
// const checkboxes = document.querySelectorAll(".checkbox-input");
//
// // all-check 체크 여부에 따라 checkbox-input 체크 여부 조절
// allCheck.addEventListener("change", function () {
//   checkboxes.forEach(function (checkbox) {
//     checkbox.checked = allCheck.checked;
//   });
// });
//
// // checkbox-input 중 하나라도 체크가 해제되면 all-check 체크 해제
// checkboxes.forEach(function (checkbox) {
//   checkbox.addEventListener("change", function () {
//     let allChecked = true;
//     checkboxes.forEach(function (checkbox) {
//       if (!checkbox.checked) {
//         allChecked = false;
//       }
//     });
//     allCheck.checked = allChecked;
//   });
// });
//
// // checkbox-input 모두 체크되면 all-check 체크
// checkboxes.forEach(function (checkbox) {
//   checkbox.addEventListener("change", function () {
//     let allChecked = true;
//     checkboxes.forEach(function (checkbox) {
//       if (!checkbox.checked) {
//         allChecked = false;
//       }
//     });
//     allCheck.checked = allChecked;
//   });
// });
