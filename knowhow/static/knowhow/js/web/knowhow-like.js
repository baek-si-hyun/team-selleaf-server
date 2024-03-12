const scrapBox = document.getElementById('scrap-box')
let status = true

const getLike = (ls) => {
    let like = ``;

    console.log(ls)
    like = `
            <img
                class="sticky-icon"
                src='/selleaf/static/public/web/images/common/scrap-off.png'
                alt=""
            />
            `

    return like

}

knowhowService.getLikeScrap(knowhow_id, member_Id, status, getLike).then((like) => {
    scrapBox.innerHTML = like
})