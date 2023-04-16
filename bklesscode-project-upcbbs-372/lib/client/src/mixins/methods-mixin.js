
export default {
    methods: {
        changeishsowEdit () {
            this.isshowEdit = true
        },
        getBBSDataList () {
            return this.$http.get('/data-source/user/tableName/bbs').then(res => {
            // 可以在这里添加业务操作
                this.bbslist = res?.data?.list
                return res
            }).catch((err) => {
                console.log(err)
            })
        },
        addBBSData () {
            return this.$http.post('/data-source/user/tableName/bbs', this.formCd7b5model).then(res => {
            // 可以在这里添加业务操作
                this.getBBSDataList()
                this.isshowEdit = false
                return res
            }).catch((err) => {
                console.log(err)
            })
        },
        getCommentDataList () {
            return this.$http.get('/data-source/user/tableName/comment').then(res => {
            // 可以在这里添加业务操作
                const bbsid = this.$route.query.bbsid
                this.commentList = res?.data?.list?.filter(item => +item.bbsid === +bbsid)
                return res
            }).catch((err) => {
                console.log(err)
            })
        },
        addCommentData () {
            return this.$http.post('/data-source/user/tableName/comment', {
                bbsid: this.$route.query.bbsid,
                comment: this.comment
            }).then(res => {
            // 可以在这里添加业务操作
                this.getCommentDataList()
                this.comment = ''
                return res
            }).catch((err) => {
                console.log(err)
            })
        },
        getBBSdetail () {
            this.$http.get(`/data-source/user/tableName/bbs/id/${this.$route.query.bbsid}`).then((res) => {
                this.bbsContent = res.data.content
                this.bbsTitle = res.data.title
            })
        },
        getData () {
            this.getBBSdetail()
            this.getCommentDataList()
        },
        goToDetail (bbsid) {
            this.$router.push({
                name: 'upclanjingdetail',
                query: {
                    bbsid
                }
            })
        }
    }
}
