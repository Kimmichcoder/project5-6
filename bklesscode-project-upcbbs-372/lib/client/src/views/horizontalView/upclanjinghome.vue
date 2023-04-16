<template>
    <section class="bk-layout-custom-component-wrapper container-nmfbfanc">
        <bk-swiper
            :is-loop="true"
            :loop-time="8000"
            :pics="swiper656f9pics"
            class="bk-layout-component-nmfbfanc swiper656f9">
        </bk-swiper>
        <bk-sideslider
            :is-show.sync="isshowEdit"
            title="新增帖子1"
            :quick-close="true"
            :show-mask="true"
            :width="600"
            direction="right"
            class="bk-layout-component-nmfbfanc sidesliderC26f0">
            <template slot="content">
                <div class="bk-layout-component-nmfbfanc block68fe2">
                    <div class="bk-layout-component-nmfbfanc" style="">
                        <bk-form
                            :model="form49b8dmodel"
                            :rules="form49b8drules"
                            ref="form"
                            form-type="horizontal"
                            :label-width="150">
                            <bk-form-item
                                property="title"
                                label="标题"
                                :label-width="150"
                                error-display-type="normal"
                                :required="false"
                                :icon-offset="8"
                                :auto-check="false"
                                class="bk-layout-component-nmfbfanc">
                                <bk-input
                                    type="text"
                                    font-size="normal"
                                    :disabled="false"
                                    :readonly="false"
                                    :clearable="true"
                                    :show-controls="true"
                                    class="bk-layout-component-nmfbfanc input84439"
                                    v-model="form49b8dmodel.title">
                                </bk-input>
                            </bk-form-item>
                            <bk-form-item
                                property="content"
                                label="内容"
                                :label-width="150"
                                error-display-type="normal"
                                :required="false"
                                :icon-offset="8"
                                :auto-check="false"
                                class="bk-layout-component-nmfbfanc">
                                <bk-input
                                    type="textarea"
                                    font-size="normal"
                                    :disabled="false"
                                    :readonly="false"
                                    :clearable="true"
                                    :show-controls="true"
                                    class="bk-layout-component-nmfbfanc input4c38d"
                                    v-model="form49b8dmodel.content">
                                </bk-input>
                            </bk-form-item>
                            <bk-form-item
                                property=""
                                label=""
                                :label-width="150"
                                error-display-type="normal"
                                :required="false"
                                :icon-offset="8"
                                :auto-check="false"
                                class="bk-layout-component-nmfbfanc">
                                <bk-button
                                    title="hello world"
                                    size="normal"
                                    theme="primary"
                                    :disabled="false"
                                    :loading="false"
                                    class="bk-layout-component-nmfbfanc button22216"
                                    @click="addBBSData">
                                    提交
                                </bk-button>
                                <bk-button
                                    title="hello world"
                                    size="normal"
                                    theme="default"
                                    :disabled="false"
                                    :loading="false"
                                    class="bk-layout-component-nmfbfanc buttonEabbc">
                                    取消
                                </bk-button>
                            </bk-form-item>
                        </bk-form>
                    </div>
                </div>
            </template>
        </bk-sideslider>

        <div class="bk-layout-row-nmfbfanc grid-b3da4">
            <div class="bk-layout-col-nmfbfanc column-2c4b9">
                <bk-button
                    title="hello world"
                    size="normal"
                    theme="primary"
                    :disabled="false"
                    :loading="false"
                    class="bk-layout-component-nmfbfanc button032eb"
                    @click="changeishsowEdit">
                    新建帖子
                </bk-button>

                <div
                    class="bk-free-layout-nmfbfanc free-layout-e38df"
                    v-for="(freeLayoutE38dfItem, freeLayoutE38dfIndex) in bbslist"
                    :key="freeLayoutE38dfIndex">
                    <div style="position: absolute; top: 5px; left: 0px;">
                        <bk-link
                            theme="primary"
                            href=""
                            :disable="false"
                            :underline="false"
                            icon=""
                            icon-placement="left"
                            class="bk-layout-component-nmfbfanc link612e2"
                            @click="(...args) => goToDetail(freeLayoutE38dfItem.id, ...args)">
                            <render-html :html="freeLayoutE38dfItem.title"></render-html></bk-link>
                    </div>
                    <div style="position: absolute; top: 36px; left: 0px;">
                        <span title="" class="bk-layout-component-nmfbfanc textA17a7">
                            {{ freeLayoutE38dfItem.createUser }}</span>
                    </div>
                    <div style="position: absolute; top: 36px; left: 75px; width: 231px;">
                        <span title="" class="bk-layout-component-nmfbfanc text1c707">
                            {{ freeLayoutE38dfItem.createTime }}</span>
                    </div>
                    <div style="position: absolute; top: 37px; left: 385px;">
                        <bk-animate-number
                            :value="0"
                            :digits="0"
                            class="bk-layout-component-nmfbfanc animateNumber8dd25"></bk-animate-number>
                    </div>
                    <div style="position: absolute; top: 36px; left: 363px;">
                        <bk-icon type="password" size="14px" class="bk-layout-component-nmfbfanc bkIconE0174"></bk-icon>
                    </div>
                </div>

                <bk-divider
                    direction="horizontal"
                    align="center"
                    color="#dde4eb"
                    class="bk-layout-component-nmfbfanc divider9ce10">
                </bk-divider>
            </div>
            <div class="bk-layout-col-nmfbfanc column-598e9">
                <!-- eslint-disable -->
                <!-- prettier-ignore -->
                <p title=""   class='bk-layout-component-nmfbfanc paragraphA168d'>中国石油大学（华东）（China University of Petroleum (East China)  ，位于山东省青岛市，是中华人民共和国教育部直属全国重点大学，教育部和五大能源企业集团公司、教育部和山东省人民政府共建，为国家“双一流”、“211工程”重点建设高校，高水平行业特色大学优质资源共享联盟成员，入选985工程优势学科创新平台、111计划、卓越工程师教育培养计划、全国毕业生就业典型经验高校、全国深化创新创业教育改革示范高校、中俄工科大学联盟成员高校，是石油、石化高层次人才培养的重要基地，设有研究生院和国家大学科技园。</p>
                <!-- eslint-enable -->
            </div>
        </div>

        <bk-sideslider
            :is-show.sync="isshowEdit"
            title="新增帖子"
            :quick-close="true"
            :show-mask="true"
            :width="600"
            direction="right"
            class="bk-layout-component-nmfbfanc sideslider3012d">
            <template slot="content">
                <div class="bk-layout-component-nmfbfanc blockB61b5">
                    <div class="bk-layout-component-nmfbfanc" style="">
                        <bk-form
                            :model="formCd7b5model"
                            :rules="formCd7b5rules"
                            ref="form"
                            form-type="horizontal"
                            :label-width="150">
                            <bk-form-item
                                property="title"
                                label="标题"
                                :label-width="150"
                                error-display-type="normal"
                                :required="false"
                                :icon-offset="8"
                                :auto-check="false"
                                class="bk-layout-component-nmfbfanc">
                                <bk-input
                                    type="text"
                                    font-size="normal"
                                    :disabled="false"
                                    :readonly="false"
                                    :clearable="true"
                                    :show-controls="true"
                                    class="bk-layout-component-nmfbfanc inputC9013"
                                    v-model="formCd7b5model.title">
                                </bk-input>
                            </bk-form-item>
                            <bk-form-item
                                property="content"
                                label="内容"
                                :label-width="150"
                                error-display-type="normal"
                                :required="false"
                                :icon-offset="8"
                                :auto-check="false"
                                class="bk-layout-component-nmfbfanc">
                                <bk-input
                                    type="textarea"
                                    font-size="normal"
                                    :disabled="false"
                                    :readonly="false"
                                    :clearable="true"
                                    :show-controls="true"
                                    class="bk-layout-component-nmfbfanc input98904"
                                    v-model="formCd7b5model.content">
                                </bk-input>
                            </bk-form-item>
                            <bk-form-item
                                property=""
                                label=""
                                :label-width="150"
                                error-display-type="normal"
                                :required="false"
                                :icon-offset="8"
                                :auto-check="false"
                                class="bk-layout-component-nmfbfanc">
                                <bk-button
                                    title="hello world"
                                    size="normal"
                                    theme="primary"
                                    :disabled="false"
                                    :loading="false"
                                    class="bk-layout-component-nmfbfanc button7f921"
                                    @click="addBBSData">
                                    提交
                                </bk-button>
                                <bk-button
                                    title="hello world"
                                    size="normal"
                                    theme="default"
                                    :disabled="false"
                                    :loading="false"
                                    class="bk-layout-component-nmfbfanc button65719">
                                    取消
                                </bk-button>
                            </bk-form-item>
                        </bk-form>
                    </div>
                </div>
            </template>
        </bk-sideslider>
    </section>
