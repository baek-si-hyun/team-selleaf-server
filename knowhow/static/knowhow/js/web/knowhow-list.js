let page = 1;

const knowhowSection = document.querySelector(".content-line-box");

const showList = (knowhows) => {
    let text = ``;
    console.log(knowhows)

    knowhows.forEach((knowhow) => {
        text += `
            <a href="/knowhow/detail/?id=${knowhow.id}" class="knowhow-content-wrap">
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
                        ${knowhow.knowhow_title}
                    </p>
                    <div class="content-bottom-box">
                      <div class="content-uploader">
                        <div class="uploader-img-box">
                          <img
                            src="${knowhow.profile}"
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
            </a>
          `;
    });

    return text;
}


knowhowService.getList(page++, showList).then((text) => {
            knowhowSection.innerHTML += text;
        });

// 스크롤 할대마다 실행
window.addEventListener("scroll", () => {
    // 맨위
    const scrollTop = document.documentElement.scrollTop;
    // 페이지 높이
    const windowHeight = window.innerHeight;
    // 암튼 높이
    const totalHeight = document.documentElement.scrollHeight;
    // 전체 높이에서 내가 보는 스크롤이 total보다 크면 추가

    if (scrollTop + windowHeight >= totalHeight) {
        knowhowService.getList(page++, showList).then((text) => {
            knowhowSection.innerHTML += text;

        });
    }
});













