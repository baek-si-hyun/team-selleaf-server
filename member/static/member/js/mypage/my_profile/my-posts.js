// 마이페이지/프로필/사진 js 파일

// 사이드 바 내 공유 버튼 눌렀을 때 모달창 표시

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
    if (e.target.closest(".share-drop-down-button")) {
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

/*
  강사 여부에 따라 게시글 묶음 메뉴 표시/숨김
*/

// 강사 여부
let isTeacher = false;

// 게시글 묶음 객체
const myClassMenu = document.querySelector(".teacher");

// 강사면 게시글 묶음 메뉴 표시, 아니면 숨김
if (isTeacher) {
  myClassMenu.style.display = "inline-block";
} else {
  myClassMenu.style.display = "none";
}

/*
  게시글 유무에 따라 표시되는 내용 변경

  게시글 있음: post-wrap - flex, no-content-wrap - none
  게시글 없음: post-wrap - none, no-content-wrap - block
*/

// 조건에 따라 표시할 div 태그들
const postWrap = document.querySelector(".post-wrap");
const noContentWrap = document.querySelector(".no-content-wrap");

// 스크랩 한 게시글 개수
let posts = document.querySelectorAll(".post-wrap .post-container");

// 게시글 없으면 내용 없음 표시
if (posts.length == 0) {
  postWrap.style.display = "none";
  noContentWrap.style.display = "block";
}
// 게시글이 하나라도 있으면 게시글 묶음 표시
else {
  postWrap.style.display = "flex";
  noContentWrap.style.display = "none";
}
