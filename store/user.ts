import { Module, VuexModule, Action, Mutation } from 'vuex-module-decorators'
import axios from 'axios'
import { SignUpForm, SignInForm } from '@/lib/forms.ts'

@Module({
  name: 'user',
  stateFactory: true,
  namespaced: true
})
export default class UserModule extends VuexModule {
  public isAuthenticated: boolean = false

  @Action public async signUp(form: SignUpForm): boolean {
    const { data } = await axios.post('http://localhost:8000/me/signup', form)
    this.setAuthentication(data.success)
    return data.success
  }

  @Action public async signIn(form: SignInForm): boolean {
    const { data } = await axios.post('http://localhost:8000/me/signin', form)
    this.setAuthentication(data.success)
    return data.success
  }

  @Mutation private setAuthentication(value: boolean) {
    this.isAuthenticated = value
  }
}