</template>
<script>
    /**
     * 请先安装 bk-magic-vue 组件库、bkui-vue-complex 复合组件库
     * bk-magic-vue 组件库: https://magicbox.bk.tencent.com/static_api/v3/components_vue/2.0/example/index.html#/install
     * bkui-vue-complex 复合组件库: https://github.com/TencentBlueKing/lesscode-comp
     *
     * 如果页面使用了远程函数，单独使用本页面，需要确保项目 store 下有相应的方法，后端有相应的转发接口
     */

    import methodsMixin from '@/mixins/methods-mixin'
    export default {
        mixins: [methodsMixin],
        data () {
            function getInitVariableValue (defaultValue, defaultValueType) {
                let val = defaultValue.all
                if (defaultValueType === 1) val = defaultValue[window.BKPAAS_ENVIRONMENT]
                return val
            }
            return {
                swiper656f9pics: [
                    {
                        url:
                            'https://magicbox.bk.tencent.com/static_api/v3/components_vue/2.0/example/example/static/images/firstswiper.jpg'
                    },
                    {
                        url:
                            'https://magicbox.bk.tencent.com/static_api/v3/components_vue/2.0/example/example/static/images/secondswiper.jpg'
                    }
                ],
                form49b8dmodel: { title: '', content: '' },
                form49b8drules: { content: [], title: [] },
                formCd7b5model: { title: '', content: '' },
                formCd7b5rules: { title: [], content: [] },
                isshowEdit: getInitVariableValue({ all: false, prod: false, stag: false }, 0),
                bbslist: getInitVariableValue(
                    { all: [], prod: ['Jack', 'Lucy', 'Lily'], stag: ['Jack', 'Lucy', 'Lily'] },
                    0
                )
            }
        },

        created () {
            this.getBBSDataList()
        }
    }
