// 공지사항 및 QnA 목록을 화면에 뿌리기 위한 로직
// 공지사항과 QnA의 페이지는 따로 설정
let noticePage = 1;
let qnaPage = 1;

// 공지사항, Q&A 버튼
const qnaButton = document.getElementById("Q&A");
const noticeButton = document.getElementById("notice");

// 공지사항 및 QnA을 표시할 리스트
const ul = document.querySelector(".list-container");

// 공지사항의 첫 페이지를 화면에 띄워주는 함수
const callFirstNotices = () => {
  // 현재 공지사항 페이지를 1로 초기화
  noticePage = 1;

  // 공지사항 목록 1페이지의 데이터 표시
  // getList의 리턴값은 Promise 객체이므로, 데이터를 활용하기 위해서는 .then() 사용
  noticeService.getList(noticePage, showNotices).then((notices) => {
    ul.innerHTML = notices;

    // 클릭 이벤트 추가
    addButtonEvent();
  });
}

// QnA의 첫 페이지를 화면에 띄워주는 함수
const callFirstQnAs = () => {
  // 현재 QnA 페이지를 1로 초기화
  qnaPage = 1;

  // QnA 목록 1페이지의 데이터 표시
  qnaService.getList(qnaPage, showQnAs).then((qnas) => {
    ul.innerHTML = qnas;

    // 클릭 이벤트 추가
    addButtonEvent();
  });
}

// 페이지가 열렸을 때 어떤 버튼이 눌려있는지에 따라 다른 정보(공지사항 or QnA) 출력
if (noticeButton.checked) {
  callFirstNotices();
} else {
  callFirstQnAs();
}

// 공지사항 버튼을 클릭했을 때의 이벤트
// 공지사항 버튼에 불 들어오고, qna 버튼은 꺼짐
// 또한, 위의 callFirstNotices 함수 사용
noticeButton.addEventListener("click", () => {
  // 공지사항 버튼 체크 시, QnA 버튼 체크 해체
  if (noticeButton.checked) {
    qnaButton.checked = false;
  }

  // 클래스로 인한 스타일 변경
  noticeButton.parentElement.classList.add("benner-inner-checked");
  qnaButton.parentElement.classList.remove("benner-inner-checked");

  // 공지사항의 첫 페이지를 불러와서 화면에 출력
  callFirstNotices();

  // 스크롤 이벤트 처리
});


// Q&A 버튼을 클릭했을 때의 이벤트
qnaButton.addEventListener("click", function () {
  // QnA 버튼 체크 시, 공지사항 버튼 체크 해제
  if (qnaButton.checked) {
    noticeButton.checked = false;
  }

  // 클래스로 인한 스타일 변경
  qnaButton.parentElement.classList.add("benner-inner-checked");
  noticeButton.parentElement.classList.remove("benner-inner-checked");

  // QnA의 첫 페이지를 불러와서 화면에 출력
  callFirstQnAs();

  // 스크롤 이벤트 처리
});


// 메뉴창 클릭 이벤트를 함수화
// querySelector가 새로 불러온 객체를 인식 못 하므로, 함수로 객체를 뿌린 뒤에 이벤트 리스너를 추가하기 위함
const addButtonEvent = () => {
  // 각 li 태그 안 데이터를 클랙했을 때의 이벤트
  // 함수화 가능?
  const items = document.querySelectorAll(".list-inner-box");

  // 각 li 태그 안 태그(객체)들을 가져옴
  items.forEach((item) => {
    const item1 = item.querySelector("h3.list-inner");
    const item2 = item.querySelector("span.question-text");
    const item3 = item.querySelector("span.question-v");
    const item4 = item.querySelector("div.question");

    // 각 리스트를 클릭했을 때, 안에 있는 태그들의 스타일 조정
    item.addEventListener("click", (e) => {
      item1.classList.toggle("list-inner-open");
      item2.classList.toggle("question-text-open");
      item3.classList.toggle("question-v-open");
      item4.classList.toggle("question-open");
    });
  });
}

// 윈도우 스크롤이 화면의 맨 아래로 내려가면, 다음 페이지 정보를 띄워주는 함수
// 다음 페이지에 띄울 게 공지사항인지 QnA인지만 다르기 때문에 따로 떼서 함수화
const scrollEvent = (callback) => {
  // 여기에 이벤트 리스너 틍록
  window.addEventListener('scroll', () => {
    // 현재 스크롤 위치
    let currentHeight = document.documentElement.scrollTop;

    let ulHeight = document.querySelector(".list-container").clientHeight;

    // 현재 열린 브라우저 창의 높이
    let windowHeight = window.innerHeight;

    // 현재 페이지 html의 총 높이
    let totalHeight = document.documentElement.scrollHeight;

    console.log(currentHeight, windowHeight, ulHeight, totalHeight);

    // 만약 스크롤을 맨 아래로 내리면 콜백함수(데이터 추가) 실행
    if (currentHeight + windowHeight >= totalHeight) {
      callback;
    }
  });
}