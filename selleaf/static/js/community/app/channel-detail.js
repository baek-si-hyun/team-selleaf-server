// 페이징 밑 무한 스크롤
let page = 1;
let isLoading = false;
// 서버에서 데이터를 가져오는 메소드
async function getPosts() {
  // fetch에 데이터를 가져 올 주소 입력
  const response = await fetch("");
  const posts = await response.json();
  return posts.reverse(); // 최신순으로 가져오도록 역순으로 정렬
}
// 가져온 데이터로 li태그를 만들어 클래스 이름을 주고 안에 내용을 만들어
// ul태그안에 작성하는 메소드(ul에 innerHtml할 경우 덮어쓰기가 되어 한개의 리스트만 작성된다)
function appendItem(post) {
  const contentLine = document.querySelector(".content-line");
  const contentItem = document.createElement("span");

  contentItem.innerHTML = `
  <div class="content-wrap">
    <div class="content-container">
      <div class="content">
        <img
          src="../../../staticfiles/images/blank-image.png"
          alt="content-img"
          class="content-img"
        />
        <button
          type="button"
          aria-label="scrap 토글 버튼"
          class="scrap-btn"
        >
          <span class="scrap-btn-box"
            ><img
              src="../../../staticfiles/images/scrap-off.png"
              alt=""
            />
          </span>
        </button>
        <div class="img-count-box">
          <svg
            class="img-count-icon"
            xmlns="http://www.w3.org/2000/svg"
            height="13"
            viewBox="0 -960 960 960"
            width="12.7"
            fill="#ffffff"
          >
            <path
              d="M262.87-417.718v87.348h-83.652q-38.943 0-65.972-27.029-27.03-27.029-27.03-65.972v-357.346q0-38.942 27.03-65.972 27.029-27.029 65.972-27.029h357.346q38.942 0 65.972 27.103 27.029 27.102 27.029 66.148v83.337h-87.349v-89.24H173.565v368.652h89.305ZM422.871-86.782q-38.943 0-65.972-27.029-27.029-27.03-27.029-65.972v-357.346q0-38.943 27.029-65.972 27.029-27.029 65.972-27.029h357.346q38.942 0 65.972 27.029 27.029 27.029 27.029 65.972v357.346q0 38.942-27.029 65.972-27.03 27.03-65.972 27.03H422.871Zm-5.653-87.348H785.87v-368.652H417.218v368.652Zm184.326-184.326Z"
            />
          </svg>
          <div>8</div>
        </div>
      </div>
      <div class="content-content">
        혹시 지금 오늘의가든에서 키우고 있는 식물이
        있나요? 영양제와 물을 열심히 주는 오늘의
        가드너라면 우리 아이의 성장일지를 #오늘의가든
        채널에서 함께 나누고 소통해봐요 💬 열심히 키워서
        받은 수확물 자랑도 환영이에요! #식집사성장기
        #식집사일상
      </div>
      <a class="content-link" href="#"></a>
    </div>
    <div class="content-uploader-box">
      <a class="content-uploader" href="#">
        <figure class="uploader-icon-box">
          <img
            src="../../../staticfiles/images/blank-image.png"
            height="0"
            class="uploader-icon"
          />
        </figure>
        <div class="uploader-name">
          오늘의집 에디터 뭐뭐뭐입니다
        </div>
      </a>
      <button
        type="button"
        name="좋아요 버튼"
        class="like-btn"
      >
        <svg
          class="like-icon"
          xmlns="http://www.w3.org/2000/svg"
          height="19"
          viewBox="0 -960 960 960"
          width="19"
        >
          <path
            d="m480-179.81-32.922-29.96q-97.061-87.038-160.184-148.519-63.124-61.481-99.139-108.152-36.015-46.671-49.846-84.632-13.831-37.961-13.831-77.119 0-77.738 53.804-131.541 53.804-53.804 131.541-53.804 48.741 0 93.774 23.5 45.034 23.5 76.803 68.078 32.885-44.578 77.288-68.078 44.404-23.5 93.289-23.5 77.737 0 131.541 53.782 53.804 53.783 53.804 131.489 0 39.227-13.331 76.19-13.331 36.964-49.333 83.113-36.001 46.149-99.516 108.674-63.515 62.524-162.82 152.519L480-179.81Zm0-64.421q91.316-82.605 150.52-140.455 59.204-57.85 94.323-100.967 35.119-43.116 49.119-76.644 14-33.528 14-65.868 0-58.527-39.551-97.97-39.551-39.442-97.588-39.442-35.015 0-65.458 14.885-30.442 14.884-62.019 48.923l-35 41h-16.692l-35-41q-31.962-34.423-63.212-49.116-31.25-14.692-64.265-14.692-57.653 0-97.396 39.442-39.743 39.443-39.743 97.99 0 32.352 13.027 64.392t47.096 74.608q34.07 42.568 93.762 100.857Q385.615-330 480-244.231Zm0-261.269Z"
          />
        </svg>
        <span class="like-count">1K</span>
      </button>
    </div>
  </div>
  `;
  contentLine.appendChild(contentItem);
}
// 한번에 보여줄 리스트의 갯수를 정하고 차츰 페이지를 증가시킨다
function showList() {
  // 중복되어 실행되는 경우가 있어 그것을 막기위해 로딩 유무 파악
  // if (isLoading) return;

  // isLoading = true;
  // getPosts().then((posts) => {
  //   const rowCount = 20;
  //   const offset = (page - 1) * rowCount;
  //   const limit = offset + rowCount;
  //   posts = posts.slice(offset, limit);

  //   if (posts.length > 0) {
  //     posts.forEach((post) => {
  //       appendItem(post);
  //     });
  //     page++;
  //   }
  //   isLoading = false;
  // });
  const dummyArray = new Array(20).fill(0);
  dummyArray.forEach((post) => {
    appendItem(post);
  });
}
// 스크롤의 위치를 검색하고 조건에 맞춰 실행하는 함수
function handleScroll() {
  // 현재 문서의 상단에서 스크롤바의 위치까지의 거리를 나타내는 값을 가져온다.
  const scrollTop = document.documentElement.scrollTop;
  // 현재 창의 뷰포트 높이를 나타낸다.
  const windowHeight = window.innerHeight;
  // 문서의 총 높이를 나타내는 값을 가져온다.
  const totalHeight = document.documentElement.scrollHeight;
  // 스크롤바가 문서의 아래쪽 끝에 도달했을 때 아래의 코드를 실행한다.
  if (scrollTop + windowHeight >= totalHeight - 300) {
    showList();
  }
}
// 스크롤 이벤트가 발생할 때마다 스크롤바의 위치를 검사하여 새로운 콘텐츠를 불러오게 된다.
window.addEventListener("scroll", handleScroll);
// 최초 실행하여 1페이지를 보여준다
showList();

