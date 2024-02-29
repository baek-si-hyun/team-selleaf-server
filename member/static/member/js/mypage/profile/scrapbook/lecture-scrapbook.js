// 마이페이지/프로필/스크랩북 js 파일

// 공유 버튼 눌렀을 때 모달창 표시

// 필요한 객체 가져오기
const shareModal = document.querySelector(".share-modal-wrap");

// 모달창 내 클립보드 버튼도 가져옴 - alert 표시용
const clipboardButton = document.querySelector(".cilpboard-button");

// 클립보드 버튼 - click 이벤트
// 클릭하면 alert 창 표시
clipboardButton.addEventListener("click", () => {
  alert("클립보드에 복사되었습니다.");
});

// click 이벤트 - 모달창 닫기
// 모달창 이외 아무 곳이나 클릭하면 모달창 닫힘
document.addEventListener("click", (e) => {
  // 만약 클릭한 곳의 상위 요소가 모달이 아닐 경우 = 모달 이외의 장소를 클릭한 경우
  if (!e.target.closest(".share-modal-wrap")) {
    // 상위 요소가 공유 버튼인 요소를 클릭했다면
    if (e.target.closest(".share-button")) {
      // 모달창을 enabled 상태로 만들어줌
      shareModal.classList.toggle("enabled");

      // 아래쪽 실행 안 하고 함수 종료
      return;
    }
    // 모달창, 버튼 이외의 장소를 클릭한 경우 모달창 enabled 해제
    shareModal.classList.remove("enabled");
  }
  // 상위 요소가 모달일 경우(모달 클릭한 경우) 아무 것도 실행 안함(상태 유지)
});

// 화면 우하단에 있는 화살표 버튼 - click 이벤트
// 클릭 시, 화면 최상단으로 스무스하게 스크롤 이동
// 필요한 객체 가져오기
const topButton = document.querySelector(".top-button-wrap");

// 클릭 이벤트 추가
topButton.addEventListener("click", () => {
  window.scrollTo({
    top: 0,
    left: 0,
    behavior: "smooth",
  });
});

// 페이지가 어느 정도 스크롤이 되었을 때만 최상단 이동 버튼이 뜨게 하기
// header 높이보다 많이(80.75px) 스크롤 했을 때 버튼 표시
// 필요한 객체 가져오기
const headerHeight = parseFloat(document.querySelector("header").style.height); // header의 높이

window.addEventListener("scroll", () => {
  // window.scrollY(아래로 스크롤 한 정도)가 header의 높이보다 커지면 버튼 표시
  if (window.scrollY > headerHeight) {
    // 만약 현재 버튼이 숨겨진(display: none) 상태라면
    if (topButton.style.display == "none") {
      // display를 block으로 바꿔서 보이게 함
      topButton.style.display = "block";
    }
    // display가 none이 아니라면 그대로 둠
    return;
  }
  // 만약 스크롤 정도가 header의 높이보다 작다면
  // 현재 보이는(display: block) 상태인지 체크
  if (topButton.style.display == "block") {
    // display를 none으로 바꿔서 다시 안 보이게 함
    topButton.style.display = "none";
  }
});

// 편집 버튼 눌렀을 때
// 현재 스크랩한 게시물 수와  삭제, 취소 버튼을 보이게하고
// 편집 버튼과 카테고리 메뉴는 안 보이게(display: none) 하는 이벤트
// 2/15 추가 - 편집 버튼 누르면 삭제 체크박스 표시

// 필요한 객체 가져오기
// 편집 버튼 클릭하면 숨겨지는 요소
const editButton = document.querySelector(".edit-button");
const categoryFilter = document.querySelector(".category-filter-wrap");

// 편집 버튼 클릭하면 보이게 되는 요소들
const contentCount = document.querySelector(".content-count-container");
const editButtonGroup = document.querySelectorAll(".edit-menu-button");
const deleteBoxes = document.querySelectorAll(".delete-box-wrap");

// 편집 버튼 - click 이벤트
editButton.addEventListener("click", (e) => {
  // 스크랩한 게시물 수 표시
  contentCount.style.display = "block";

  //  삭제, 취소 버튼도 표시
  // 한 번에 다 가져왔으니 forEach로 순회
  editButtonGroup.forEach((button) => {
    button.style.display = "inline-block";
  });

  // 2/15 추가 - 각 거래의 삭제 체크박스 표시
  deleteBoxes.forEach((box) => {
    box.style.display = "block";
  });

  // 기존 편집 버튼과 카테고리 리스트 숨김
  e.target.style.display = "none";
  categoryFilter.style.display = "none";
});

// 취소 버튼 눌렀을 때 다시 편집 버튼과 카테고리 메뉴를 보이게 하는 이벤트
// 2/15 추가 - 취소 버튼 누르면 삭제 체크박스 숨김 + 체크된 모든 박스의 체크 초기화

// 취소 버튼 객체 가져옴
const cancelButton = document.querySelector(".edit-menu-button:last-child");

// 취소 버튼 - click 이벤트
cancelButton.addEventListener("click", () => {
  // 스크랩한 게시물 수 숨김
  contentCount.style.display = "none";

  //  삭제, 취소 버튼도 숨김
  editButtonGroup.forEach((button) => {
    button.style.display = "none";
  });

  // 2/15 추가 - 각 거래의 삭제 체크박스 숨김
  deleteBoxes.forEach((box) => {
    box.style.display = "none";
  });

  // 편집 버튼 표시
  editButton.style.display = "inline-block";
  categoryFilter.style.display = "block";
});

