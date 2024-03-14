// 페이지가 열릴 때 체크된 박스가 없다면 삭제 버튼 disabled
const deleteBtn = document.querySelector(".delete-button");

// 현재 체크된 박스의 개수를 세는 함수
const countCheckBoxes = () => {
  // 각 체크박스의 상태가 변할 때마다 체크된 박스의 개수를 셈
  const checkedBoxes = document.querySelectorAll("input[type='checkbox']:checked")

  // 체크된 박스가 하나라도 있다고 가정하고 삭제 버튼의 disabled 해제
  deleteBtn.disabled = false;

  // 체크된 박스가 하나도 없다면 삭제 버튼 비활성화, 전체 선택 체크 해제
  if (checkedBoxes.length === 0) {
    deleteBtn.disabled = true;
  }
}

// 페이지가 열렸을 때 체크된 박스 개수를 셈
countCheckBoxes();

// 화면에 게시물 목록을 뿌리기 위한 로직
// 커뮤니티, 노하우, 거래는 각기 다른 페이지 사용
let postPage = 1;
let knowhowPage = 1;
let tradePage = 1;

// 리스트를 표시할 ul 태그
const ul = document.querySelector("ul.list-content");

// 게시물 숫자를 표시할 span 태그
const postCountTag = document.querySelector(".all-num");

// 카테고리 선택 버튼
const order1 = document.querySelector(".order-1");

// 커뮤니티 게시글 세서 화면에 적용하는 기능을 함수화
const countPosts = async () => {
  postCount = await postService.countPosts();
  postCountTag.innerText = postCount;
}

// 노하우 게시글 세서 화면에 적용하는 기능을 함수화
const countKnowhows = async () => {
  knowhowCount = await postService.countKnowhows();
  postCountTag.innerText = knowhowCount;
}

// 거래 게시글 세서 화면에 적용하는 기능을 함수화
const countTrades = async () => {
  tradeCount = await postService.countTrades();
  postCountTag.innerText = tradeCount;
}

// 커뮤니티 게시물 정보의 첫 페이지를 화면에 띄워주는 함수
const callFirstPostsList = () => {
  // 만들어둔 모듈을 사용해서 정보를 불러옴
  postService.getPostsList(postPage, showPosts).then((posts) => {
    ul.innerHTML = posts;

    // 게시물 숫자 변경
    countPosts();

    // 체크박스 클릭 이벤트 추가
    addCheckBoxEvent();
  });
}

// 노하우 게시물 정보의 첫 페이지를 화면에 띄워주는 함수
const callFirstKnowhowsList = () => {
  // 만들어둔 모듈을 사용해서 정보를 불러옴
  postService.getKnowhowList(knowhowPage, showKnowhows).then((posts) => {
    ul.innerHTML = posts;

    // 게시물 숫자 변경
    countKnowhows();

    // 체크박스 클릭 이벤트 추가
    addCheckBoxEvent();
  });
}

// 노하우 게시물 정보의 첫 페이지를 화면에 띄워주는 함수
const callFirstTradesList = () => {
  // 만들어둔 모듈을 사용해서 정보를 불러옴
  postService.getTradeList(tradePage, showTrades).then((posts) => {
    ul.innerHTML = posts;

    // 게시물 숫자 변경
    countTrades();

    // 체크박스 클릭 이벤트 추가
    addCheckBoxEvent();
  });
}

// 페이지 열렸을 때 커뮤니티 게시글 표시
callFirstPostsList();

// 삭제 버튼 누르면 뜨는 모달창
document.addEventListener("DOMContentLoaded", function () {
  const deleteButtons = document.querySelectorAll(".delete-button");
  const modalWrap = document.querySelector(".delete-modal-wrap");

  deleteButtons.forEach(function (deleteButton) {
    deleteButton.addEventListener("click", () => {
      modalWrap.style.display = "flex";
    });
  });

  const cancelButton = document.querySelector(".modal-cancel button");
  const confirmButton = document.querySelector(".modal-confirm button");

  cancelButton.addEventListener("click", () => {
    modalWrap.style.display = "none";
  });

  // 삭제 버튼 클릭 시, 체크된 게시물만 삭제
  confirmButton.addEventListener("click", async () => {
    modalWrap.style.display = "none";

    // 삭제 후 체크 해제할 전체 선택 체크박스
    const allCheck = document.querySelector(".all-check");

    // 삭제할 게시물의 id를 담을 빈 문자열
    let deleteIds = ``;

    // 이 시점에서 체크된 박스 개수를 세고
    const checkedBoxes = document.querySelectorAll(".checkbox-input:checked");

    // 각 체크박스를 감싸는 li 태그의 id를 deleteIds에 추가
    // 사이사이에 콤마를 붙여서 뷰에서 .split을 쓸 수 있게 만들어줌
    checkedBoxes.forEach((checkbox) => {
      deleteIds += `,${checkbox.parentElement.classList[1]}`;
    });

    // 현재 필터 검사하고, 서로 다른 뷰에 삭제 요청 후 해당 유형의 게시물 목록의 첫 페이지를 다시 불러옴
    // 커뮤니티 게시물 삭제 시
    if (order1.innerText === "커뮤니티") {
      await postService.deletePosts(deleteIds);
      callFirstPostsList();
    }
    // 노하우 게시물 삭제 시
    else if (order1.innerText === "노하우") {
      await postService.deleteKnowhows(deleteIds);
      callFirstKnowhowsList();
    }
    // 거래 게시물 삭제 시
    else if (order1.innerText === "거래") {
      await postService.deleteTrades(deleteIds);
      callFirstTradesList();
    }

    // 전체 선택 체크박스와 삭제 버튼 초기화
    allCheck.checked = false;
    deleteBtn.disabled = true;
  });
});

