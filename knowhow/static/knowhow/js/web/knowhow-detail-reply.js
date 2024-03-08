let page = 1;

const writeButton = document.querySelector(".comment-submit-btn");
const replySection = document.querySelector(".reply-section");
const moreButton = document.getElementById("more-replies");
const replyCount = document.getElementById("reply-count")

replyService.getList(knowhow_id, page + 1).then((replies) => {
    if (replies.length !== 0){
        moreButton.style.display = "flex";
    }
});

// replyService.count(knowhow_id).then((counts) => {
//     console.log(counts);
// })

const showCount = (counts) => {
    let replyText = `${counts.counts}`
}

const showList = (replies) => {
    let text = ``;
    replies.forEach((reply) => {
        // console.log(reply.created_date)
        text += `
            <div class="comment-item-box">
                      <div class="comment-item">
                        <div class="comment-user-img-wrap">
                          <figure class="comment-user-img-container">
                            <img
                              src="/static/public/web/images/common/blank-image.png"
                              height="0"
                              class="comment-user-img"
                            />
                          </figure>
                        </div>
                        <div class="comment-content-box">
                          <div class="comment-user-name-box">
                            <div role="link" class="commment-user-name">
                              ${reply.member_name}
                            </div>
                          </div>
                          <div class="comment">
                            ${reply.knowhow_reply_content}
                          </div>
                          <div class="comment-data">
                            <div class="time-before">${timeForToday(reply.created_date)}</div>
                            <div class="comment-like-btn-box">
                              <div class="comment-split">・</div>
                              <button type="button" class="comment-like-btn">
                                <img
                                  src="/staticfiles/images/like-off.png"
                                  class="comment-like-icon"
                                  alt=""
                                />
                                <span class="comment-like-text">좋아요</span>
                              </button>
                            </div>
                            <div class="comment-declaration-btn-box">
                              <div class="comment-split">・</div>
                              <button class="comment-declaration-btn">
                                신고
                              </button>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
        `;
        // if(reply.member_id === Number(memberId)) {
        //     text += `
        //                     <span class="date">·</span>
        //                     <span class="update ${reply.id}">수정</span>
        //                     <span class="date">·</span>
        //                     <span class="delete ${reply.id}">삭제</span>
        //     `
        // }
        // text += `
        //                 </h6>
        //             </section>
        //         </div>
        //     </li>
        // `;
    });

    return text;
}

moreButton.addEventListener("click", (e) => {
    replyService.getList(knowhow_id, ++page, showList).then((text) => {
        replySection.innerHTML += text;
    });

    replyService.getList(knowhow_id, page + 1).then((replies) => {
    if (replies.length === 0){
        moreButton.style.display = "none";
    }
});

});

writeButton.addEventListener("click", async (e) => {
    const replyNum = document.getElementById("reply-count");
    const replyContent = document.getElementById("reply-content");
    await replyService.write({
        reply_content: replyContent.value,
        knowhow_id: knowhow_id
    });
    replyContent.value = "";

    page = 1
    const text = await replyService.getList(knowhow_id, page, showList);
    replySection.innerHTML = text;

    const replies = await replyService.getList(knowhow_id, page + 1);



    if (replies.length !== 0){
        moreButton.style.display = "flex";
    }



    commentSubmitBtn.disabled = true;
    commentSubmitBtn.style.cursor = 'context-menu';
    commentSubmitBtn.style.color = "rgb(194, 200, 204)"
});

replyService.getList(knowhow_id, page, showList).then((text) => {
    replySection.innerHTML = text;
});

// ul 태그의 자식 태그까지 이벤트가 위임된다.
replySection.addEventListener("click", async (e) => {
    if(e.target.classList[0] === 'update'){
        const replyId = e.target.classList[1]
        const updateForm = document.getElementById(`update-form${replyId}`)

        updateForm.style.display = "block";
        updateForm.previousElementSibling.style.display = "none";

    }else if(e.target.classList[0] === 'calcel'){
        const replyId = e.target.classList[1]
        const updateForm = document.getElementById(`update-form${replyId}`)
        updateForm.style.display = "none";
        updateForm.previousElementSibling.style.display = "block";

    }else if(e.target.classList[0] === 'update-done'){
        const replyId = e.target.classList[1]
        const replyContent = document.querySelector(`#update-form${replyId} textarea`);
        await replyService.update({replyId: replyId, replyContent: replyContent.value})
        page = 1
        const text = await replyService.getList(post_id, page, showList);
        replySection.innerHTML = text;
        const replies = await replyService.getList(post_id, page + 1);
        if (replies.length !== 0){
            moreButton.style.display = "flex";
        }

    }else if(e.target.classList[0] === 'delete'){
        const replyId = e.target.classList[1];
        await replyService.remove(replyId);
        page = 1
        const text = await replyService.getList(knowhow_id, page, showList);
        replySection.innerHTML = text;

        const replies = await replyService.getList(knowhow_id, page + 1);
        if (replies.length !== 0){
            moreButton.style.display = "flex";
        }
    }
});




const date = document.querySelector(".week-data")
let test = new Date(knowhowDate)
// console.log(Date())
// console.log(Date(knowhowDate))
// console.log(Date(knowhowDate).format('%Y-%m-%dT%H:%M:%SZ'))
// console.log(knowhowDate)
// console.log(Date().toISOString(knowhowDate))
// console.log(timeForToday(knowhowDate))
date.innerText = timeForToday(Date(knowhowDate))




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












