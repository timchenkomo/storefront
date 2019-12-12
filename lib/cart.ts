import { Book } from './book'

export interface CartItem {
  product: Book;
  quantity: number;
}
