<template>

    <el-container style="position:relative" v-show="bb==1">
        <el-drawer

                :visible.sync="drawer"
                :with-header="false"
                :direction="direction">
            <div style="height:700px">
                <h1 style="margin-left:100px">
                    <svg class="icon" aria-hidden="true" style="width:3em;height:3em">
                        <use xlink:href="#icon-quanxian"></use>
                    </svg>
                    <span style="margin-top:15px;margin-left:20px;position:absolute">协作权限管理</span>
                </h1>
                <div style="margin-top: 15px;">
                    <el-input placeholder="输入 邮箱/用户名 添加协作权限" v-model="search">
                        <template slot="prepend">
                            <el-popover
                                    placement="bottom-start"
                                    width="400"
                                    trigger="click">
                                <div v-if="searchItem.length>0">
                                    <ul v-for="(item,index) in searchItem" :key="index">
                                        <li style="position:relative">
                                            <el-avatar size="medium" :src="'/media/'+item.u_icon"></el-avatar>
                                            <span style="font-size:17px;position:absolute;margin-top:-5px;margin-left:20px">
        {{ item.u_username }}
        <el-button type="text" @click="dialogVisible = true;inviteId=item.id">
           <i class="el-icon-circle-plus-outline" style="font-size:20px"></i> 
        </el-button>
       
        </span>
                                        </li>
                                    </ul>
                                </div>
                                <div v-else>
                                    <pre style="color:gray;font-size:15px;font-weight:normal">                 当前搜索结果为0</pre>
                                </div>
                                <el-button slot="reference" @click="searchUser(search)">
                                    <svg class="icon" aria-hidden="true" style="width:2em;height:2em">
                                        <use xlink:href="#icon-sousuo"></use>
                                    </svg>
                                </el-button>
                            </el-popover>
                        </template>
                    </el-input>
                    <!--协作者列表卡片-->
                    <div>
                        <el-card class="box-card" shadow="never">
                            <div slot="header" class="clearfix">
                                <span style="font-size:17px;position:absolute;margin-top:-5px;margin-left:20px">协作者</span>
                            </div>
                            <div>
                                <div>
                                    <ul v-for="(item,index) in userItem" :key="index">
                                        <li style="position:relative">
                                            <svg class="icon" aria-hidden="true" style="width:2em;height:2em">
                                                <use xlink:href="#icon-renwu2"></use>
                                            </svg>
                                            <el-avatar size="medium" :src="'/media/'+item.u_icon" class="img"></el-avatar>
                                            <span class="user_name">
                     {{ item.u_username }}
                    </span>
                                            <p style="positon:relative;margin-left:70px">
                                                <el-button v-show="item.comment==0"
                                                           @click="changePower(index,item.id,1,item.change)">享有评论权限
                                                </el-button>
                                                <el-button v-show="item.comment==1"
                                                           @click="changePower(index,item.id,0,item.change)">无评论权限
                                                </el-button>
                                                <el-button v-show="item.change==0"
                                                           @click="changePower(index,item.id,item.comment,1)">享有修改权限
                                                </el-button>
                                                <el-button v-show="item.change==1"
                                                           @click="changePower(index,item.id,item.comment,0)">无修改权限
                                                </el-button>
                                            </p>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </el-card>
                    </div>
                </div>
            </div>

        </el-drawer>
        <el-dialog
                title="发送协作者邀请"
                :visible.sync="dialogVisible"
                width="30%"
                :before-close="handleClose">
            <el-input
                    type="textarea"
                    autosize
                    placeholder="请输入内容"
                    v-model="reason">
            </el-input>
            <span slot="footer" class="dialog-footer">
    <button class="btn-6" @click="invite(inviteId,reason)">确 定</button>
  </span>
        </el-dialog>
        <!--头部导航栏-->
        <el-header>
            <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
                <div class="flex flex6">
                    <div style="">
                        <svg class="icon" aria-hidden="true" style="width:4em;height:4em">
                            <use xlink:href="#icon-wendang"></use>
                        </svg>
                    </div>
                    <div style="margin-left:20px;margin-right:30px">
                        <h1 class="change-color" style="font-weight:lighter ">{{ document_type }}</h1>
                    </div>
                    <!--          <router-link :to="{path: '/changefile/'+fileId}">-->
                    <button class="btn-6 " v-show="change_power===0&&allow_edit===0" plain @click="goChangeFile">修改
                    </button>
                    <!--          </router-link>-->
                    <el-button class="btn-10 " v-show="change_power===0&&allow_edit===1" plain disabled>当前有人正在修改 禁止修改
                    </el-button>
                    <button class="btn-10 " v-show="change_power===1" plain disabled>您没有修改的权限</button>
                    <button class="btn-6 " v-show="type===1&&is_team===1" plain @click="drawer = true"
                            style="margin-left: 10px">
                        协作
                    </button>
                    <button class="btn-7" v-show="type===1&&allowShare===0" @click="set_allowShare(1)" plain>允许分享
                    </button>
                    <button class="btn-8" v-show="type===1&&allowShare===1" @click="set_allowShare(0)" plain>禁止分享
                    </button>

                    <input type="text" v-model="localURL" style="display: none">
                    <button class="copyURL btn-8"
                            v-if="allowShare==0"
                            :data-clipboard-text="localURL"
                            type="primary"
                            @click="copy" plain style="margin-left: 10px">
                        分享
                    </button>

                    <button class="btn-10" v-show="type==1" @click="del()" plain>删除</button>

                    <button class="btn-5" @click="$router.go(-1)"> < 返回前页</button>

                </div>
            </el-menu>
            <div style="position:relative">
                <div class="flex flex6" style="position:absolute;right:20px;top:-70px">
                    <el-button type="text" icon="el-icon-star-off" v-show="star==1" @click="set_favorite(0)"
                               style="color:gray;font-size:30px"></el-button>
                    <el-button type="text" icon="el-icon-star-on" v-show="star==0" @click="set_favorite(1)"
                               style="color:#ede159;font-size:30px"></el-button>
                    <span style="color:gray;font-size:12px;margin-left:20px">{{ creator }}创建于{{ create_date }}</span>
                </div>
            </div>
        </el-header>
        <!--drawer设置-->

        <!--中间文件内容-->
        <el-main>
            <el-row>
                <el-col :span="3" class="grid-content"></el-col>
                <el-col :span="18">
                  <div style="text-align: center; margin-top: 50px">
                    <h1 style="color: orange">注意：如果想修改文档，请点击上方的修改按钮进行修改</h1>
                  </div>
                    <h2 style="margin-top:60px">{{ title }}</h2>
                    <wang-enduit style="margin-top:30px" v-model="content"></wang-enduit>
                </el-col>
                <el-col :span="3" class="grid-content"></el-col>
            </el-row>
        </el-main>
        <!--底部评论区-->
        <el-footer>
            <el-row>
                <el-col :span="2" class="grid-content">
                </el-col>
                <el-col :span="20" style="position:relative">
                    <div v-if="comment_power==1">
                        <div class="mengban" v-if="comment_power==1" style="opacity: 0.5; background-color:#ededed">
                        </div>
                        <div class="mengban">
                            <p class="change-color" v-if="comment_power==1" style="margin-top:70px;font-size:23px">
                                您没有评论的权限</p>
                        </div>
                    </div>
                    <el-form ref="form" :model="form" label-width="100px">
                        <el-form-item label="评论">
                            <el-input type="textarea" v-model="form.desc"></el-input>
                        </el-form-item>
                        <el-form-item>
                            <el-button type="primary" @click="onSubmit(form.desc)">提交</el-button>
                        </el-form-item>
                    </el-form>

                </el-col>

                <el-col :span="2" class="grid-content"></el-col>
            </el-row>
            <div style="text-align: center; margin-bottom: 2rem">
                <h2 style="font-size: 2rem">评论区</h2>
            </div>

            <el-row v-for="(item, index) in comments" :key="index">
                <el-col :span="3" class="grid-content"></el-col>
                <el-col :span="19">
                    <el-card shadow="always" style="margin-bottom: 1rem">
                        <el-col :span="10"><span><h3>用户名：{{ item.u_username }}</h3></span></el-col>
                        <el-col :span="10"><span><h3>评论时间：{{ item.time }}</h3></span></el-col>
                        <el-col :span="4" v-if="type==1"><span><el-button class="btn-10" @click="deleteComment(index,item.id)">删除</el-button></span>
                        </el-col>
                        <el-col :span="24" class="grid-content"></el-col>
                        <el-col :span="24" style="margin-bottom: 1rem"><span>{{ item.content }}</span></el-col>
                    </el-card>
                </el-col>
                <el-col :span="2" class="grid-content"></el-col>
            </el-row>
        </el-footer>
    </el-container>
