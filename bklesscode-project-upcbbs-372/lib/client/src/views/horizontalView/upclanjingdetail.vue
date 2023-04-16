<template>
    <section class="bk-layout-custom-component-wrapper container-bebcfaka">
        <div class="bk-layout-component-bebcfaka block2136b">
            <!-- eslint-disable -->
            <!-- prettier-ignore -->
            <p title=""   class='bk-layout-component-bebcfaka paragraph7948e'>{{bbsTitle}}</p>
            <!-- eslint-enable -->
        </div>
        <!-- eslint-disable -->
        <!-- prettier-ignore -->
        <p title=""   class='bk-layout-component-bebcfaka paragraph1e298'>{{bbsContent}}</p>
        <!-- eslint-enable -->
        <bk-divider
            direction="horizontal"
            align="left"
            color="#dde4eb"
            class="bk-layout-component-bebcfaka divider72097">
            评论
        </bk-divider>
        <bk-input
            type="textarea"
            font-size="normal"
            :disabled="false"
            :readonly="false"
            :clearable="true"
            :show-controls="true"
            class="bk-layout-component-bebcfaka inputB6961"
            v-model="comment">
        </bk-input>
        <bk-button
            title="hello world"
            size="normal"
            theme="primary"
            :disabled="false"
            :loading="false"
            class="bk-layout-component-bebcfaka button32962"
            @click="addCommentData">
            提交评论
        </bk-button>

        <div
            class="bk-free-layout-bebcfaka free-layout-e8c19"
            v-for="(freeLayoutE8c19Item, freeLayoutE8c19Index) in commentList"
            :key="freeLayoutE8c19Index">
            <div style="position: absolute; top: 9px; left: 0px;">
                <span title="" class="bk-layout-component-bebcfaka textAc96e">
                    {{ freeLayoutE8c19Item.createUser }}</span>
            </div>
            <div style="position: absolute; top: 10px; left: 107px;">
                <span title="" class="bk-layout-component-bebcfaka text1178f">
                    {{ freeLayoutE8c19Item.createTime }}</span>
            </div>
            <div style="position: absolute; top: 59px; left: 0px;">
                <span title="" class="bk-layout-component-bebcfaka textF0333"> {{ freeLayoutE8c19Item.comment }}</span>
            </div>
        </div>
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
                bbsTitle: getInitVariableValue({ all: '', prod: '', stag: '' }, 0),
                bbsContent: getInitVariableValue({ all: '', prod: '', stag: '' }, 0),
                comment: getInitVariableValue({ all: '', prod: '', stag: '' }, 0),
                commentList: getInitVariableValue(
                    { all: [], prod: ['Jack', 'Lucy', 'Lily'], stag: ['Jack', 'Lucy', 'Lily'] },
                    0
                )
            }
        },

        created () {
            this.getData()
        }
    }
</script>
<style lang="css" scoped>
    .container-bebcfaka {
        padding-left: 200px;
        padding-right: 200px;
        padding-top: 20px;
        padding-bottom: 0px;
        height: 100%;
    }
    .bk-layout-row-bebcfaka {
        display: flex;
    }
    .bk-layout-row-bebcfaka:after {
        display: block;
        clear: both;
        content: '';
        font-size: 0;
        height: 0;
        visibility: hidden;
    }
    .bk-layout-col-bebcfaka {
        float: left;
        position: relative;
        min-height: 1px;
    }
    .bk-free-layout-bebcfaka {
        height: 500px;
        width: 100%;
        display: inline-block;
        position: relative;
    }
    .bk-free-layout-item-inner-bebcfaka {
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

    .bk-layout-component-bebcfaka.block2136b {
        display: block;
        width: 100%;
    }
    .bk-layout-component-bebcfaka.paragraph7948e {
        display: inline-block;
        width: 100%;
        height: 32px;
        text-align: center;
        font-size: 14px;
        white-space: pre-wrap;
        word-break: break-all;
        margin-left: 0;
    }
    .bk-layout-component-bebcfaka.paragraph1e298 {
        display: inline-block;
        width: 100%;
        height: 385px;
        text-align: left;
        font-size: 14px;
        white-space: pre-wrap;
        word-break: break-all;
        margin-top: 8px;
        margin-left: 0;
    }
    .bk-layout-component-bebcfaka.divider72097 {
        display: block;
        margin-top: 8px;
    }
    .bk-layout-component-bebcfaka.inputB6961 {
        display: inline-block;
        vertical-align: middle;
        width: 100%;
        margin-top: 8px;
        margin-left: 0;
    }
    .bk-layout-component-bebcfaka.button32962 {
        display: inline-block;
        vertical-align: middle;
        margin-top: 8px;
    }
    .free-layout-e8c19 {
        height: 142px;
        margin-top: 8px;
        margin-left: 0;
        width: 100%;
    }
    .bk-layout-component-bebcfaka.textAc96e {
        display: inline-block;
        text-align: center;
        font-size: 14px;
        vertical-align: middle;
    }
    .bk-layout-component-bebcfaka.text1178f {
        display: inline-block;
        text-align: center;
        font-size: 14px;
        vertical-align: middle;
    }
    .bk-layout-component-bebcfaka.textF0333 {
        display: inline-block;
        text-align: center;
        font-size: 14px;
        vertical-align: middle;
    }
</style>