/*
  카테고리 버튼(category-filter-wrap) 클릭하면 대카테고리 모달창 표시
  카테고리 버튼 or 다른 곳 클릭하면 다시 안 보이게 변경
*/

// 필요한 객체 가져오기 - 대카테고리 모달창
const categoryModal = document.querySelector(".first-category-modal-wrap");

// 각 이미지 별 a 태그
const postLinks = document.querySelectorAll(".post-link");

// click 이벤트 - 대카테고리 모달창 표시/숨김
// 버튼 or 모달창 이외의 장소에 클릭하면 모달창 닫힘
document.addEventListener("click", (e) => {
  // 만약 대카테고리 모달창 이외의 장소를 클릭한 경우
  if (!e.target.closest(".first-category-modal-wrap")) {
    // 카테고리 버튼을 클릭했다면
    if (e.target.closest(".category-filter-wrap")) {
      // 대카테고리 모달창에 enabled 클래스 추가함으로서 표시
      // 카테고리 버튼 한 번 더 누르면 닫힘
      categoryModal.style.display =
        categoryModal.style.display == "none" ? "block" : "none";

      // 2/19 추가 - 게시물 이미지 z-index 조정
      postLinks.forEach((post) => {
        post.style.zIndex = -1;
      });

      // 아래쪽 실행 안 하고 함수 종료
      return;
    }
    // 대카테고리 모달창, 카테고리 버튼 이외의 장소를 클릭한 경우 대카테고리 모달창 숨김
    categoryModal.style.display = "none";

    // 이미지 z-index 원복
    postLinks.forEach((post) => {
      post.style.zIndex = 1;
    });
  }
  // 대카테고리 모달창 클릭한 경우 아무 것도 실행 안함(상태 유지)
});

/*
  스크랩 한 강의 유무에 따라 표시되는 내용 변경

  강의 있음: post-wrap - flex, no-content-wrap - none
  강의 없음: post-wrap - none, no-content-wrap - block
*/

// 조건에 따라 표시할 div 태그들
const postWrap = document.querySelector(".post-wrap");
const noContentWrap = document.querySelector(".no-content-wrap");

// 스크랩 한 강의 개수
let classPosts = document.querySelectorAll(".post-wrap .post-container");

// 강의 없으면 내용 없음 표시
if (classPosts.length == 0) {
  postWrap.style.display = "none";
  noContentWrap.style.display = "block";
}
// 강의가 하나라도 있으면 강의 게시물 표시
else {
  postWrap.style.display = "flex";
  noContentWrap.style.display = "none";
}

// 현재 강의 개수를 페이지 상단 메뉴, 편집 눌렀을 때 나오는 전체 개시물 개수에 표시
const lectureCount = document.querySelector(".lecture");

// 현재 체크된 박스 개수와 전체 게시물 개수를 표시할 태그
const checkedCount = document.querySelector(".content-count-container");

// 상기한 부분에 현재 게시물 수 표시
lectureCount.innerText = `강의(${classPosts.length})`;

// 현재 체크된 박스 개수를 실제 화면에 표시 (innerText)
checkedCount.innerHTML = `<i>0</i> / ${classPosts.length}`;

/*
  2/15 추가 - 삭제 체크박스(delete-box-input) click하면 체크

  delete-box-container(부모)와 visual-box-wrap(형제)에
  enabled 클래스를 부여함으로서 표시함

  + 만약 클릭 시점에서 체크된 input이 하나 이상이라면  삭제 버튼 활성화
  + 현재 체크된 박스 개수를 화면에 표시(.content-count-container > i)
*/

// 각 삭제 체크박스의 input을 전부 가져옴
const deleteInputs = document.querySelectorAll(".delete-box-input");

// 취소 버튼 옆  삭제 버튼
const deleteButton = document.querySelector(".content-delete");

// 각 삭제 체크박스에 click 이벤트 부여
deleteInputs.forEach((input) => {
  input.addEventListener("click", (e) => {
    // 각 체크박스의 부모와 형제 요소
    const boxContainer = e.target.closest(".delete-box-container");
    const visualBox = e.target.previousElementSibling;

    // 클릭으로 체크박스가 체크된 경우, 위 요소들에 enabled 클래스 추가
    if (e.target.checked) {
      // 추가 전에, 기존에 enabled 클래스가 있었는지 검사
      if (!boxContainer.classList.contains("enabled")) {
        boxContainer.classList.add("enabled");
      }

      if (!visualBox.classList.contains("enabled")) {
        visualBox.classList.add("enabled");
      }
    }
    // 클릭으로 체크가 해제된 경우, enabled 클래스 삭제
    else {
      boxContainer.classList.remove("enabled");
      visualBox.classList.remove("enabled");
    }

    // 체크된 박스 전부를 가져옴
    const checkedBoxes = document.querySelectorAll(".delete-box-input:checked");

    // 만약 체크된 박스가 없다면 삭제 버튼 비활성화, 있으면 활성화
    if (checkedBoxes.length >= 1) {
      deleteButton.disabled = false;
    } else {
      deleteButton.disabled = true;
    }

    // 현재 체크된 박스 개수를 실제 화면에 표시 (innerHTML)
    checkedCount.innerHTML = `<i>${checkedBoxes.length}</i> / ${classPosts.length}`;
  });
});
