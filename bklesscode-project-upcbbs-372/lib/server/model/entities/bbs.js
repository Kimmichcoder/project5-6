import { Entity, Column } from 'typeorm'
import Base from './base'

@Entity({ name: 'bbs' })
export default class extends Base {
    @Column({ name: 'title', type: 'varchar', length: 255 })
    'title'

    @Column({ name: 'content', type: 'text' })
    'content'
}