//스크랩 버튼;
const contentLineBox = document.querySelector(".content-line");
const scrapPopup = document.querySelector(".scrap-popup-wrap");
const scrapCancel = document.querySelector(".scrap-popup-cancel-wrap");

let timeoutId;
let animationTarget;

contentLineBox.addEventListener("click", handleScrapButtonClick);

function handleScrapButtonClick(e) {
  const target = e.target.closest(".scrap-btn");
  if (!target) return; // 스크랩 버튼이 아닌 경우 무시

  const img = target.querySelector("img");
  const imgSrc = img.getAttribute("src");

  if (imgSrc === "../../../staticfiles/images/scrap-off.png") {
    img.setAttribute("src", "../../../staticfiles/images/scrap-on.png");
    showPopup(scrapPopup);
  } else {
    img.setAttribute("src", "../../../staticfiles/images/scrap-off.png");
    showPopup(scrapCancel);
  }
}

// 팝업 보여주기
function showPopup(target) {
  clearTimeout(timeoutId);
  if (animationTarget) animationTarget.classList.remove("show-animation");
  animationTarget = target;
  animationTarget.classList.remove("hide-animation");
  animationTarget.classList.add("show-animation");

  // 일정 시간 후 팝업 숨기기
  timeoutId = setTimeout(() => {
    hidePopup();
  }, 3000);
}

// 팝업 숨기기
function hidePopup() {
  if (!animationTarget) return;
  animationTarget.classList.remove("show-animation");
  animationTarget.classList.add("hide-animation");
}

const modalWrap = document.querySelector(".modal-wrap");
const filterBtn = document.querySelector(".filter-btn");
modalWrap.addEventListener("click", (e) => {
  console.log(e.target.closest(".modal-content-item"));
  if (
    !e.target.closest(".modal-container") ||
    e.target.closest(".modal-cancel-btn")
  ) {
    modalWrap.classList.remove("modal-open");
  }
});
const modalContentItems = document.querySelectorAll(".modal-content-item");
modalContentItems.forEach((item) => {
  item.addEventListener("click", (e) => {
    filterBtn.innerHTML =
      e.target.innerText + `<span class="filter-drop-down-icon"></span>`;
    modalWrap.classList.remove("modal-open");
  });
});
filterBtn.addEventListener("click", (e) => {
  e.stopPropagation();
  modalWrap.classList.add("modal-open");
});