</template>

<script>
    import WangEnduit from "@/components/wangEnduit";

    export default {
        name: "editor",
        components: {
            WangEnduit,
        },
        data() {
            return {
              formInterval:null,
                form: {
                    desc: ''
                },
                allow_edit: -1,
                dialogVisible: false,
                inviteId: -1,
                reason: "",
                document_type: "个人文档",
                type: 1,
                change_power: -1,
                comment_power: 1,
                is_team: 1,
                team_id: 3242,
                title: "今天的交互",
                content: "sdas",
                creator: "ZZZ飘",
                create_date: "2020/1/1",
                allowShare: 1,
                star: 1,
                //悬浮框
                visible: false,
                isComment: false,
                localURL: '',
                value: '',
                //查找协作者
                search: "",
                searchItem: [

                ],
                author: {

                }
                ,
                //uploadPath,
                editor: null,
                info_: null,
                //title
                activeIndex: '1',
                activeIndex2: '1',
                //drawer
                drawer: false,
                direction: 'rtl',
                comments: [],
                fileId: 123,
                userItem: [],
                bb:0

            }
        },
      beforeDestroy() {
    clearInterval(this.formInterval)
  },
        mounted() {
            this.fileId = this.$route.params.documentId
            this.getURL()
             this.formInterval = setInterval(() => {
      this.getContentInTime()
    }, 1000)

            //35 获取文档信息
            this.$axios.get('/app/file_info/',
                {
                    params: {
                        id: this.fileId
                    },
                    headers: {'Content-Type': 'application/x-www-form-urlencoded'}
                }).then(res => {
                console.log(res)
                this.type = res.data.type
                if ((this.type === -1 && this.allowShare === 1) || res.data.is_delete === 1) {
                    this.$router.push({path: "/error"})
                } else if (this.type === -2) {
                    this.$router.push({path: "/login"})
                }
                this.change_power = res.data.change
                this.comment_power = res.data.comment
                this.team_id = res.data.team_id
                if (this.team_id > -1) {
                    this.document_type = "团队文档"
                    this.is_team = 0
                } else {
                    this.document_type = "个人文档"
                    this.is_team = 1
                }
                this.title = res.data.title
                this.content = res.data.content
                this.comments = res.data.comments
                this.allowShare = res.data.allow_Share
                this.star = res.data.star
                this.userItem = res.data.list
                this.creator = res.data.creator
                this.create_date = res.data.create_date
                this.bb=1
            })
        },
        methods: {
            getContentInTime() {
                //轮询，实时查看文档内容
                this.fileId = this.$route.params.documentId
                this.$axios.get('/app/file_content/',
                    {
                        params: {
                            id: this.fileId
                        },
                        headers: {'Content-Type': 'application/x-www-form-urlencoded'}
                    }).then(res => {
                    console.log(res)
                    this.title = res.data.title
                    this.content = res.data.content
                    if (res.data.status === 0) {
                        if (res.data.power === 0 || res.data.power === 2) {
                            this.allow_edit = 0
                        } else {
                            this.allow_edit = 1
                        }
                    } else {
                        this.allow_edit = 1
                    }
                })
            },
            handleClick() {
                alert('button click');
            },
            handleSelect(key, keyPath) {
                console.log(key, keyPath);
            },
            goBack() {
                console.log('go back');
            },
            searchUser(search) {
                //13 搜索用户
                this.$axios.post('/app/search_person/',
                    this.qs.stringify({
                        key: search,
                    }),
                    {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
                    .then(res => {
                        console.log(res)
                        this.searchItem = res.data.list
                    })
            },
            changePower(index, id, comment, change) {
                //16 分配个人文档权限
                this.$axios.get('/app/grant_power/', {
                    params: {
                        u_id: id,
                        id: this.fileId,
                        comment: comment,
                        change: change
                    },
                    headers: {'Content-Type': 'application/x-www-form-urlencoded'}
                }).then(res => {
                    console.log(res)
                    if (res.data.status == 0) {
                        this.userItem[index].change = change
                        this.userItem[index].comment = comment
                    }
                })
            },
            goChangeFile() {
                //37.5 判断是否掌握修改能力
                this.$axios.get('/app/get_change_power/', {
                    params: {
                        id: this.fileId
                    },
                    headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                }).then(res => {
                    if (res.data.status === 0) {
                        alert('获取修改能力成功，修改后请点击退出修改以便他人修改文档')
                        this.$router.push({path: '/changefile/' + this.fileId})
                    } else {
                        alert('获取修改能力失败，请等待当前修改文档的用户')
                    }
                })
            },
            set_allowShare(allowShare) {
                //38 设置分享权限
                this.$axios.get('/app/set_is_share/',
                    {
                        params: {
                            id: this.fileId,
                            type: allowShare
                        },
                        headers: {'Content-Type': 'application/x-www-form-urlencoded'}
                    }).then(res => {
                    console.log(res)
                    if (res.data.status === 0) {
                        this.allowShare = allowShare
                    } else {
                        this.$message.error(res.data.msg);
                    }
                })
            },
            set_favorite(type) {
                //39 收藏文档
                this.$axios.post('/app/deal_collect/',
                    this.qs.stringify({
                        id: this.fileId,
                        type: type
                    }),
                    {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
                    .then(res => {
                        console.log(res)
                        if (res.data.status == 0) {
                            this.star = type
                        } else {
                            this.$message.error(res.data.msg);
                        }
                    })
            },
            del() {
                //40 删除文档
                this.$confirm('您确定要删除该文档吗？', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                }).then(() => {
                    this.$axios.post('/app/delete_file/',
                        this.qs.stringify({
                            id: this.fileId
                        }),
                        {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
                        .then(res => {
                            console.log(res)
                            if (res.data.status == 0) {
                                this.$router.push({path: "/diamond/dashboard/desktop"})
                            } else {
                                this.$message.error(res.data.msg);
                            }
                        })
                })
            },
            onSubmit(content) {
                //45 评论文档
                this.$axios.post('/app/submit_comment/',
                    this.qs.stringify({
                        id: this.fileId,
                        content: content
                    }),
                    {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
                    .then(res => {
                        console.log(res)
                        if (res.data.status == 0) {
                            this.$message({
                                message:"评论成功",
                                type : "success",
                            })
                            this.form.desc = ""
                            var com = {
                                id: res.data.id,
                                time: res.data.time,
                                u_username: res.data.u_username,
                                content: content
                            }
                            this.comments.push(com)
                        } else {
                            this.$message.error(res.data.msg);
                        }
                    })
            },
            invite(id, reason) {
                //47 邀请加入协作者
                this.$axios.post('/app/cooperate_invitation/',
                    this.qs.stringify({
                        id: this.fileId,
                        u_id: id,
                        reason: reason
                    }),
                    {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
                    .then(res => {
                        console.log(res)
                        if (res.data.status === 0) {
                            //发送邀请成功
                        } else {
                            this.$message.error(res.data.$msg);
                        }
                    })
                this.reason = ""
                this.dialogVisible = false
            },
            deleteComment(index,id) {
                //51 删除评论
                this.$confirm('您确定要删除这条评论吗？', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                }).then(() => {
                    this.$axios.get('/app/delete_comment/', {
                        params: {
                            id: id,
                        },
                        headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                    }).then(res => {
                        if (res.data.status === 0 ) {
                            this.comments.splice(index,1)
                            this.$message({
                                message: '删除成功',
                                type: 'success',
                            })
                        }
                    })
                })
            },

            copy() {
                let clipboard = new this.Clipboard('.copyURL');
                clipboard.on('success', e => {
                    this.$message({
                        type: 'success',
                        message: '链接已复制到剪贴板'
                    });
                    this.aa = e
                    clipboard.destroy()
                })
            },
            getURL() {
                this.localURL = location.href
            },
            handleClose(done) {
                done();
                this.reason = ""
            },
        }
    }
</script>

<style>
    .mengban {
        position: absolute;
        height: 170px;
        text-align: center;
        width: 100%;
        margin-left: 3%;;
        margin-top: -20px;
        z-index: 100
    }

    .editor {
        width: 100%;
        margin: 0 auto;
        position: relative;
        z-index: 0;
    }

    .toolbar {
        border: 1px solid #ccc;
    }

    .text {
        border: 1px solid #ccc;
        min-height: 500px;
    }

    .el-row {
        margin-bottom: 20px;

    &
    :last-child {
        margin-bottom: 0;
    }

    }
    .el-col {
        border-radius: 4px;
    }

    .bg-purple-dark {
        background: #99a9bf;
    }

    .bg-purple {
        background: #d3dce6;
    }

    .bg-purple-light {
        background: #e5e9f2;
    }

    .grid-content {
        border-radius: 4px;
        min-height: 36px;
    }

    .row-bg {
        padding: 10px 0;
        background-color: #f9fafc;
    }
</style>
