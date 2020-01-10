import { Module, VuexModule, Action, Mutation } from 'vuex-module-decorators'
import axios from 'axios'
import { SignUpForm, SignInForm } from '@/lib/forms.ts'
import { UserInfoData } from '@/lib/user.ts'

@Module({
  name: 'user',
  stateFactory: true,
  namespaced: true
})
export default class UserModule extends VuexModule {
  public isAuthenticated: boolean = false
  public name: string = ""
  public token: string = ""

  @Action public async signUp(form: SignUpForm): Promise<boolean> {
    const { data } = await axios.post('/me/signup', form)
    this.setAuthentication("some token to do")
    return data.success
  }

  @Action public async signIn(form: SignInForm): Promise<boolean> {
    const credentials = new FormData()
    credentials.set('username', form.login)
    credentials.set('password', form.password)

    try {
      // authenticate user
      const { data } = await axios.post('/me/signin', credentials)
      const isSignedIn = data.access_token !== undefined
      this.setAuthentication(data.access_token)

      // load all the data
      await this.loadUserData()

      return isSignedIn
    } catch (Exception) {
      return false
    }
  }

  @Action public async loadUserData(): Promise<UserInfoData | undefined> {
    try {
      const { data } = await axios.get('/me')
      this.setUserData(data)
      return data
    } catch {
      return undefined
    }
  }

  @Mutation private setAuthentication(token: string) {
    this.token = token
    this.isAuthenticated = token !== undefined
  }

  @Mutation private setUserData(value: UserInfoData) {
    this.name = value.name
  }
}
