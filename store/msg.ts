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
    this.messages.push(msg)
  }

  @Mutation
  public remove(msg: Message) {
    this.messages.remove(msg)
  }

  @Mutation
  public removeByIdx(idx: number) {
    if (idx > -1) {
      this.messages.splice(idx, 1)
    }
  }
}
