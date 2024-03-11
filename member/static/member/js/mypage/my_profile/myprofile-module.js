const postService = (()=>{

    const allPostList = async (page, callback) =>{
        console.log('모든 리스트 가져오기')
        const response = await fetch(`/member/mypage/show/${page}`);
        const posts = await response.json();
        console.log(posts)
        if (callback){
            return callback(posts)
        }
        return posts

    };

    const getList = async (page, callback) =>{
        console.log('리스트 가져오기')
        const response = await fetch(`/member/mypage/show/posts/${page}`);
        const posts = await response.json();
        if (callback){
            return callback(posts)
        }
        return posts

    };

    const getReplies = async (page, callback)=>{
        const response = await fetch(`/member/mypage/show/replies/${page}`);
        const replies = await response.json();
        if (callback){
            return callback(replies)
        }
        return replies

    };

        const getReviews = async (page, callback)=>{
        console.log('댓글 가져오기')
        const response = await fetch(`/member/mypage/show/reviews/${page}`);
        const reviews = await response.json();
        if (callback){
            return callback(reviews)
        }
        return reviews

    };


    const getLikes = async (page, callback)=>{
        const response = await fetch(`/member/mypage/show/likes/${page}`);
        const likes = await response.json();
        if (callback){
            return callback(likes)
        }
        return likes

    };

    return {getList:getList, allPostList:allPostList, getReplies:getReplies, getReviews:getReviews,getLikes:getLikes }
})()