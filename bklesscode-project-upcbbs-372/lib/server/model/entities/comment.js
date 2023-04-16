import { Entity, Column } from 'typeorm'
import Base from './base'

@Entity({ name: 'comment' })
export default class extends Base {
    @Column({ name: 'comment', type: 'varchar', length: 255 })
    'comment'

    @Column({ name: 'bbdid', type: 'int' })
    'bbdid'
}
