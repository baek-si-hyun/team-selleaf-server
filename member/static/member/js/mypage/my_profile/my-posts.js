// // 마이페이지/프로필/사진 js 파일
//
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

const showList = (posts) => {
  let text = ``
  posts.forEach((post) => {
      if('post_title' in post) {
      const postPlantTags = post.post_plant.map(plant => `<span class="post-tag-icon">${plant}</span>`).join('');

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
                          src="/upload/${post.post_file}"
                          alt=""
                          class="image"
                        />
                        <div class="image__dark-overlay"></div>
                      </div>
                    </div>
                  </div>
                  <div class="post-contents-wrap">
                    <div class="post-contents-container">
                      <h1 class="post-contents-header">
                        <span class="post-contents-user">${post.member_name}</span>
                        <span class="post-contents-banner">${post.post_title}</span>
                      </h1>
                      <span class="post-price">
                        <span class="post-price-letter">${post.post_content}</span>
                      </span>
                      <div class="post-content-pc-reply">
                        <p class="post-content-reply">댓글 ${post.post_reply.length}</p>
                        <p class="post-content-scrap">조회수 ${post.post_count}</p>
                      </div>
                      <span class="post-tag">${postPlantTags}</span>
                    </div>
                  </div>
                </article>
              </div>
            </div>
          `;
      }else if('knowhow_title' in post){
      const knowhowPlantTags = post.knowhow_plant.map(knowhow_plant => `<span class="post-tag-icon">${knowhow_plant}</span>`).join('');
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
                          src="/upload/${post.knowhow_file}"
                          alt=""
                          class="image"
                        />
                        <div class="image__dark-overlay"></div>
                      </div>
                    </div>
                  </div>
                  <div class="post-contents-wrap">
                    <div class="post-contents-container">
                      <h1 class="post-contents-header">
                        <span class="post-contents-user">${post.writer}</span>
                        <span class="post-contents-banner">${post.knowhow_title}</span>
                      </h1>
                      <span class="post-price">
                        <span class="post-price-letter">${post.knowhow_content}</span>
                      </span>
                      <div class="post-content-pc-reply">
                        <p class="post-content-reply">댓글 ${post.knowhow_reply.length}</p>
                        <p class="post-content-scrap">조회수 ${post.knowhow_count}</p>
                      </div>
                      <span class="post-tag">${knowhowPlantTags}</span>
                    </div>
                  </div>
                </article>
              </div>
            </div>
          `;
      }
    
  });

  return text;
};

const wrap = document.querySelector('.post-wrap')

postService.getList(page++,showList).then((text)=>{
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
        postService.getList(page++,showList).then((text)=>{
          wrap.innerHTML += text
        })
    }
});



















