export interface Group {
  /** Unique ID of group of products. */
  slug: string;

  /** Title of a product. */
  title: string;

  /** Author of a product. */
  author: string;

  /** Url to cover image. */
  cover: string;

  /** Description of a product. */
  description: string;

  /** List of a product varieties. */
  products: Product[]
}

export enum ProductType {
  Digital = 'digital',
  Audio = 'audio',
  Printed = 'printed'
}

export interface Product {
  /** Unique product ID. */
  slug: string;

  /** Type of a product variety. */
  type: ProductType;

  /** Price of a product */
  price: number;

  /** Name of variety */
  title: string;

  /** List of urls to download file */
  urls: UrlInfo[];

  series: string;
  year_published: number;
  publisher: string;
  group_slug: string;
}

export interface UrlInfo {
  url: string;
  size: string;
  ext: string;
}

export const EmptyGroup: Group = {
  slug: 'null', title: 'Empty book', author: 'No one', cover: '', description: '', products: []
}

export const EmptyProduct: Product = {
  id: '',
  price: -1,
  type: ProductType.Digital,
  title: '',
  urls: [],
  series: '',
  year_published: 0,
  publisher: ''
}

export function productType(t: string): string {
  if (t === 'digital') { return 'Эл. книга' }
  if (t === 'audio') { return 'Аудиокнига' }
  if (t === 'printed') { return 'Печатная' }
  return 'Книга'
}
