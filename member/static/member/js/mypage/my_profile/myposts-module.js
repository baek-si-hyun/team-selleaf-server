const postService = (()=>{
    const getList = async (member_id, callback) =>{
        console.log('리스트 가져오기')
        const response = await fetch(`/member/mypage/myposts/${member_id}`);
        const posts = await response.json();
        if (callback){
            return callback(posts)
        }
        return posts

    };

    return {getList:getList}
})()