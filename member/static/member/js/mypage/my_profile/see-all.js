// 마이페이지/프로필/모두보기 js 파일

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
  강사 여부에 따라 강의 현황 메뉴 표시/숨김
*/

// 강사 여부
let isTeacher = false;

// 강의 현황메뉴 객체
const myClassMenu = document.querySelector(".teacher");

// 강사면 강의 현황 메뉴 표시, 아니면 숨김
if (isTeacher) {
  myClassMenu.style.display = "inline-block";
} else {
  myClassMenu.style.display = "none";
}


// 스크랩 한 게시글 개수
let posts = document.querySelectorAll(".post-wrap .post-container");

// 게시글 수를 표시할 span 태그
const postCount = document.querySelector(".post-count");

// 현재 게시글 개수를 span 태그 안에 표시
postCount.innerText = posts.length;

/* 
  각 리뷰글에 마우스 올린 경우 제목, 본문, 이미지 투명도 조정

  또한, 현재 게시글 개수도 표시
*/

// 각 리뷰글
const reviewsItems = document.querySelectorAll(".reviews-history-item-wrap");

// 각 리뷰글에 mouseover, mouseout 이벤트 추가
reviewsItems.forEach((item) => {
  // 각 리뷰글의 이미지, 제목, 본문을 변수화
  const itemImage = item.children[1].children[0];
  const itemTitle = item.children[1].children[1];
  const itemArticle = item.children[1].children[2];

  item.addEventListener("mouseover", () => {
    itemImage.style.opacity = 0.6;
    itemTitle.style.opacity = 0.6;
    itemArticle.style.opacity = 0.6;
  });

  item.addEventListener("mouseout", () => {
    itemImage.style.opacity = 1;
    itemTitle.style.opacity = 1;
    itemArticle.style.opacity = 1;
  });
});

/*
  리뷰 내역의 유무에 따라 표시할 내용 변경
*/

// 리뷰 내역이 없을 때 보이는 태그
const noContents = document.querySelector(".no-reviews");

// 각 리뷰 내역 사이의 구분선
const itemsSeperator = document.querySelectorAll(".items-seperator");

// 리뷰 내역이 있을 경우
if (reviewsItems.length >= 1) {
  // 리뷰 내역 없을 때 뜨는 텍스트들 안 보이게 함
  noContents.style.display = "none";

  // 각 리뷰내역 표시
  reviewsItems.forEach((item) => {
    item.style.display = "block";
  });

  // 구분선 표시
  itemsSeperator.forEach((item) => {
    item.style.display = "block";
  });
}
// 리뷰 내역이 없을 경우
else {
  // 리뷰 내역 없을 때 뜨는 텍스트들을 보이게 함
  noContents.style.display = "block";

  // 각 리뷰내역 숨김
  reviewsItems.forEach((item) => {
    item.style.display = "none";
  });

  // 구분선 숨김
  itemsSeperator.forEach((item) => {
    item.style.display = "none";
  });
}

// 리뷰 수를 표시할 span 태그
const reviewCount = document.querySelector(".review-count");

// 현재 리뷰 개수를 span 태그 안에 표시
reviewCount.innerText = reviewsItems.length;


const showList = (posts) => {
  let text = ``
  console.log('리스트 보여주기')
  posts.forEach((post) => {
    if (post.length === 0) {
      text = `
      <a class="photo-upload-wrap no-posts" href="#">
        <img alt=""
          class="add-icon"
          src="../../../images/mypage/add-icon.svg"
        />
        첫 번째 게시글을 올려보세요
      </a>
    `
    }else {
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
                  <span class="post-contents-user"
                    >${post.member_name}</span
                  >
                  <span class="post-contents-banner"
                    >${post.post_title}</span
                  >
                </h1>
                <span class="post-price">
                  <span class="post-price-letter"
                    >${post.post_content}</span
                  >
                </span>
                <div class="post-content-pc-reply">
                  <p class="post-content-reply">댓글  ${post.post_reply.length}</p>
                  <p class="post-content-scrap">
                    조회수  ${post.post_count}
                  </p>
                </div>
                <span class="post-tag">
                  ${post.post_plant.forEach((plant)=> {
                    const tag = document.querySelector('.post-tag')
                    tag.innerHTML = <span className="post-tag-icon">${plant}</span>
                  })}
                </span>
              </div>
            </div>
          </article>
        </div>
      </div>
    `
    }

  })
  return text
}

const wrap = document.querySelector('.post-wrap')

postService.getList(member_id,showList).then((text)=>{
  wrap.innerHTML = text
})


















