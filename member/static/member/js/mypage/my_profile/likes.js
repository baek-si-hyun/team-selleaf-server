// 마이페이지/프로필/노하우 js 파일

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

let page = 1;

const showLikeList = (likes) => {
  let text = ``
  console.log('리스트 보여주기')
  likes.forEach((like) => {
    if ('post_id' in like) {
      text += `
          <div class="post-container">
            <div class="post-inner">
              <article class="post">
                <a href="#" class="post-link"></a>
                <div class="post-image-wrap_">
                  <div class="post-image-container">
                    <div class="post-image-inner">
                      <div class="post-image"></div>
                      <img
                        src="/upload/${like.post_file}"
                        alt=""
                        class="image"
                      />
                    </div>
                  </div>
                </div>
              </article>
            </div>
          </div>
          `;
    }else  if('knowhow_id' in like) {
      text += `
          <div class="post-container">
            <div class="post-inner">
              <article class="post">
                <a href="#" class="post-link"></a>
                <div class="post-image-wrap_">
                  <div class="post-image-container">
                    <div class="post-image-inner">
                      <div class="post-image"></div>
                      <img
                        src="/upload/${like.knowhow_file}"
                        alt=""
                        class="image"
                      />
                    </div>
                  </div>
                </div>
              </article>
            </div>
          </div>
          `;
    }
  });
  return text
};

const wrap = document.querySelector('.post-wrap')

postService.getLikes(page++,showLikeList).then((text)=>{
  wrap.innerHTML += text
})

window.addEventListener("scroll", () => {
    // 맨위
    const scrollTop = document.documentElement.scrollTop;
    // 페이지 높이
    const windowHeight = window.innerHeight;
    // 암튼 높이
    const totalHeight = document.documentElement.scrollHeight;
    // 전체 높이에서 내가 보는 스크롤이 total보다 크면 추가

    if (scrollTop + windowHeight >= totalHeight) {
      postService.getLikes(page++,showLikeList).then((text)=>{
        wrap.innerHTML += text
      })
    }
});




