export interface Message {
  msg: string

  /** Color of a message. Example: green, red */
  color?: string

  /** Time after which message will be removed automatically */
  time?: number
}
