<template>
    <bk-navigation
        head-theme-color="#FFFFFF"
        navigation-type="top-bottom"
        :need-menu="false"
        class="bk-layout-custom-component-wrapper"
        :class="{ 'white-navigation': true }">
        <template slot="side-header">
            <span class="title-icon">
                <img
                    src="https://bkrepo.ce.bktencent.com/generic/bksaas-addons/public-bkapp-bk_les-5/372/file-lib/28fecd9621ebe7cce38a3c4136b9fdd5.jpg"
                    style="width: 28px; height: 28px;"
                />
            </span>
            <span class="title-desc" :class="{ 'theme-style': true }">dididada的论坛</span>
        </template>
        <div class="navigation-header" slot="header">
            <ol class="header-nav">
                <bk-popover
                    v-for="item in topMenuLesscode"
                    :disabled="!item.children || item.children.length <= 0"
                    :key="item.id"
                    theme="light navigation-message"
                    :arrow="false"
                    offset="0, -5"
                    placement="bottom"
                    :tippy-options="{ flipBehavior: ['bottom'], appendTo: 'parent' }">
                    <li
                        class="header-nav-item"
                        :class="{ 'item-active': item.id === curNav.id, 'theme-item': true }"
                        @click="goToPage(item)">
                        {{ item.name }}
                    </li>
                    <template slot="content">
                        <ul class="navigation-head-nav">
                            <li
                                class="nav-item"
                                v-for="headerNavItem in item.children"
                                :key="headerNavItem.id"
                                @click="goToPage(headerNavItem)">
                                {{ headerNavItem.name }}
                            </li>
                        </ul>
                    </template>
                </bk-popover>
            </ol>
            <bk-popover
                class="nav-head-right"
                theme="light navigation-message"
                :arrow="false"
                offset="-10, 0"
                placement="bottom-start"
                :tippy-options="{ hideOnClick: false, appendTo: 'parent' }">
                <div class="header-user" :class="{ 'theme-style': true }">
                    <span>{{ user.username }}</span>
                    <i class="bk-icon icon-down-shape"></i>
                </div>
                <template slot="content">
                    <span @click="signOut" class="nav-sign-out">退出</span>
                </template>
            </bk-popover>
        </div>
        <router-view class="page-container"></router-view>
    </bk-navigation>
</template>
<script>
    /**
     * 请先安装 bk-magic-vue 组件库、bkui-vue-complex 复合组件库
     * bk-magic-vue 组件库: https://magicbox.bk.tencent.com/static_api/v3/components_vue/2.0/example/index.html#/install
     * bkui-vue-complex 复合组件库: https://github.com/TencentBlueKing/lesscode-comp
     *
     * 如果页面使用了远程函数，单独使用本页面，需要确保项目 store 下有相应的方法，后端有相应的转发接口
     */

    import { mapGetters } from 'vuex'
    import auth from '@/common/auth'

    export default {
        data () {
            return {
                curNav: {},
                topMenuLesscode: [
                    {
                        name: '论坛首页',
                        id: 'cmmmgieomhfodbln',
                        icon: 'icon-block-shape',
                        pageCode: 'upclanjinghome',
                        link: '',
                        children: []
                    }
                ]
            }
        },
        computed: {
            ...mapGetters(['user'])
        },
        watch: {
            $route () {
                this.setNav()
            }
        },
        created () {
            this.setNav()
        },
        methods: {
            goToPage (item) {
                if (this.$route.query.id === item.id) return

                this.setNav(item.id)
                const originQuery = item.query || ''
                const queryStr = originQuery[0] === '?' ? originQuery.slice(1) : originQuery
                const queryArr = queryStr.split('&').filter(v => v)
                const query = queryArr.reduce(
                    (res, item) => {
                        const [key, value = ''] = item.split('=')
                        res[key] = value
                        return res
                    },
                    { id: item.id }
                )
                if (item.pageCode && item.pageCode === this.$route.name) {
                    this.$router.push({ path: this.$route.path, query })
                } else if (item.pageCode) {
                    this.$router.push({ name: item.pageCode, query })
                } else if (item.fullPath) {
                    this.$router.push({ path: item.fullPath, query })
                } else if (item.link) {
                    window.open(item.link, '_blank')
                } else {
                    this.$router.push({ path: 'hlefalbp', query })
                }
            },
            signOut () {
                auth.signOut()
            },
            setNav (id) {
                const itemId = id || this.$route.query.id
                const name = this.$route.name
                ;(this.topMenuLesscode || []).forEach(topNav => {
                    const isSameId
                        = itemId
                            && (topNav.id === itemId
                                || (Array.isArray(topNav.children) && topNav.children.find(nav => nav.id === itemId)))
                    const isSameName
                        = !itemId
                            && name
                            && (topNav.pageCode === name
                                || (Array.isArray(topNav.children) && topNav.children.find(nav => nav.pageCode === name)))
                    if (isSameId || isSameName) this.curNav = topNav || {}
                })
            }
        }
    }
