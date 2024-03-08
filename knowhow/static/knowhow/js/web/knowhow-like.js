const likeBtn = document.getElementById("like-btn");

likeBtn.addEventListener("click", () => {
    knowhowService.Like(knowhow_id, member_id).then()
})