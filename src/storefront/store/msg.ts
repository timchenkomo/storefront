import { Module, VuexModule, Mutation } from 'vuex-module-decorators'
import { Message } from '~/lib/msg.ts'

@Module({
  name: 'msg',
  stateFactory: true,
  namespaced: true
})
export default class MsgModule extends VuexModule {
  messages: Message[] = []

  @Mutation
  public add(msg: Message) {
    msg.time = Date.now() + 3000
    this.messages.push(msg)
  }

  @Mutation
  public remove(msg: Message) {
    this.messages = this.messages.filter(x => x.msg !== msg.msg)
  }

  @Mutation
  public removeByIdx(idx: number) {
    if (idx > -1) {
      this.messages.splice(idx, 1)
    }
  }

  @Mutation
  public clean() {
    this.messages = this.messages
      .filter(x => x.time ? x.time > Date.now() : true)
  }
}