</script>
<style lang="css" scoped>
    .container-hlefalbp {
        padding-left: 24px;
        padding-right: 24px;
        padding-top: 20px;
        padding-bottom: 0px;
        height: 100%;
    }
    .bk-layout-row-hlefalbp {
        display: flex;
    }
    .bk-layout-row-hlefalbp:after {
        display: block;
        clear: both;
        content: '';
        font-size: 0;
        height: 0;
        visibility: hidden;
    }
    .bk-layout-col-hlefalbp {
        float: left;
        position: relative;
        min-height: 1px;
    }
    .bk-free-layout-hlefalbp {
        height: 500px;
        width: 100%;
        display: inline-block;
        position: relative;
    }
    .bk-free-layout-item-inner-hlefalbp {
        height: 100%;
        position: relative;
    }
    .bk-form-radio {
        margin-right: 20px;
    }
    .bk-form-checkbox {
        margin-right: 20px;
    }
    .echarts {
        width: 100%;
        height: 100%;
    }
    /* 设置 bk-exception 组件宽度为 100% */
    .bk-exception-img {
        width: 100%;
    }
    .bk-form-item {
        margin: 10px;
    }
    .bk-sideslider {
        margin: 0;
    }
    /* 设置 .bk-form-control 组件宽度为 auto */
    .bk-form-control {
        width: auto;
    }
    .bk-form-control .bk-input-text {
        font-size: 12px;
    }
    [align-horizontal-left] > *,
    [align-horizontal-center] > *,
    [align-horizontal-right] > *,
    [align-horizontal-space-between] > *,
    [align-vertical-top] > *,
    [align-vertical-center] > *,
    [align-vertical-bottom] > * {
        flex-shrink: 0;
    }
    [align-horizontal-left],
    [align-horizontal-center],
    [align-horizontal-right],
    [align-horizontal-space-between] {
        display: flex !important;
        align-items: flex-start;
        flex-wrap: wrap;
    }
    [align-horizontal-left] {
        justify-content: flex-start;
    }
    [align-horizontal-center] {
        justify-content: center;
    }
    [align-horizontal-right] {
        justify-content: flex-end;
    }
    [align-horizontal-space-between] {
        justify-content: space-between;
    }
    [align-vertical-top],
    [align-vertical-center],
    [align-vertical-bottom] {
        display: flex !important;
        flex-wrap: wrap;
    }
    [align-vertical-top] {
        align-items: flex-start;
    }
    [align-vertical-center] {
        align-items: center;
    }
    [align-vertical-bottom] {
        align-items: flex-end;
    }
    [absolute-align-horizontal-left] {
        left: 0 !important;
    }
    [absolute-align-horizontal-center] {
        left: 50% !important;
        transform: translateX(-50%) !important;
    }
    [absolute-align-horizontal-right] {
        left: unset !important;
        right: 0 !important;
    }
    [absolute-align-vertical-top] {
        top: 0 !important;
    }
    [absolute-align-vertical-center] {
        top: 50% !important;
        transform: translateY(-50%) !important;
    }
    [absolute-align-vertical-bottom] {
        top: unset !important;
        bottom: 0 !important;
    }
    [absolute-align-horizontal-center][absolute-align-vertical-center] {
        transform: translate(-50%, -50%) !important;
    }

    .bk-navigation {
        width: auto;
        height: 100vh;
        outline: 1px solid #ebebeb;
    }
    .bk-navigation .bk-navigation-wrapper {
        height: calc(100vh - 252px) !important;
    }
    .bk-navigation-wrapper .navigation-container .container-content {
        padding: 0px;
    }
    .navigation-header {
        -webkit-box-flex: 1;
        -ms-flex: 1;
        flex: 1;
        height: 100%;
        display: -webkit-box;
        display: -ms-flexbox;
        display: flex;
        -webkit-box-align: center;
        -ms-flex-align: center;
        align-items: center;
        font-size: 14px;
    }
    .navigation-header .header-nav {
        display: -webkit-box;
        display: -ms-flexbox;
        display: flex;
        padding: 0;
        margin: 0;
    }
    .navigation-header .header-title {
        font-size: 16px;
    }
    .navigation-header .header-nav-item {
        list-style: none;
        height: 50px;
        display: -webkit-box;
        display: -ms-flexbox;
        display: flex;
        -webkit-box-align: center;
        -ms-flex-align: center;
        align-items: center;
        margin-right: 40px;
        color: #96a2b9;
        min-width: 56px;
    }
    .navigation-header .header-nav-item:hover {
        cursor: pointer;
        color: #d3d9e4;
    }
    .navigation-header .header-nav-item.item-active {
        color: #ffffff !important;
    }
    .navigation-head-nav {
        width: 150px;
        display: -webkit-box;
        display: -ms-flexbox;
        display: flex;
        -webkit-box-orient: vertical;
        -webkit-box-direction: normal;
        -ms-flex-direction: column;
        flex-direction: column;
        background: #ffffff;
        border: 1px solid #e2e2e2;
        -webkit-box-shadow: 0px 3px 4px 0px rgba(64, 112, 203, 0.06);
        box-shadow: 0px 3px 4px 0px rgba(64, 112, 203, 0.06);
        padding: 6px 0;
        margin: 0;
        color: #63656e;
    }
    .navigation-head-nav .nav-item {
        -webkit-box-flex: 0;
        -ms-flex: 0 0 32px;
        flex: 0 0 32px;
        display: -webkit-box;
        display: -ms-flexbox;
        display: flex;
        -webkit-box-align: center;
        -ms-flex-align: center;
        align-items: center;
        padding: 0 20px;
        list-style: none;
    }
    .navigation-head-nav .nav-item:hover {
        color: #3a84ff;
        cursor: pointer;
        background-color: #f0f1f5;
    }
    .tippy-popper .tippy-tooltip.navigation-message-theme {
        padding: 0;
        border-radius: 0;
        -webkit-box-shadow: none;
        box-shadow: none;
    }
    .nav-sign-out {
        display: inline-block;
        cursor: pointer;
        background: #ffffff;
        border: 1px solid #e2e2e2;
        box-shadow: 0px 3px 4px 0px rgb(64 112 203 / 6%);
        padding: 0 25px;
        line-height: 30px;
    }
    .nav-sign-out:hover {
        color: #3a84ff;
        background-color: #f0f1f5;
    }
    .header-user {
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #96a2b9;
    }
    .header-user:hover {
        color: #d3d9e4;
    }
    .header-user .bk-icon {
        margin-left: 5px;
        font-size: 12px;
    }
    .white-theme .header-user {
        color: #63656e;
    }
    .white-theme .header-user:hover {
        color: #3a84ff;
    }
    .nav-head-right {
        color: #d3d9e4;
        margin-left: auto;
        display: flex;
        align-items: center;
        cursor: pointer;
    }

    .bk-navigation .theme-style {
        color: #ffffff;
        opacity: 0.86;
        font-weight: normal;
    }
    .title-desc.white-theme-title {
        color: #313238;
        font-weight: normal;
    }
    .navigation-header .header-nav-item.theme-item {
        color: #ffffff !important;
        opacity: 0.68;
    }
    .navigation-header .header-nav-item.theme-item:hover {
        opacity: 1;
    }
    .header-user.theme-style:hover {
        color: #ffffff;
        opacity: 1;
    }
    .white-navigation .theme-style {
        color: #313238;
    }
    .white-navigation .header-nav-item.theme-item {
        color: #63656e !important;
        opacity: 1;
    }
    .white-navigation .header-nav-item.item-active,
    .white-navigation .header-nav-item.theme-item:hover {
        color: #000000 !important;
    }
    .white-navigation .header-user {
        color: #63656e;
    }
    .white-navigation .header-user:hover {
        color: #000000;
    }
    .white-theme-menu .navigation-sbmenu-title-arrow {
        color: #c4c6cc !important;
    }
    .white-theme-menu-item:hover .navigation-menu-item-name {
        color: #313238 !important;
    }
</style>
