export interface Message {
  msg: string
  color: string

  /** Time after which message will be removed automatically */
  time: number
}