//아래 게시물 창 버튼
const paginationBtn = document.querySelectorAll(".page-count-num");
const paginationBox = document.querySelector(".page");

paginationBox.addEventListener("click", (e) => {
  let pageBtn = e.target.closest("button.page-count-num");
  if (pageBtn) {
    paginationBtn.forEach((item) => {
      item.classList.contains("page-count-num") &&
        item.classList.remove("page-count-num-choice");
    });
    pageBtn.classList.add("page-count-num-choice");
  }
});

// 카테고리 선택 모달
const modalButton = document.querySelector("button.list-order");
const modal = document.querySelector(".list-order-function");
const modalUl = document.querySelector("ul.list-order-function");
const modalSvg = document.querySelector("svg.list-order");

document.addEventListener("click", (e) => {
  // 카테고리 버튼 클릭 시 모달창 열림
  if (e.target.closest("button.list-order")) {
    modal.style.display = "block";
    modalSvg.style.transform = "rotate(180deg)";
    modalButton.classList.add("border-color");
  }
  // 모달창 내부를 클릭했을 때 모달창 표시 유지
  else {
    if (e.target.classList.contains("list-order-function")) {
      modal.style.display = "block";
      return;
    }
    //화면의 나머지 부분을 클릭하면 모달창 닫힘
    modal.style.display = "none";
    modalSvg.style.transform = "rotate(360deg)";
    modalButton.classList.remove("border-color");
  }
});

// 모달창 내 게시물 선택
const modalBtns = modal.querySelectorAll("button.function-latest");

modalBtns.forEach((modalBtn) => {
  modalBtn.addEventListener("click", (e) => {
    // 전체 선택 체크박스와 삭제 버튼
    const allCheck = document.querySelector(".all-check");

    // 버튼 클릭 시 해당 버튼 안 텍스트를 유형 선택 버튼에도 똑같이 적용
    const btn = e.target.closest("button");
    const categoryText = btn.innerText;

    order1.innerText = categoryText;

    // 선택에 따라 다른 API에 데이터 요청해서 리스트 변경 - 첫 페이지 표시
    categoryText === "커뮤니티"
        ? callFirstPostsList()
        : categoryText === "노하우"
        ? callFirstKnowhowsList()
        : categoryText === "거래"
        ? callFirstTradesList() : false;

    // 전체 선택 버튼과 삭제 버튼 초기화
    deleteBtn.disabled = true;
    allCheck.checked = false;
  });
});

// 검색창 눌렀을때 검색바에 아웃라인주기
const searchBar = document.querySelector("label.search-bar");

document.addEventListener("click", (e) => {
  if (e.target.closest("label.search-bar")) {
    searchBar.classList.add("search-bar-checked");
    return;
  }
  searchBar.classList.remove("search-bar-checked");
});

const inputField = document.querySelector(".search-bar input");
const cancelButton = document.querySelector(".search-bar .cancel-logo");
const searchButton = document.querySelector(".search-bar .search-logo");

// 입력 필드에 입력 내용이 변경될 때마다 실행될 함수를 정의합니다.
function handleInputChange() {
  const inputValue = inputField.value.trim(); // 입력 내용을 가져옵니다.

  // 입력 내용이 있을 때
  if (inputValue !== "") {
    cancelButton.style.display = "flex"; // cancel-logo를 보여줍니다.
    searchButton.style.display = "none"; // search-logo를 숨깁니다.
  } else {
    // 입력 내용이 없을 때
    cancelButton.style.display = "none"; // cancel-logo를 숨깁니다.
    searchButton.style.display = "flex"; // search-logo를 보여줍니다.
  }
}

// cancel-logo를 클릭했을 때 실행될 함수를 정의합니다.
function handleCancelClick() {
  inputField.value = ""; // 입력 필드 내용을 지웁니다.
  cancelButton.style.display = "none"; // cancel-logo를 숨깁니다.
  searchButton.style.display = "flex"; // search-logo를 보여줍니다.
}

// 입력 필드에 이벤트 리스너를 추가합니다.
inputField.addEventListener("input", handleInputChange);

// cancel-logo에 클릭 이벤트 리스너를 추가합니다.
cancelButton.addEventListener("click", handleCancelClick);

const addCheckBoxEvent = () => {
  // 체크박스 관련 js
  const allCheck = document.querySelector(".all-check");
  const checkboxes = document.querySelectorAll(".checkbox-input");

  // all-check 체크 여부에 따라 checkbox-input 체크 여부 조절
  allCheck.addEventListener("change", function () {
    checkboxes.forEach(function (checkbox) {
      checkbox.checked = allCheck.checked;

      // 현재 체크된 박스 개수를 세서 삭제 버튼의 활성화 여부 조정
      countCheckBoxes();
    });
  });

  // checkbox-input 중 하나라도 체크가 해제되면 all-check 체크 해제
  checkboxes.forEach(function (checkbox) {
    checkbox.addEventListener("change", function () {
      let allChecked = true;
      checkboxes.forEach(function (checkbox) {
        if (!checkbox.checked) {
          allChecked = false;
        }
      });
      allCheck.checked = allChecked;
    });
  });

  // checkbox-input 모두 체크되면 all-check 체크
  checkboxes.forEach(function (checkbox) {
    checkbox.addEventListener("change", function () {
      let allChecked = true;
      checkboxes.forEach(function (checkbox) {
        if (!checkbox.checked) {
          allChecked = false;
        }
      });
      allCheck.checked = allChecked;
    });
  });

  // 체크박스의 체크 상태가 변할 때마다 체크된 박스 개수를 셈
  checkboxes.forEach((checkbox) => {
    checkbox.addEventListener("change", countCheckBoxes);
  });
}
