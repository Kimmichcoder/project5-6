-- ----------------------------
-- TABLE STRUCTURE FOR comment
-- ----------------------------
CREATE TABLE `comment`  (
    `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '自增唯一主键。系统保留字段，不可修改',
    `createTime` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '系统会默认写入数据创建时间。系统保留字段，不推荐修改',
    `createUser` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '系统会默认写入数据创建人。系统保留字段，不推荐修改',
    `updateTime` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '系统会默认写入数据更新时间。系统保留字段，不推荐修改',
    `updateUser` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '系统会默认写入数据更新人。系统保留字段，不推荐修改',
    `comment` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
    `bbdid` int(11) NOT NULL,
    PRIMARY KEY (`id`) USING BTREE,
    INDEX `id`(`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT 'comment' ROW_FORMAT = Dynamic;
