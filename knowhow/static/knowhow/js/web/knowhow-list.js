let page = 1;

const knowhowSection = document.querySelector(".content-line-box");

const showList = (knowhows) => {
    let text = ``;
    console.log(knowhows)

    knowhows.forEach((knowhow) => {
        text += `
            <div class="content-item-wrap">
              <div class="content-item-container">
                <div class="content-img-box">
                  <img
                    src="/upload/${knowhow.knowhow_file}"
                    class="content-img"
                  />
                  <div class="scrap-btn-box">
                    <button
                      type="button"
                      aria-label="scrap 토글 버튼"
                      class="scrap-btn"
                    >
                      <span class="scrap-icon-box">
                        <img
                          src="../../../staticfiles/images/scrap-off.png"
                          alt=""
                        />
                      </span>
                    </button>
                  </div>
                </div>
                <p class="content-title">
                
                </p>
                <div class="content-bottom-box">
                  <div class="content-uploader">
                    <div class="uploader-img-box">
                      <img
                        src="../../../staticfiles/images/blank-image.png"
                        class="uploader-img"
                      />
                    </div>
                    <span class="uploader-name">${knowhow.member_name}</span>
                  </div>
                  <div class="content-data-box">
                    <span class="content-data"
                      >스크랩 <span>3</span>
                    </span>
                    <span class="content-data"
                      >조회 <span>${knowhow.knowhow_count}</span>
                    </span>
                  </div>
                </div>
              </div>
            </div>
          `;
    });

    return text;
}

function handleScroll() {
    // 맨위
    const scrollTop = document.documentElement.scrollTop;
    // 페이지 높이
    const windowHeight = window.innerHeight;
    // 암튼 높이
    const totalHeight = document.documentElement.scrollHeight;
    // 전체 높이에서 내가 보는 스크롤이 total보다 크면 추가
    if (scrollTop + windowHeight >= totalHeight - 300) {
        knowhowService.getList(++page, showList).then((text) => {
            knowhowSection.innerHTML += text;
        });
    }
}

// 스크롤 할대마다 실행
    window.addEventListener("scroll", handleScroll);
    knowhowService.getList(++page, showList).then((text) => {
        knowhowSection.innerHTML += text;
    });


// knowhowService.getList(page, showList).then((text) => {
//     knowhowSection.innerHTML = text;
// });


function timeForToday(datetime) {
    const today = new Date();
    const date = new Date(datetime);

    let gap = Math.floor((today.getTime() - date.getTime()) / 1000 / 60);

    if (gap < 1) {
        return "방금 전";
    }

    if (gap < 60) {
        return `${gap}분 전`;
    }

    gap = Math.floor(gap / 60);

    if (gap < 24) {
        return `${gap}시간 전`;
    }

    gap = Math.floor(gap / 24);

    if (gap < 31) {
        return `${gap}일 전`;
    }

    gap = Math.floor(gap / 31);

    if (gap < 12) {
        return `${gap}개월 전`;
    }

    gap = Math.floor(gap / 12);

    return `${gap}년 전`;
}












