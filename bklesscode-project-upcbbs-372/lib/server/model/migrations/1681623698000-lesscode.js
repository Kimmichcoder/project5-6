const path = require('path')
const { execSql } = require('../../util')

export class Lesscode1681623698000 {
    async up (queryRunner) {
        await execSql(queryRunner, path.resolve(__dirname, './sql/1681623698000-lesscode.sql'))
    }

    async down () {}
}
