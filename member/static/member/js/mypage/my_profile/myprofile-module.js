const postService = (()=>{

    const allPostList = async (member_id, callback) =>{
        console.log('모든 리스트 가져오기')
        const response = await fetch(`/member/mypage/show/${member_id}`);
        const posts = await response.json();
        console.log(posts)
        if (callback){
            return callback(posts)
        }
        return posts

    };

    const getList = async (member_id, callback) =>{
        console.log('리스트 가져오기')
        const response = await fetch(`/member/mypage/myposts/${member_id}`);
        const posts = await response.json();
        if (callback){
            return callback(posts)
        }
        return posts

    };

    const getReplies = async (member_id, callback)=>{
        console.log('댓글 가져오기')
        const response = await fetch(`/member/mypage/show/replies/${member_id}`);
        const replies = await response.json();
        if (callback){
            return callback(replies)
        }
        return replies

    };

    return {getList:getList, allPostList:allPostList, getReplies:getReplies}
})()