</script>
<style lang="css" scoped>
    .container-nmfbfanc {
        padding-left: 200px;
        padding-right: 200px;
        padding-top: 20px;
        padding-bottom: 0px;
        height: 100%;
    }
    .bk-layout-row-nmfbfanc {
        display: flex;
    }
    .bk-layout-row-nmfbfanc:after {
        display: block;
        clear: both;
        content: '';
        font-size: 0;
        height: 0;
        visibility: hidden;
    }
    .bk-layout-col-nmfbfanc {
        float: left;
        position: relative;
        min-height: 1px;
    }
    .bk-free-layout-nmfbfanc {
        height: 500px;
        width: 100%;
        display: inline-block;
        position: relative;
    }
    .bk-free-layout-item-inner-nmfbfanc {
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

    .bk-layout-component-nmfbfanc.swiper656f9 {
        width: 100%;
        height: 300px;
        margin-left: 0;
    }
    .bk-layout-component-nmfbfanc.sidesliderC26f0 {
        display: inline-block;
    }
    .bk-layout-component-nmfbfanc.block68fe2 {
        display: block;
        width: 100%;
    }
    .bk-layout-component-nmfbfanc.input84439 {
        display: inline-block;
        vertical-align: middle;
        width: 300px;
    }
    .bk-layout-component-nmfbfanc.input4c38d {
        display: inline-block;
        vertical-align: middle;
        width: 300px;
    }
    .bk-layout-component-nmfbfanc.button22216 {
        display: inline-block;
        vertical-align: middle;
        width: 88px;
    }
    .bk-layout-component-nmfbfanc.buttonEabbc {
        display: inline-block;
        vertical-align: middle;
        width: 88px;
        margin-left: 8px;
    }
    .grid-b3da4 {
        margin-top: 30px;
        height: 424px;
    }
    .column-2c4b9 {
        width: 75%;
    }
    .bk-layout-component-nmfbfanc.button032eb {
        display: inline-block;
        vertical-align: middle;
    }
    .free-layout-e38df {
        height: 75px;
        margin-top: 8px;
        margin-left: 0;
        width: 100%;
    }
    .bk-layout-component-nmfbfanc.link612e2 {
        display: inline-block;
        text-align: center;
        vertical-align: middle;
    }
    .bk-layout-component-nmfbfanc.textA17a7 {
        display: inline-block;
        text-align: center;
        font-size: 14px;
        vertical-align: middle;
    }
    .bk-layout-component-nmfbfanc.text1c707 {
        display: inline-block;
        text-align: center;
        font-size: 14px;
        vertical-align: middle;
        width: 231px;
    }
    .bk-layout-component-nmfbfanc.animateNumber8dd25 {
        display: inline-block;
        vertical-align: middle;
    }
    .bk-layout-component-nmfbfanc.bkIconE0174 {
        display: inline-block;
        font-size: 14px;
        vertical-align: middle;
    }
    .bk-layout-component-nmfbfanc.divider9ce10 {
        display: block;
        margin-top: 8px;
    }
    .column-598e9 {
        width: 25%;
        margin-left: -4px;
    }
    .bk-layout-component-nmfbfanc.paragraphA168d {
        display: inline-block;
        width: 258px;
        text-align: left;
        font-size: 14px;
        white-space: pre-wrap;
        word-break: break-all;
        margin-left: 20px;
    }
    .bk-layout-component-nmfbfanc.sideslider3012d {
        display: inline-block;
    }
    .bk-layout-component-nmfbfanc.blockB61b5 {
        display: block;
        width: 100%;
    }
    .bk-layout-component-nmfbfanc.inputC9013 {
        display: inline-block;
        vertical-align: middle;
        width: 300px;
    }
    .bk-layout-component-nmfbfanc.input98904 {
        display: inline-block;
        vertical-align: middle;
        width: 300px;
    }
    .bk-layout-component-nmfbfanc.button7f921 {
        display: inline-block;
        vertical-align: middle;
        width: 88px;
    }
    .bk-layout-component-nmfbfanc.button65719 {
        display: inline-block;
        vertical-align: middle;
        width: 88px;
        margin-left: 8px;
    }
</style>
